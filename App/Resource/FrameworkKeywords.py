from CustomHTMLReportLibrary import *
from robot.libraries.BuiltIn import BuiltIn
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement 
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import ActionChains

import Environment
import time
import subprocess
import platform

# This global variable controls webdriver session
driver: webdriver = None
global_suite_name = ""
testcase_status: str = "PASS"
excel_file = ""

def set_driver( driver_instance: webdriver ):
    global driver 
    driver = driver_instance
    
def get_driver()->webdriver:
    global driver
    return driver

def get_git_root():
    return subprocess.Popen(['git', 'rev-parse', '--show-toplevel'], stdout=subprocess.PIPE).communicate()[0].rstrip().decode('utf-8')

def get_excel_file():
    global excel_file
    return excel_file

def get_biq_url():
    if Environment.env_name.upper() != "DEV" and Environment.env_name.upper() != "QA" and Environment.env_name.upper() != "UAT":
        BuiltIn().fail("Environment "+Environment.env_name+" not supported.  Should be dev, qa or uat.  Please check your Environment.py")  
    return Environment.biq_url[Environment.env_name]

def set_excel_file( filename ):
    global excel_file
    excel_file = filename

def suite_setup(suite_name: str, excel_name: str="MasterTestData.xls"):
    # Sets debug level on robot
    BuiltIn().set_log_level("INFO")
    git_root = get_git_root()
    BuiltIn().log_to_console("GIT ROOT IS:"+git_root)
    # Environment setup
    # Test results settings
    if ( "." in suite_name ): # In the form of full name we have to remove path
        paths = suite_name.split(".")
        suite_name = paths[len(paths)-1]
    global global_suite_name
    global_suite_name = suite_name
    result_folder = BuiltIn().get_variable_value("${OUTPUT_DIR}").replace("\\","/")
    if "pabot_results" in result_folder: # Running with pabot
        result_folder = os.path.abspath(result_folder+"../../..")
    BuiltIn().log_to_console("HTML results folder="+result_folder)
    dt_tme = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    # Naming logic for runs
    if platform.system() == 'Linux':
        Environment.runName = suite_name +"-Build " + os.getenv( "BUILD_ID")
    else: # Windows
        if Environment.runName == 'Auto':
            Environment.runName = suite_name+"-"+dt_tme
   
    suite_result_folder = suite_name + "_" + dt_tme
    suite_result_folder = os.path.join(result_folder, suite_result_folder)
    suite_result_html = os.path.join(suite_result_folder, suite_name + ".html")
    if not os.path.exists(suite_result_folder):
        os.makedirs(suite_result_folder, exist_ok=True)

    details_folder = os.path.join(suite_result_folder, "Details")
    if not os.path.exists(details_folder):
        os.makedirs(details_folder, exist_ok=True)

    screenshot_path = os.path.join(suite_result_folder, "Screenshots")
    if not os.path.exists(screenshot_path):
        os.makedirs(screenshot_path, exist_ok=True)
    global excel_file

    excel_file = git_root.replace("\\","/")+"/App/TestData/"+Environment.env_name.upper()+"/"+excel_name
    BuiltIn().log_to_console("USING EXCEL FILE:"+excel_file)
    BuiltIn().set_global_variable("${resultFolder}", result_folder.replace("\\", "/"))
    BuiltIn().set_global_variable("${suite_result_folder}", suite_result_folder.replace("\\", "/"))    
    BuiltIn().set_global_variable("${suite_result}", suite_result_html.replace("\\", "/"))
    BuiltIn().set_global_variable("${detailsFolderPath}", details_folder.replace("\\", "/"))
    BuiltIn().set_global_variable("${screenshotPath}", screenshot_path.replace("\\", "/"))
    BuiltIn().log_to_console("RESULT FOLDER IS:"+result_folder.replace("\\", "/"))

    generate_suite_report_header(suite_result_html, suite_name)

