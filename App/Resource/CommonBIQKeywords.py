from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.keys import Keys
from FrameworkKeywords import open_or_get_browser, report, click_element_and_wait_next_element_with_retry, get_biq_url, click_locator, get_text, wait_until_locator_text_changes, find_element_with_locator, get_text, wait_until_locator_is_visible, send_keys, wait_until_locator_is_not_visible, element_is_visible, click_js, element_is_present, get_attribute
import time
import Environment
import Login
change_subscriber_link = "xpath=//a[@id='change_subscriber']"
save_changes_button =  "xpath=//button[@id='saveChangeSubcriber']/span[text()='Save Changes']"
subcode_status = "xpath=//li[contains(text(), 'Subcode : ')]"

def change_subscriber(subcode:str):
    try:
        BuiltIn().log_to_console("\nCHANGE SUBSCRIBER:"+subcode)
        # Waits till Dashboard/header is enough rendered 
        wait_until_locator_is_visible( subcode_status, 2*Environment.retry_times )
        wait_until_locator_is_visible( change_subscriber_link )
        time.sleep(5)
        # Review if current setting is already subcode
        subcodetext = get_text(subcode_status, 2*Environment.retry_times, raise_exception_on_failure=False)
        if str(subcode) in subcodetext: # if subcode is already set return, there is nothing to do. 
            report("Change subscriber", "Subscriber should be changed", "Subscriber " + subcode + " is selected",
                   "PASS")
            return
        # Interaction with popup and select option
        click_element_and_wait_next_element_with_retry(change_subscriber_link, save_changes_button, 2*Environment.retry_times)
        if wait_until_locator_is_visible(save_changes_button):
            subcode_option = "xpath=//input[@name='subcode' and @value='" + subcode + "']"
            if wait_until_locator_is_visible( subcode_option ):
                if click_locator(subcode_option) == False:
                    report("Change subscriber", "Subscriber should be changed", "Subscriber "+ str(subcode) +" can not click option on combo list.", "FAIL")
            else:
                report("Change subscriber", "Subscriber should be changed", "Subscriber "+ str(subcode) +" is not found on combo list.", "FAIL")

            BuiltIn().log_to_console("********  subcode " + subcode + " selected *************")
            subcode_checkbox = "xpath=//input[@id='selectSubcodeCheckbox']"
            click_locator(subcode_checkbox)
            click_locator(save_changes_button)
        else:
            report("Change subscriber", "Subscriber should be changed", "Subscriber change window is not found.", "FAIL")
        # Verify subcode is changed
        validate_subcode_has_changed(subcode)

    except Exception as e:
        err_msg = "xpath=//div[@id='changeSubscriberPanel']/div/span/br"
        if find_element_with_locator(err_msg):
            report("Change Subscriber", "Subscriber should be changed", "Subscriber "+subcode+" is not changed. "+ get_text(err_msg), "FAIL")
        else:
            report("Change Subscriber", "Subscriber should be changed", "Subscriber "+str( subcode )+" is not changed. "+ e.__str__(), "FAIL")

def validate_subcode_has_changed(subcode):
    BuiltIn().log_to_console("\nVALIDATE SUBCODE HAS CHANGED TO:"+subcode)
    subcodetext = get_text(subcode_status, not_empty=True)
    if subcode in subcodetext: # subcode is already changed?
        report("Change subscriber", "Subscriber should be changed", "Subscriber " + subcode + " is selected", "PASS")
    else:
        if wait_until_locator_text_changes(subcode_status, 5*Environment.retry_times): # Wait change
            subcodetext = get_text(subcode_status, not_empty=True)
            if subcode in subcodetext: # subcode is changed?
                report("Change subscriber", "Subscriber should be changed", "Subscriber " + subcode + " is selected", "PASS")
            else:
                report("Change subscriber", "Subscriber should be changed", "Subscriber "+ subcode +" update failed", "FAIL")                
        else:
            report("Change subscriber", "Subscriber should be changed", "Subscriber "+ subcode +" update failed", "FAIL")

