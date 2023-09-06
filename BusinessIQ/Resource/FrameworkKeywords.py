from CustomHTMLReportLibrary import *
from robot.libraries.BuiltIn import BuiltIn
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
import Environment

# This global variable controls webdriver session
driver: webdriver = None
global_suite_name = ""


def set_driver( driver_instance: webdriver ):
    global driver 
    driver = driver_instance
    
def get_driver():
    global driver
    return driver

def suite_setup(suite_name: str):
    if ( "." in suite_name ): # In the form of full name we have to remove path
        paths = suite_name.split(".")
        suite_name = paths[len(paths)-1]
    global global_suite_name
    global_suite_name = suite_name
    result_folder = os.path.join(os.getcwd(), 'Results')
    dt_tme = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    suite_result_folder = suite_name + "_" + dt_tme
    suite_result_folder = os.path.join(result_folder, suite_result_folder)
    suite_result = os.path.join(suite_result_folder, suite_name + ".html")
    if not os.path.exists(suite_result_folder):
        os.makedirs(suite_result_folder)

    details_folder = os.path.join(suite_result_folder, "Details")
    if not os.path.exists(details_folder):
        os.makedirs(details_folder)

    screenshot_path = os.path.join(suite_result_folder, "Screenshots")
    if not os.path.exists(screenshot_path):
        os.makedirs(screenshot_path)

    BuiltIn().set_global_variable("${resultFolder}", result_folder.replace("\\", "/"))
    BuiltIn().set_global_variable("${suite_result}", suite_result.replace("\\", "/"))
    BuiltIn().set_global_variable("${detailsFolderPath}", details_folder.replace("\\", "/"))
    BuiltIn().set_global_variable("${screenshotPath}", screenshot_path.replace("\\", "/"))
    generate_suite_report_header(suite_result, suite_name)


def test_setup(test_name):
    print ("${detailsFolderPath}")
    details_folder = BuiltIn().get_variable_value("${detailsFolderPath}")
    test_result = generate_test_report_header(details_folder, test_name)
    BuiltIn().set_global_variable("${testResultpath}", test_result.replace("\\", "/"))
    BuiltIn().set_test_variable("${testcase_status}", "PASS")
    global  global_suite_name
    excel_file = os.getcwd().replace("\\","/")+"/BusinessIQ/TestData/MasterTestData.xls"
    export_variables(excel_file, global_suite_name.split("-")[0], test_name)
    driver = open_or_get_browser()


def export_variables(excel_name, sheet_name, test_name):
    df = pd.read_excel(excel_name, sheet_name, dtype=str)
    test_data_set = df[df.TestName == test_name].replace(np.nan, '', regex=True)
    print( test_data_set )
    for k in test_data_set.items():
        BuiltIn().set_test_variable("${" + k[0] + "}", test_data_set[k[0]].values[0])


def end_test(test_name, test_description):
    test_result_path = BuiltIn().get_variable_value("${testResultpath}")
    suite_result = BuiltIn().get_variable_value("${suite_result}")
    testcase_status = BuiltIn().get_variable_value("${testcase_status}")
    log_execution_endtime_to_report_file(test_result_path)
    write_result_to_SuiteReport(suite_result, test_result_path, test_name, test_description, testcase_status)
    global driver
    driver = open_or_get_browser()
    if ( not Environment.local_browser ):
        if testcase_status == 'FAIL':
            driver.execute_script('lambda-status=failed')
        else:
            driver.execute_script('lambda-status=passed')
    driver.quit()
    driver = None
    BuiltIn().set_global_variable("${driver}", None)
    # Disconnect From Database


def open_or_get_browser():
    username = Environment.userName
    access_key = Environment.accessKey
    desired_caps = {
        "build": Environment.runName,  # Change your build name here
        "name": BuiltIn().get_variable_value("${TEST_NAME}"),  # Change your test name here
        "browserName": Environment.browserName,
        "version": Environment.browserVersion,
        "platform": Environment.os,
        "resolution": Environment.resolution,
        "selenium_version": Environment.seleniumVersion,
        "console": 'true',  # Enable or disable console logs
        "network": 'true'  # Enable or disable network logs
    }
    try:
#        driver = BuiltIn().get_variable_value("${driver}")
        driver = get_driver()
        if driver is None:
            BuiltIn().log_to_console("\nCREATING WEBDRIVER SESSION")
            if Environment.local_browser == True:
                driver = webdriver.Chrome()
            else:
                driver = webdriver.Remote(
                command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key),
                desired_capabilities=desired_caps)
            #BuiltIn().set_global_variable("${driver}", driver)
            set_driver( driver )
        driver.implicitly_wait( 10 )
    except Exception as ex:
        BuiltIn().fail("Failed open_or_get_browser:"+str(ex))
        
    return driver


def close_browser():
    global driver
    driver = get_driver()
    driver.quit()
    driver = None


def get_current_timestamp():
    dt_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    return dt_time


def report(step_description, expected_result, actual_result, status):
    screenshot_path = BuiltIn().get_variable_value("${screenshotPath}")
    test_result_path = BuiltIn().get_variable_value("${testResultpath}")

    driver = open_or_get_browser()
    tm = get_current_timestamp()
    screenshot_name = 'Screen_'+tm+'.png'
    screenshot = os.path.join(screenshot_path, screenshot_name)
    try:
        driver.save_screenshot(screenshot)
    except Exception as e:
        BuiltIn().log("********************************")
        BuiltIn().log(e.message)

    write_result_to_TestReport(test_result_path, screenshot_name, step_description, expected_result, actual_result,
                               status)

def browser_back():
    BuiltIn().log_to_console( "browser_back")
    driver = open_or_get_browser()
    driver.back()

def switch_to_window_by_handle( handle ):
    BuiltIn().log_to_console( "switch_to_window_by_handle "+handle)
    driver = open_or_get_browser()
    driver.switch_to.window(handle)
    
def click_js(element):
    BuiltIn().log_to_console( "click_js "+ str(element))
    try:
        driver = open_or_get_browser()        
        driver.execute_script("arguments[0].click();", element)
        BuiltIn().log_to_console("done.\n")
    except Exception as e:
        BuiltIn().log_to_console("failed!!! "+ e.args[0])

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

def find_element_with_locator( locator ):
    BuiltIn().log_to_console("find_element_with_locator "+locator )
    try:
        location_method = get_location_method( locator )
        location_expression = get_location_expression( locator )
        driver = open_or_get_browser()
        if location_method == 'id':
            return driver.find_element( By.ID, location_expression)
        elif location_method == 'name':
            return driver.find_element( By.NAME, location_expression)
        elif location_method == 'xpath':
            return driver.find_element( By.XPATH, location_expression)
        elif location_method == 'link_text':
            return driver.find_element( By.LINK_TEXT, location_expression)  
        elif location_method == 'partial_link_text':
            return driver.find_element( By.PARTIAL_LINK_TEXT, location_expression)  
        elif location_method == 'tag_name':
            return driver.find_element( By.TAG_NAME, location_expression)  
        elif location_method == 'partial_link_text':
            return driver.find_element( By.CLASS_NAME, location_expression)  
        elif location_method == 'css_selector':
            return driver.find_element( By.CSS_SELECTOR, location_expression)  
        elif location_method == 'css_class_name':
            return driver.find_element( By.CLASS_NAME, location_expression)  
    except Exception as e:
        BuiltIn().log_to_console("failed!!! "+ e.args[0])
        return None

def find_elements_with_locator( locator ):
    BuiltIn().log_to_console("find_elements_with_locator "+locator )
    try:
        location_method = get_location_method( locator )
        location_expression = get_location_expression( locator )
        driver = open_or_get_browser()
        if location_method == 'id':
            return driver.find_elements( By.ID, location_expression)
        elif location_method == 'name':
            return driver.find_elements( By.NAME, location_expression)
        elif location_method == 'xpath':
            return driver.find_elements( By.XPATH, location_expression)
        elif location_method == 'link_text':
            return driver.find_elements( By.LINK_TEXT, location_expression)  
        elif location_method == 'partial_link_text':
            return driver.find_elements( By.PARTIAL_LINK_TEXT, location_expression)  
        elif location_method == 'tag_name':
            return driver.find_elements( By.TAG_NAME, location_expression)  
        elif location_method == 'partial_link_text':
            return driver.find_elements( By.CLASS_NAME, location_expression)  
        elif location_method == 'css_selector':
            return driver.find_elements( By.CSS_SELECTOR, location_expression)  
        elif location_method == 'css_class_name':
            return driver.find_elements( By.CLASS_NAME, location_expression)  
    except Exception as e:
        BuiltIn().log_to_console("failed!!! "+ e.args[0])
        return None
        