def report(step_description, expected_result, actual_result, status):
    screenshot_path = BuiltIn().get_variable_value("${screenshotPath}")
    test_result_path = BuiltIn().get_variable_value("${testResultpath}")
    result_folder = BuiltIn().get_variable_value("${resultFolder}")
    tm = get_current_timestamp()
    BuiltIn().log_to_console( "STEP="+ step_description+" EXPECTED="+expected_result+" ACTUAL="+actual_result+" STATUS="+status)

    screenshot_name = 'Screen_'+tm+'.png'
    screenshot = os.path.join(screenshot_path, screenshot_name).replace("\\", "/")
    # Adds relative images for robot 
    screenshot_robot_relative_path = os.path.relpath(screenshot, result_folder)
    robot_img_html = "<img src='"+ screenshot_robot_relative_path + "' width='50%' height='50%'"
    try:
        driver = get_driver()
        if driver != None:
            driver.save_screenshot(screenshot)
    except Exception as e:
        BuiltIn().log("***************FAILED SCREENSHOT*****************")
    global     testcase_status
    if "FAIL" in status:
        if testcase_status in "FAIL": # Already failed
            BuiltIn().fail("STEP="+ step_description+" EXPECTED="+expected_result+" ACTUAL="+actual_result+" STATUS="+status)
        else:
            testcase_status = "FAIL"
            if ( test_result_path != None ): # At least one test is in execution.
                write_result_to_TestReport(test_result_path, screenshot_name, step_description, expected_result, actual_result, status)
            BuiltIn().log( robot_img_html, html=True)
            BuiltIn().fail(" STEP="+ step_description+" EXPECTED="+expected_result+" ACTUAL="+actual_result
                            +" STATUS="+status+"\n", actual_result)
    elif "PASS" in status:
        BuiltIn().log( "STEP="+ step_description+" EXPECTED="+expected_result+" ACTUAL="+actual_result+" STATUS="+status, html=True)
        if ( test_result_path != None ): # At least one test is in execution.
            write_result_to_TestReport(test_result_path, screenshot_name, step_description, expected_result, actual_result, status)
        if platform.system() == 'Windows':
            BuiltIn().log( robot_img_html, html=True)
    else:
        BuiltIn().fail("ERROR: Unrecognized Status parameter on report()")
        
def test_setup(test_name:str, export: bool=True):
    details_folder = BuiltIn().get_variable_value("${detailsFolderPath}")
    test_result = generate_test_report_header(details_folder, test_name)
    BuiltIn().set_global_variable("${testResultpath}", test_result.replace("\\", "/"))
    global testcase_status
    testcase_status = "PASS"
    global  global_suite_name
    if export:
        export_variables(excel_file, global_suite_name.split("-")[0], test_name)
    if not Environment.local_browser:
        driver = open_or_get_browser()
        if driver != None:
            driver.execute_script("lambda-name="+BuiltIn().get_variable_value("${TEST_NAME}")); # Change name on Lambdatest
        else:
            BuiltIn().log_to_console("\nWARNING: Webdriver session is closed on test_setup().")

def export_variables(excel_file, sheet_name, test_name):
    try:
        df = pd.read_excel(excel_file, dtype=str)
        test_data_set = df[df.TestName == test_name].replace(np.nan, '', regex=True)
        print( test_data_set )
        for k in test_data_set.items():
            BuiltIn().set_test_variable("${" + k[0] + "}", test_data_set[k[0]].values[0])
    except Exception as ex:
        BuiltIn().log_to_console("ERROR on Excel file"+excel_file+" exception:"+str( ex ) )
        BuiltIn().fail("ERROR on Excel file.   Test name="+test_name+" not found on sheet "+sheet_name)

def get_variable_value( sheet_name, test_name, variable_name):
    try:
        global excel_file
        df = pd.read_excel(excel_file, dtype=str)
        test_data_set = df[df.TestName == test_name].replace(np.nan, '', regex=True)
        print( test_data_set )
        for k in test_data_set.items():
            if k[0] == variable_name:
                return test_data_set[k[0]].values[0]
        return None
    except Exception as ex:
        BuiltIn().log_to_console("ERROR on Excel file"+excel_file+" exception:"+str( ex ) )
        BuiltIn().log_to_console("ERROR on Excel file.   Test name="+test_name+" not found on sheet "+sheet_name)
        BuiltIn().fail("ERROR on Excel file.   Test name="+test_name+" not found on sheet "+sheet_name)
        
def end_test(test_name, test_description, close_session: bool = True):
    test_result_path = BuiltIn().get_variable_value("${testResultpath}")
    suite_result = BuiltIn().get_variable_value("${suite_result}")
    global testcase_status 
    log_execution_endtime_to_report_file(test_result_path)
    write_result_to_SuiteReport(suite_result, test_result_path, test_name, test_description, testcase_status)
    global driver
    driver = get_driver()
    if driver != None:
        if ( not Environment.local_browser ):
            if testcase_status == 'FAIL':
                driver.execute_script('lambda-status=failed')
            else:
                driver.execute_script('lambda-status=passed')
        if close_session:
            BuiltIn().log_to_console("\nCLOSING WEBDRIVER SESSION.")
            driver.quit()
            driver = None
            set_driver(None)
    else: # driver==None
        if close_session:
            BuiltIn().log_to_console("\nERROR: end_test() CANNOT CLOSE WEBDRIVER SESSION.")
            BuiltIn().fail("\nERROR: end_test() CANNOT CLOSE WEBDRIVER SESSION.")          