############################################
# V2 header locators
subscriber_button = "xpath=//span[contains(text(),'Subscriber:')]"
subscriber_input = "xpath=//input[@aria-label='Subcode']"
select_subscriber_as_default_checkbox = "xpath=//mat-checkbox"
selector_options = "xpath=//mat-option"
save_button_locator = "xpath=//button/span[contains(text(),'Save')]"
error_after_save_msg = "xpath=//mat-error"
change_subscriber_window_title = "xpath=//h3[contains(@class,'mat-dialog-title')]"
def default_checkbox_is_checked():
    click_locator(change_subscriber_window_title) # Change focus to popup window
    is_checked_locator = "xpath=//*[@type='checkbox' and @aria-checked='true']"
    checkbox_input = "xpath=//*[@id='mat-checkbox-1-input']"
    checked_attribute = get_attribute(checkbox_input, "aria-checked")
    return checked_attribute == "true"
def set_current_subscriber_as_default():
    if default_checkbox_is_checked() == False:
        if click_locator(select_subscriber_as_default_checkbox):
            report("Change subscriber", "Subscriber can be selected as default.","Subscriber selected as default.", "PASS")  
        else:
            report("Change subscriber", "Subscriber can be selected as default.","Subscriber cannot selected as default.", "FAIL")  
def get_current_subscriber()->str:

    subscriber:str = get_text(subscriber_button, not_empty=True)
    if subscriber == 'Subscriber:':
        wait_until_locator_text_changes(subscriber_button, verbose=False)
        subscriber:str = get_text(subscriber_button, not_empty=True)
    subscriber = subscriber.replace("Subscriber:","")
    subscriber = subscriber.lstrip().rstrip()
    BuiltIn().log_to_console("\nGet current subscriber V2:"+subscriber)
    return subscriber
def change_subscriber_v2(subscriber:str, select_first_available: bool = False, select_subscriber_as_default: bool = False):
    try:
        BuiltIn().log_to_console("\nCHANGE SUBSCRIBER V2:"+subscriber)
        wait_until_locator_is_visible(subscriber_button)
        subcodetext = get_text(subscriber_button, not_empty=True)
        if str(subscriber) in subcodetext and select_first_available==False:
            report("Change subscriber", "Subscriber should be changed",
                   "Subscriber " + str(subscriber) + " is already selected",
                   "PASS")
            return
        click_element_and_wait_next_element_with_retry(subscriber_button, subscriber_input)
        if select_first_available: # Use first available.
            click_element_and_wait_next_element_with_retry(subscriber_input,selector_options)
            option = find_element_with_locator(selector_options)
            if wait_until_locator_is_visible(selector_options):
                if click_js(option)== False: # Click on the first available
                    BuiltIn().fail("ERROR: Cannot click default option ")
            subcodetext = get_text(subscriber_button, not_empty=True)
            if select_subscriber_as_default: # Click checkbox
                set_current_subscriber_as_default()
            click_locator( save_button_locator)   
            wait_until_locator_is_visible(subscriber_button,1)
            report("Change subscriber", "Subscriber should be changed","Subscriber " + str(subcodetext) + " is selected","PASS")           
        else: # Use subscriber value to find option
            subscriber_option = "xpath=//span[contains(text(),'"+subscriber+"')]"
            send_keys(subscriber_input, subscriber, clear_input=True)
            time.sleep(1)
            if wait_until_locator_is_visible(subscriber_option):
                if click_locator(subscriber_option)== False:
                    BuiltIn().fail("ERROR: Cannot click option "+subscriber_option)
            else:
                BuiltIn().fail("ERROR: Cannot find subscriber:"+subscriber) 
            if select_subscriber_as_default: # Click checkbox
                set_current_subscriber_as_default()          
            click_locator( save_button_locator)
            if element_is_visible( error_after_save_msg,timeout_In_seconds=3 ):
                BuiltIn().fail("ERROR:"+get_text(error_after_save_msg, not_empty=True))
            wait_until_locator_is_visible(subscriber_button,1)
            subcodetext = get_text(subscriber_button, not_empty=True)
            if str(subscriber) in subcodetext:
                report("Change subscriber", "Subscriber should be changed","Subscriber " + str(subscriber) + " is selected","PASS")
            else:
                report("Change subscriber", "Subscriber should be changed to subscriber", "Subscriber update failed.  "+subcodetext, "FAIL")
                

    except Exception as e:
        report("Change subscriber", "Subscriber should be changed to "+subscriber, "Exception="+e.__str__(), "FAIL")

def logout_from_biq2():
    try:
        Login.logout_from_biq_v2()
        report("Logout from BIQ V2", "User should be logged out", "User logged out from BIQ", "PASS")
    except Exception as e:
        report("Logout from BIQ V2", "User should be logged out", "User not logged out from BIQ", "FAIL")