def click_locator( locator ):
    BuiltIn().log_to_console( "Click on "+str(locator))
    driver = open_or_get_browser()
    element = find_element_with_locator( locator )
    WebDriverWait(driver, Environment.explicit_timeout_in_seconds).until(EC.element_to_be_clickable(element))
    element.click()

def click_web_element( element: WebElement ):
    BuiltIn().log_to_console( "Click on web element"+str(element))
    driver = open_or_get_browser()
    WebDriverWait(driver, Environment.explicit_timeout_in_seconds).until(EC.element_to_be_clickable(element))
    element.click()
    
def send_keys( locator, text_value: str ):
    BuiltIn().log_to_console( "Set Text Field on "+str(locator))
    driver = open_or_get_browser()
    input_element = find_element_with_locator( locator )
    WebDriverWait(driver, Environment.explicit_timeout_in_seconds).until(EC.visibility_of(input_element))
    input_element.send_keys( text_value )
    
def location_should_contain( url:str ):
    BuiltIn().log_to_console( "Current location should contain "+url)
    driver = open_or_get_browser()
    try:
        WebDriverWait(driver, Environment.explicit_timeout_in_seconds).until(EC.url_contains( url ))
        BuiltIn().log_to_console("done.\n")
        return True
    except Exception as e:
        BuiltIn().log_to_console("failed!!! "+ e.args[0])
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

def wait_until_locator_is_visible( locator: str ):
    BuiltIn().log_to_console( "wait_until_element_is_visible "+str(locator))
    driver = open_or_get_browser()
    try:
        for seconds in range(1, 30):
            element = find_element_with_locator( locator )
            if  element != None:
                if element.is_displayed():
                    BuiltIn().log_to_console("visible!!! \n")
                    return True
            WebDriverWait(driver, 1)
        BuiltIn().log_to_console("failed element is not visible!!!.... ")
        return False

    except Exception as e:
        BuiltIn().log_to_console("failed element is not visible!!! - Exception"+ e.args[0])
        return False
    
def page_should_contain( expected_error_message: str )-> bool:
    BuiltIn().log_to_console( "page_should_contain  " + expected_error_message)
    driver = open_or_get_browser()
    html = driver.page_source
    return html.__contains__(expected_error_message)

def element_is_present( locator: str ):
    web_elements_list = find_elements_with_locator( locator )
    BuiltIn().log_to_console( "element_is_present ?  " + str(locator) + " " + str(( web_elements_list != [] )))
    return ( web_elements_list != [] )
  
def element_in_array_is_present( locators_array:list[str]):
    BuiltIn().log_to_console( "element_in_array_is_present?  ")
    try:
        for seconds in range(40):
            index = 0
            for locator in locators_array:
                if  element_is_present(locator):
                    BuiltIn().log_to_console("visible!!! \n")
                    return index
                index = index + 1

            WebDriverWait(driver, 1)
        BuiltIn().log_to_console("failed elements are not found!!!.... ")
    except Exception as e:
        BuiltIn().log_to_console("failed elements are not found!!! - Exception:"+ e.args[0])
        return False
    return -1

def wait_until_location_does_not_contain( page_url: str ):
    BuiltIn().log_to_console( "wait_until_location_does_not_contain "+page_url)
    driver = open_or_get_browser()
    WebDriverWait(driver, Environment.explicit_timeout_in_seconds).until_not( EC.url_contains( page_url ))

def get_text( locator ):
    BuiltIn().log_to_console( "Get Text "+str(locator))
    element = find_element_with_locator( locator )
    return element.text