def open_or_get_browser()->webdriver:
    global driver
    username = Environment.userName
    access_key = Environment.accessKey
    try:
        driver = get_driver()
        if driver == None: # Get a new session
            desired_caps: DesiredCapabilities().CHROME = {
                "project": Environment.project_name,
                "build": Environment.runName,  # Change your build name here
                "browserName": Environment.browserName,
                "browserVersion": Environment.browserVersion,
                "platform": Environment.os,
                "idleTimeout": Environment.idleTimeout,
                "selenium_version": Environment.seleniumVersion,
                "console": True,  # Enable or disable console logs
                "network": False,  # Enable or disable network logs
                "terminal": True, # Enable or disable terminal logs
                "acceptInsecureCerts": True, # Accept all certificates W3C
                "acceptSslCerts": True, # Accept all certificates JSON
                "pageLoadStrategy": "eager"
            }
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-infobars")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")            
            options.add_argument("start-maximized")
            # options.add_argument("disable-notifications")
            # options.add_argument("--disable-infobars")
            # options.add_argument("--disable-notifications")
            # options.add_argument("--disable-notifications")
            # options.add_argument("--suppress-message-center-popups")
            # options.add_argument("suppress-message-center-popups")
            options.add_argument('ignore-certificate-errors') 
            prefs = {"credentials_enable_service": False,"profile.password_manager_enabled": False}
            options.add_experimental_option("prefs", prefs)           
            # if Environment.removeImages:
            #     prefs = {"profile.managed_default_content_settings.images": 2}
            #     options.add_experimental_option("prefs", prefs)
            if platform.system() == 'Linux':
                Environment.local_browser = False # Enforces Lambdatest on Linux.
            BuiltIn().log_to_console("\nCREATING WEBDRIVER SESSION")
            if Environment.local_browser == True:
                driver = webdriver.Chrome(desired_capabilities=desired_caps, chrome_options=options)
                if driver == None:
                    BuiltIn().fail("ERROR: Cannot get webdriver session.")                
                else:
                    BuiltIn().log_to_console("RUNNING ON LOCAL CHROME/WINDOWS")
            else:
                driver = webdriver.Remote(command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key),
                                          desired_capabilities=desired_caps, options=options, keep_alive=True)
                if driver == None:
                    BuiltIn().fail("ERROR: Cannot get webdriver session.")                
                else:
                    if platform.system() == 'Linux':
                        BuiltIn().log_to_console("RUNNING ON LAMBDATEST/LINUX")                
                    else:
                        BuiltIn().log_to_console("RUNNING ON LAMBDATEST/WINDOWS")
            set_driver( driver )
        else:               
            driver.implicitly_wait( Environment.implicit_timeout_in_seconds )
    except Exception as ex:
        BuiltIn().fail("Failed open_or_get_browser:"+str(ex))
    return driver

def close_browser():
    global driver
    driver = get_driver()
    driver.close()
    driver = None
    
def close_session():
    global driver
    driver = get_driver()
    driver.quit()
    driver = None

def get_current_timestamp():
    dt_time:str = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    return dt_time

def waitForAlertPresent(timeOutInSeconds=Environment.explicit_timeout_in_seconds):
    try:
        driver = open_or_get_browser()
        WebDriverWait(driver, timeOutInSeconds, poll_frequency=1, ignored_exceptions=[StaleElementReferenceException]).until(EC.alert_is_present)
        return True
    except Exception as e:
        return False

def clickOKOnAlert(timeOutInSeconds=Environment.explicit_timeout_in_seconds):
    try:
        driver = open_or_get_browser()
        waitForAlertPresent(timeOutInSeconds)
        driver.switch_to_alert().accept()
    except Exception as e:
        raise Exception("Can not click Ok on alert.")

def clickCancelOnAlert(timeOutInSeconds=Environment.explicit_timeout_in_seconds):
    try:
        driver = open_or_get_browser()
        waitForAlertPresent(timeOutInSeconds)
        driver.switch_to_alert().dismiss()
    except Exception as e:
        raise Exception("Can not click Cancel on alert.")
    
def browser_back():
    BuiltIn().log_to_console( "browser back")
    driver = open_or_get_browser()
    driver.back()

def browser_refresh():
    BuiltIn().log_to_console( "browser refresh")
    driver = open_or_get_browser()
    driver.refresh()
    
def set_zoom_level_of_current_page_to( percentage: int):
    BuiltIn().log_to_console( message="Set zoom level to "+ str(percentage)+"%", no_newline=True)
    driver = open_or_get_browser()        
    driver.execute_script("document.body.style.zoom='" + str(percentage) + "%'")
    BuiltIn().log_to_console(" done.\n")