def open_biq_dashboard():
    driver = open_or_get_browser()
    try:
        driver.get( get_biq_url()+"dashboard/home.action?fromTopNav=Y")
        if len(driver.find_elements(By.XPATH, 
                "//div[@class='title_bar']/h1[contains(text(),'Welcome to BusinessIQ!')]")) > 0:
            report("Open BIQ dashboard","BIQ dashboard should be visible","BIQ dashboard is visible","PASS")
        else:
            report("Open BIQ dashboard", "BIQ dashboard should be visible", "BIQ dashboard is not visible", "FAIL")
    except Exception as e:
        report("Open BIQ dashboard", "BIQ dashboard should be visible", "BIQ dashboard is not visible"+e.__str__(), "FAIL")

def go_to_biq2_dashboard():
    try:
        driver = open_or_get_browser()
        time.sleep(3)
        driver.find_element(By.XPATH, "//mat-icon[contains(text(),'dashboard')]/..").click()
        time.sleep(3)
        report("open biq2 dashboard", "biq2 dashboard should be seen",
               "biq2 dashboard visible", "PASS")
    except Exception as e:
        report("open biq2 dashboard", "biq2 dashboard should be seen",
               "biq2 dashboard not visible" + e.__str__(), "FAIL")

def validate_pagination_for_grid_biqv2(title):
    try:
        driver = open_or_get_browser()
        wait = WebDriverWait(driver, 40)
#        wait.until(EC.visibility_of_element_located(By.XPATH,  "//mat-card-title[contains(text(),'')]/../../..//tbody/tr[1]"))
        items = driver.find_element(By.XPATH, "//mat-card-title[contains(text(),'')]/../../..//div[@class='mat-paginator-range-label']").text
        if "1" in items and "10" in items:
            report("validate numbering before moving to next page","numbering should show 1-10","numbering is showing as expected","PASS")
        else:
            report("validate numbering before moving to next page", "numbering should show 1-10",
                   "numbering is not showing as expected", "FAIL")
            
        driver.find_element(By.XPATH, "//mat-card-title[contains(text(),'"+str(title)+"')]/../../..//button[@class='mat-focus-indicator mat-tooltip-trigger mat-paginator-navigation-next mat-icon-button mat-button-base']").click()
        time.sleep(5)
#        wait.until(EC.visibility_of_element_located(By.XPATH,  "//mat-card-title[contains(text(),'"+str(title)+"')]/../../..//tbody/tr[1]"))
        items_after_click = driver.find_element(By.XPATH, "//mat-card-title[contains(text(),'"+str(title)+"')]/../../..//div[@class='mat-paginator-range-label']").text
        if "11" in items_after_click and "20" in items_after_click:
            report("validate numbering after moving to next page","numbering should show 11-20","numbering is showing as expected","PASS")
        else:
            report("validate numbering before moving to next page", "numbering should show 11-20",
                   "numbering is not showing as expected", "FAIL")
            
        number_of_items_before_click=len(driver.find_elements(By.XPATH, "//mat-card-title[contains(text(),'"+str(title)+"')]/../../..//tbody/tr"))
        if str(number_of_items_before_click) == "10":
            report("validate number of items in table before click","number of items before click should be 10",
                   "number of items showing as expected","PASS")
        else:
            report("validate number of items in table before click", "number of items before click should be 10",
                   "number of items not showing as expected", "FAIL")
            
        driver.find_element(By.XPATH, "//mat-card-title[contains(text(),'"+str(title)+"')]/../../..//div[@class='mat-paginator-container']/div/mat-form-field/div/div/div/mat-select/div").click()
        driver.find_element(By.XPATH, "//mat-option/span[contains(text(),'25')]").click()
        time.sleep(5)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//mat-card-title[contains(text(),'" + str(title) + "')]/../../..//tbody/tr[1]")))
        number_of_items_after_click=len(driver.find_elements(By.XPATH, "//mat-card-title[contains(text(),'"+str(title)+"')]/../../..//tbody/tr"))
        if str(number_of_items_after_click) == "25":
            report("validate number of items in table before click","number of items before click should be 25",
                   "number of items showing as expected","PASS")
        else:
            report("validate number of items in table before click", "number of items before click should be 25",
                   "number of items not showing as expected", "FAIL")
    except Exception as e:
        report("validate pagination for given list grid","proper pagination should be seen",
               "pagination not functioning as expected"+e.__str__(),"FAIL")