def scroll_into_view_to_element( locator ):
    element = find_element_with_locator( locator )
    driver = open_or_get_browser()
    driver.execute_script("arguments[0].scrollIntoView();", element)
def scroll_center_view_to_element( locator ):
    element = find_element_with_locator( locator )
    driver = open_or_get_browser()    
    element = find_element_with_locator( locator )
    driver.execute_script("arguments[0].scrollIntoView({'block':'center','inline':'center'})", element)
 
def highlight(element:WebElement, effect_time=1, color='red', border=2):
    """Highlights (blinks) a Selenium Webdriver element"""
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)
    original_style = element.get_attribute('style')
    apply_style("border: {0}px solid {1};".format(border, color))
    time.sleep(effect_time)
    apply_style(original_style)    
def switch_to_window_by_handle( handle ):
    BuiltIn().log_to_console( "switch_to_window_by_handle "+handle)
    driver = open_or_get_browser()
    driver.switch_to.window(handle)
    
def get_window_handle_by_title(title):
    '''Search a window handle by title'''
    driver = open_or_get_browser()
    windows_handles = driver.window_handles
    handle = None
    BuiltIn().log_to_console( "get_window_handle_by_title..."+title)
    for window_handle in windows_handles:
        driver.switch_to.window(window_handle)
        if driver.title == title:
            handle = window_handle
            break
    if handle is None:
        BuiltIn().log_to_console( "not found.\n")
    else:
        BuiltIn().log_to_console( "found.\n")
    return handle

def get_location_method( locator: str ):
    location_method:str = locator[ 0: locator.find('=')]
    return location_method.lower()

def get_location_expression( locator: str ):
    size = locator.__len__()
    location_expression = locator[locator.find('=')+1: size ]
    return location_expression

def click_js(element: WebElement, verbose: bool = True):
    '''Do click when an element is not clickable with classic selenium click method. Uses JS executor'''
    if verbose:
        BuiltIn().log_to_console( message="click_js "+ str(element), no_newline=True)
    try:
        driver = open_or_get_browser()        
        driver.execute_script("arguments[0].click();", element)
        if verbose:
            BuiltIn().log_to_console("done.\n")
        return True
    except Exception as e:
        if verbose:
            BuiltIn().log_to_console("failed!!! "+ e.__str__())
        return False

def click_element_and_wait_next_element_with_retry( locator, next_element_to_wait_locator, retries: int=Environment.retry_times ):
    """Do click retries times on hard to click elements, i.e. that takes time to render and when clicked does not do anything."""
    BuiltIn().log_to_console("click_element_with_retry on:"+locator)
    if wait_until_locator_is_present(locator) == False:
        report("click_element_with_retry", "", "Element "+locator+" not found.", "FAIL")

    BuiltIn().log_to_console("click_element_with_retry on:"+locator+" found.")

    for retry in range(1, retries):
        BuiltIn().log_to_console("Click retry nº "+str(retry))
        click_locator( locator )
        if find_element_with_locator(next_element_to_wait_locator):
            return True

    raise AssertionError("click_element_with_retry: Click on "+locator +" did not act, and/or not found element "+next_element_to_wait_locator+"\n")

def clickjs_element_and_wait_next_element_with_retry( locator, next_element_to_wait_locator, retries: int=Environment.retry_times ):
    """Do click retries times on hard to click elements, i.e. that takes time to render and when clicked does not do anything."""
    BuiltIn().log_to_console("click_element_with_retry on:"+locator)
    if wait_until_locator_is_present(locator) == False:
        report("click_element_with_retry", "", "Element "+locator+" not found.", "FAIL")

    BuiltIn().log_to_console("click_element_with_retry on:"+locator+" found.")

    for retry in range(1, retries):
        BuiltIn().log_to_console("Click retry nº "+str(retry))
        element: WebElement = find_element_with_locator(locator)
        click_js( element )
        if find_element_with_locator(next_element_to_wait_locator):
            return True

    raise AssertionError("click_element_with_retry: Click on "+locator +" did not act, and/or not found element "+next_element_to_wait_locator+"\n")

def find_element_with_locator( locator, verbose:bool = True )->WebElement:
    if verbose == True:
        BuiltIn().log_to_console(message="find_element_with_locator "+locator+"...", no_newline=True )
    element: WebElement = None
    try:
        location_method = get_location_method( locator )
        location_expression = get_location_expression( locator )
        driver:webdriver = open_or_get_browser()
        element = driver.find_element(location_method, location_expression)
        if verbose:
            BuiltIn().log_to_console("found!!!" )
            highlight(element)
        return element
    except Exception as e:
        if verbose:
            BuiltIn().log_to_console("failed!!! "+ e.__str__())
        return None

def find_elements_with_locator( locator, verbose: bool= True )->list[WebElement]:
    if verbose:
        BuiltIn().log_to_console(message="find_elements_with_locator "+locator+"...", no_newline=True )
    elements: list[WebElement] = None
    try:
        location_method = get_location_method( locator )
        location_expression = get_location_expression( locator )
        driver: webdriver = open_or_get_browser()
        elements = driver.find_elements(location_method, location_expression)
        if elements == [] and verbose:
            BuiltIn().log_to_console("not found!!!" )
        else:
            if verbose:
                BuiltIn().log_to_console("found!!!" )
        return elements

    except Exception as e:
        BuiltIn().log_to_console("failed!!! "+ e.__str__())
        return None
        
def click_locator( locator ):
    try:
        BuiltIn().log_to_console( message="Click on "+str(locator), no_newline=True)
        locator_tuple = (get_location_method( locator ), get_location_expression( locator ))
        WebDriverWait(driver, Environment.explicit_timeout_in_seconds).until(EC.element_to_be_clickable(locator_tuple))
        element: WebElement = find_element_with_locator( locator, verbose=False )
        element.click()
        BuiltIn().log_to_console(" done!!! ")
        return True
    except Exception as e:
        BuiltIn().log_to_console(" failed!!! "+ e.__str__())
        return False
    
def click_web_element( element: WebElement ):
    BuiltIn().log_to_console( "Click on web element"+str(element))
    driver = open_or_get_browser()
    WebDriverWait(driver, Environment.explicit_timeout_in_seconds).until(EC.element_to_be_clickable(element))
    element.click()    
    
def clear_input_locator( locator ):
    BuiltIn().log_to_console( "Clear on "+locator)
    driver = open_or_get_browser()
    input_element: WebElement = find_element_with_locator( locator )
    locator_tuple = (get_location_method( locator ), get_location_expression( locator ))
    WebDriverWait(driver, Environment.explicit_timeout_in_seconds, ignored_exceptions=[StaleElementReferenceException]).until(EC.element_to_be_clickable(locator_tuple))
    input_element.clear()

def send_keys(locator, text_value: str, clear_input: bool=True, verbose: bool= True):
    if verbose:
        BuiltIn().log_to_console("SendKeys to "+str(locator)+" Text="+text_value)
    input_element: WebElement = find_element_with_locator(locator, False)
    if input_element == None:
        BuiltIn().fail("Element "+ locator + " not found!.")
    locator_tuple = (get_location_method(locator), get_location_expression(locator))
    WebDriverWait(driver, Environment.explicit_timeout_in_seconds, ignored_exceptions=[StaleElementReferenceException]).until(EC.element_to_be_clickable(locator_tuple))
    click_js(input_element, False)
    if clear_input:
        input_element.clear()
    input_element.send_keys(text_value)

def location_should_contain( url:str ):
    BuiltIn().log_to_console( "Current location should contain "+url)
    driver = open_or_get_browser()
    try:
        WebDriverWait(driver, Environment.explicit_timeout_in_seconds).until(EC.url_contains( url ))
        BuiltIn().log_to_console("done.\n")
        return True
    except Exception as e:
        BuiltIn().log_to_console("failed!!! "+ e.__str__())
        return False

def visibility_of_element_located_by(locator):
    """An expectation for checking that an element is present on the DOM of a
    page and visible. Visibility means that the element is not only displayed
    but also has a height and width that is greater than 0.

    locator - used to find the element
    returns the WebElement once it is located and visible
    """

    def _predicate(driver):
        try:
            return EC._element_if_visible(find_element_with_locator(*locator))
        except StaleElementReferenceException:
            return False

    return _predicate

def wait_until_locator_is_present( locator: str, verbose:bool=True,  retries: int=Environment.retry_times ):
    if verbose:
        BuiltIn().log_to_console( "Wait until element is present."+str(locator), no_newline=True)
    try:
        for attempt in range(1, retries):
            if verbose:
                BuiltIn().log_to_console( ".", no_newline=True)
            element = find_element_with_locator( locator, False )
            if  element != None:
                if verbose:
                    BuiltIn().log_to_console("present!!! \n")
                return True
        if verbose:
            BuiltIn().log_to_console("failed element is not present!!!.... ")
        return False
    except Exception as e:
        if verbose:
            BuiltIn().log_to_console("failed element is not present!!! - Exception"+ e.__str__())
        return False
    
def page_should_contain( expected_text: str )-> bool:
    BuiltIn().log_to_console( "page_should_contain  " + expected_text)
    driver = open_or_get_browser()
    html = driver.page_source
    return html.__contains__(expected_text)

def element_is_present( locator: str, timeout_In_seconds:float=Environment.implicit_timeout_in_seconds, verbose: bool=True ):
    if verbose:
        BuiltIn().log_to_console( message="element_is_present ?  " + str(locator) + "...", no_newline=True)
    locator_tuple = (get_location_method(locator), get_location_expression(locator))
    element = None
    try:
        element = WebDriverWait(driver, timeout_In_seconds, ignored_exceptions=[StaleElementReferenceException]).until(EC.presence_of_element_located(locator_tuple))
    except:
        element = None
    if element != None:
        if verbose:
            BuiltIn().log_to_console("yes")
        return True
    else:
        if verbose:
            BuiltIn().log_to_console("no")
        return False        

def element_is_visible( locator: str, timeout_In_seconds:float=Environment.implicit_timeout_in_seconds, verbose: bool=True ):
    # TODO: Verify error on chromedriver 
    if verbose:
        BuiltIn().log_to_console( message="element is visible ?  " + str(locator) + "...", no_newline=True)
    locator_tuple = (get_location_method(locator), get_location_expression(locator))
    element = None
    try:
        element = WebDriverWait(driver, timeout_In_seconds, ignored_exceptions=[StaleElementReferenceException]).until(EC.visibility_of_element_located(locator_tuple))
    except:
        element = None
    if element != None:
        if verbose:
            BuiltIn().log_to_console("yes")
        return True
    else:
        if verbose:
            BuiltIn().log_to_console("no")
        return False        

def element_is_checked( locator: str, timeout_In_seconds:float=Environment.implicit_timeout_in_seconds ):
    BuiltIn().log_to_console( message="Radio is checked ?  " + str(locator) + "...", no_newline=True)
    locator_tuple = (get_location_method(locator), get_location_expression(locator))
    element:WebElement = None
    try:
        element = WebDriverWait(driver, timeout_In_seconds, ignored_exceptions=[StaleElementReferenceException]).until(EC.presence_of_element_located(locator_tuple))
    except:
        element = None
    if element != None:
        BuiltIn().log_to_console("yes")
    else:
        BuiltIn().log_to_console("no")
        return False       
    return element.is_selected 

def element_has_class(locator, classname):
    element: WebElement = find_element_with_locator(locator)
    if element == None: # attribute not found
        return False    
    classes:str = element.get_attribute("class")
    classes = classes.split(" ")
    for class_id in classes:
        if class_id == classname:
            return True
    return False
  
def element_in_array_is_present( locators_array:list[str], retries: int=Environment.retry_times):
    BuiltIn().log_to_console( "Element in array is present?  ", no_newline=True)
    try:
        driver: webdriver.Chrome = open_or_get_browser()
        driver.implicitly_wait( 1 )
        for attempt in range(retries):
            index = 0
            for locator in locators_array:
                if element_is_present( locator, 1, False ): 
                    driver.implicitly_wait( Environment.implicit_timeout_in_seconds )
                    BuiltIn().log_to_console( "Found="+locator )
                    return index
                BuiltIn().log_to_console( ".", no_newline=True)
                index = index + 1
        BuiltIn().log_to_console("failed elements are not found!!!.... ")
    except Exception as e:
        BuiltIn().log_to_console("failed elements are not found!!! - Exception:"+ e.__str__())
    driver.implicitly_wait( Environment.implicit_timeout_in_seconds )
    return -1

def element_in_array_is_visible( locators_array:list[str], retries: int=Environment.retry_times):
    BuiltIn().log_to_console( "Element in array is visible?  ", no_newline=True)
    try:
        driver: webdriver.Chrome = open_or_get_browser()
        driver.implicitly_wait( 1 )
        for attempt in range(retries):
            index = 0
            for locator in locators_array:
                if element_is_visible( locator, 1, False ): 
                    driver.implicitly_wait( Environment.implicit_timeout_in_seconds )
                    BuiltIn().log_to_console( "Found="+locator )
                    return index
                BuiltIn().log_to_console( ".", no_newline=True)
                index = index + 1
        BuiltIn().log_to_console("failed elements are not visible!!!.... ")
    except Exception as e:
        BuiltIn().log_to_console("failed elements are not visible!!! - Exception:"+ e.__str__())
    driver.implicitly_wait( Environment.implicit_timeout_in_seconds )
    return -1

def wait_until_location_does_not_contain( page_url: str ):
    BuiltIn().log_to_console( "wait_until_location_does_not_contain "+page_url)
    driver = open_or_get_browser()
    WebDriverWait(driver, Environment.explicit_timeout_in_seconds).until_not( EC.url_contains( page_url ))

def get_text( locator, retries: int=Environment.retry_times, not_empty: bool=False, raise_exception_on_failure: bool=True, verbose: bool=True ):
    try:
        if verbose:
            BuiltIn().log_to_console( "Get Text "+str(locator), no_newline=True)
        if wait_until_locator_is_present(locator, False) == False:
            BuiltIn().fail("ERROR: Element "+locator+" is not found on get_text().")
        text = None
        for attempt in range(1, retries): 
            try:
                element: WebElement = find_element_with_locator( locator, False )
                text = element.text
                if not_empty: # Needs an non empty result
                    if text != '':
                        if verbose:
                            BuiltIn().log_to_console( " Got Text ["+text+"]")
                        return text                        
                else:
                    if verbose:
                        BuiltIn().log_to_console( " Got Text ["+text+"]")
                    return text
            except:
                if verbose:
                    BuiltIn().log_to_console(".", no_newline=True)
                text = None
            time.sleep(1)
        BuiltIn().fail("ERROR: Element "+locator+" does not have text attribute.")
    except Exception as e:
        if verbose:
            BuiltIn().log_to_console("Text in element not found!!! - Exception:"+ str( e))
        if raise_exception_on_failure:
            raise Exception("ERROR: Element "+locator+" does not have text attribute.")

def get_text_from_mouse_hover_layer( locator, tooltip )->str:
    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)
    locator_tuple = (get_location_method( locator ), get_location_expression( locator ))

    desired_elem = wait.until(EC.visibility_of_element_located(locator_tuple))
    scroll_center_view_to_element(locator)
    actions.move_to_element(desired_elem).perform()
    tooltip_tuple = (get_location_method( tooltip ), get_location_expression( tooltip ))
    text = wait.until(EC.visibility_of_element_located(tooltip_tuple)).text
    return text

def get_attribute( locator, name, retries: int=Environment.retry_times, not_empty: bool=False, raise_exception_on_failure: bool=True, verbose: bool=True )->str:
    '''Get an atribute 'name' from locator element.   If property not found fail or return 'None'.'''
    try:
        BuiltIn().log_to_console( "Get Attribute "+name+" from "+str(locator))
        if wait_until_locator_is_present(locator) == False:
            raise Exception("ERROR: Element "+locator+" is not found on get_attribute().")
        value = None
        for attempt in range(1, retries): 
            try:
                element: WebElement = find_element_with_locator( locator, verbose=False )
                value = element.get_attribute( name )
                if value != None: # Property exists
                    if not_empty: # Needs an non empty result
                        if value != '':
                            if verbose:
                                BuiltIn().log_to_console( "Got Attribute "+name+" ["+value+"]")
                            return value                        
                    else:
                        if verbose:
                            BuiltIn().log_to_console( "Got Attribute "+name+" ["+value+"]")
                        return value
            except:
                BuiltIn().log_to_console(".")
                value = None
            time.sleep(1)
        if raise_exception_on_failure: # Didn't find after attempts
            BuiltIn().fail("ERROR: Element "+locator+" does not have "+name+" attribute.")
        return value
    except Exception as e:
        if verbose:
            BuiltIn().log_to_console(name+" attribute in element not found!!! - Exception:"+ str( e))
        if raise_exception_on_failure:
            raise Exception("ERROR:"+name+" attribute in element not found!!! - Exception:"+ str( e))
        
def wait_until_locator_text_changes( locator: str, retries: int=Environment.retry_times, verbose: bool=True ):
    try:
        if verbose:
            BuiltIn().log_to_console( "Wait until locator text changes in "+locator, no_newline=True)
        element: WebElement = find_element_with_locator( locator, verbose=False )
        current_text = element.text
        for retry in range(1, retries):
            element = find_element_with_locator( locator, verbose=False )
            if  element != None and element.text != current_text:
                if verbose:
                    BuiltIn().log_to_console("changed!!! \n")
                return True
            else:
                if verbose:
                    BuiltIn().log_to_console( ".", no_newline=True)
            time.sleep(1)
        if verbose:
            BuiltIn().log_to_console("ERROR: Text did not change!!!.... ")
        return False
    except Exception as e:
        BuiltIn().log_to_console("ERROR: Text did not change!!! - Exception:"+ str( e))
        raise Exception("ERROR: Element "+locator+" does not change text attribute in "+str(Environment.retry_times)+" retries.")

def wait_until_locator_does_not_have_attribute( locator: str, attribute_name: str, retries: int=Environment.retry_times, verbose: bool=True  ):
    '''Waits retrying until locator does not have attribute name assigned.'''
    if verbose:
        BuiltIn().log_to_console( "wait until locator:"+str(locator)+" does not have attribute:"+attribute_name)
    try:
        for attempt in range(1, retries):
            BuiltIn().log_to_console( "Retry nº:" + str(attempt))
            element: WebElement = find_element_with_locator(locator)
            if element == None:
                BuiltIn().fail("Cannot find element "+locator)
            if element.get_attribute( attribute_name ) == None: # attribute not found
                return True
        if verbose:
            BuiltIn().log_to_console(" attribute is present!!!.... ")
        return False
    except Exception as e:
        if verbose:
            BuiltIn().log_to_console(" failed attribute is present!!!....  - Exception"+ e.__str__())
        return False

def wait_until_locator_is_clickable( locator: str, timeout_In_seconds:float=Environment.implicit_timeout_in_seconds ):
    try:
        BuiltIn().log_to_console( message="Wait for locator clickable.. "+str(locator), no_newline=True)
        locator_tuple = (get_location_method( locator ), get_location_expression( locator ))
        WebDriverWait(driver, timeout_In_seconds).until(EC.element_to_be_clickable(locator_tuple))
        BuiltIn().log_to_console(" OK!!! ")
        return True
    except Exception as e:
        BuiltIn().log_to_console("failed!!! "+ e.__str__())
        return False

def wait_until_locator_is_visible( locator: str, timeout_In_seconds:float=Environment.implicit_timeout_in_seconds, verbose:bool = True ):
    try:
        if verbose:
            BuiltIn().log_to_console( message="Wait for locator visible.. "+str(locator), no_newline=True)
        locator_tuple = (get_location_method( locator ), get_location_expression( locator ))
        WebDriverWait(driver, timeout_In_seconds).until(EC.visibility_of_element_located(locator_tuple))
        if verbose:
            BuiltIn().log_to_console(" OK!!! ")
        return True
    except Exception as e:
        if verbose:
            BuiltIn().log_to_console(" failed!!! "+ e.__str__())
        return False

def wait_until_locator_is_not_visible( locator: str, timeout_In_seconds:float=Environment.implicit_timeout_in_seconds, verbose:bool = True ):
    try:
        if verbose:
            BuiltIn().log_to_console( message="Wait for locator not visible.. "+str(locator), no_newline=True)
        locator_tuple = (get_location_method( locator ), get_location_expression( locator ))
        WebDriverWait(driver, timeout_In_seconds).until(EC.invisibility_of_element_located(locator_tuple))
        if verbose:
            BuiltIn().log_to_console(" OK!!! ")
        return True
    except Exception as e:
        if verbose:
            BuiltIn().log_to_console(" failed!!! "+ e.__str__())
        return False
            
def select_option_from_combo_list_by_text(combo_locator, option_text, verbose=True):
    '''Selects an option from combo_locator using inner text.'''
    if verbose:
        BuiltIn().log_to_console("Select option from combo list:"+option_text)
    try:
        click_locator( combo_locator )
        combo:WebElement = find_element_with_locator(combo_locator)
        objSelect = Select(combo)
        objSelect.select_by_visible_text(option_text)
    except Exception as e:
        if verbose:
            BuiltIn().log_to_console("Option "+option_text+" is not selected")
        BuiltIn().fail("ERROR: Option ["+option_text+"] can't be selected from "+combo_locator+".  Exception:"+e.__str__())

def get_current_select_option_excluding( select_locator, excluded:str='', retries: int=Environment.retry_times ):
    '''Get the current select option but excluding a value.    Use when select last on rendering and need to exclude initial default value.'''
    try:
        BuiltIn().log_to_console("\nGet current option from select."+select_locator, no_newline=True)    
        combo:WebElement = find_element_with_locator(select_locator, False)
        scoring_select = Select(combo)
        iteration = 1
        selected_option = ''
        while (selected_option == '' or excluded in selected_option ) and iteration <= retries: # Waits until have a selected option
            BuiltIn().log_to_console(".", no_newline=True)  
            try:
                selected_option = (scoring_select.first_selected_option).text
            except:
                continue
            iteration = iteration+1
            time.sleep( 1 )
        if iteration > Environment.retry_times:
            BuiltIn().fail("Can not find selected option in Select object.  Retries:"+str(retries))
        BuiltIn().log_to_console("done")        
        return selected_option
    except Exception as e:
        BuiltIn().fail("Cannot find current selected option:"+e.__str__()) 
        
def get_first_unchecked_option_from_select( select_locator ):
    '''Get the first unchecked value from a select object, excluding default_value [0].'''
    try:
        options_locator = select_locator+"/option"
        option_list = find_elements_with_locator(options_locator)
        
        for i in range(1, len(option_list)-1): # review options
            option = option_list[i]
            BuiltIn().log_to_console(".", no_newline=True)  
            if not option.is_selected():
                BuiltIn().log_to_console("done")                    
                return option.text
        BuiltIn().fail("Can not find unselected option in Select object.")
    except Exception as e:
        BuiltIn().fail("Cannot find unselected option:"+e.__str__(), "FAIL")          