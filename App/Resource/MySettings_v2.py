from FrameworkKeywords import open_or_get_browser, report, click_js, wait_until_locator_is_present, send_keys, click_locator, element_is_checked, get_text, find_element_with_locator
import time
from selenium.webdriver.remote.webelement import WebElement 
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import Environment


def goto_my_settings():
    BuiltIn().log_to_console("\nGOTO MY SETTINGS" )
    driver = open_or_get_browser()
    wait = WebDriverWait(driver, 10)
    try:
        driver.find_element(By.XPATH, "//button[@id='user-menu-btn']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[text()=' My Settings ']").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Settings']")))
        if len(driver.find_elements(By.XPATH, "//h2[text()='Settings']")) > 0:
            time.sleep(3)
            report("Open V2 my settings page", "My settings page should be opened", "My settings page opened", "PASS")
        else:
            report("Open V2 my settings page", "My settings page should be opened", "My settings page did not open",
                   "FAIL")
    except Exception as e:
        report("Open my settings page", "My settings page should be opened", "My settings page not opened:"+e.__str__(), "FAIL")


def validate_subscriber(subscriber):
    try:
        driver = open_or_get_browser()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH,  "//span[contains(text(), 'Subscriber:')]")))
        time.sleep(5)
        subscriber_button = "xpath=//span[contains(text(), 'Subscriber:')]"
        subcodetext = get_text( subscriber_button, not_empty=True )
        if str(subscriber) in subcodetext:
            report("Check default subscriber", "Subscriber " + subscriber + " should be default",
                   "Subscriber " + str(subscriber) + " is default",
                   "PASS")
        else:
            report("Check default subscriber", "Subscriber " + subscriber + " should be default",
                   "Subscriber " + str(subscriber) + " is not set default but "+subcodetext,
                   "FAIL")
    except Exception as e:
        report("Check default subscriber", "Subscriber " + subscriber + " should be default",
               "Subscriber " + str(subscriber) + " is not set default",
               "FAIL")

def is_checkbox_selected( checkbox_locator:str ):
    try:
        checkbox: WebElement = find_element_with_locator( checkbox_locator )
        attribute = checkbox.get_attribute("aria-checked")
        return attribute == 'true'
    except Exception as e:
        report("is_checkbox_selected", "Can read attribute","Can not read.", "FAIL")        


def set_my_settings(subscriber, scoring_model, portfolio, BIQV2Default):
    try:
        BuiltIn().log_to_console("\nSET MY SETTINGS  subscriber="+subscriber+" scoring="+scoring_model+" portfolio="+portfolio+" V2 Default="+BIQV2Default)
        driver = open_or_get_browser()

        goto_my_settings()
        # Set subcode
        subcode_input = "xpath=//span[text()='Select Subcode']/../../../input"
        subcode_option = "xpath=//span[@class = 'mat-option-text' and contains(text(), '" + str(subscriber) + "')]"
        wait_until_locator_is_present( subcode_input )
        send_keys( subcode_input, subscriber)
        wait_until_locator_is_present( subcode_option )
        click_locator( subcode_option )
        
        checkbox1 = "xpath=//input[@id='mat-checkbox-1-input']"
        if not is_checkbox_selected(checkbox1):
            click_locator( checkbox1 )
            
        # Set Scoring model
        score_model_combo = driver.find_element(By.XPATH, "//mat-select[@placeholder='Scoring Model Default']/div/div/span")
        score_option = "xpath=//span[@class='mat-option-text' and contains(text(),' " + scoring_model + " ')]"
        wait_until_locator_is_present( "xpath=//mat-select[@placeholder='Scoring Model Default']/div/div/span" )
        click_js( score_model_combo )
        wait_until_locator_is_present( score_option )
        score_model_option = find_element_with_locator( score_option )
        click_js( score_model_option )
        
        # Set Portfolio
        all_portfolios_msg = "xpath=//div[contains(text(),'All Portfolios Available')]"
        select_portfolio_input = "xpath=//input[@data-placeholder='Select Portfolio']"
        select_portfolio_option = "xpath=//span[@class= 'mat-option-text' and contains(text(), '" + portfolio + "')]"
        
        if element_is_checked( all_portfolios_msg ) == False:
            send_keys(select_portfolio_input, portfolio)
            wait_until_locator_is_present( select_portfolio_option )
            portfolio_option = driver.find_element(By.XPATH, "//span[@class= 'mat-option-text' and contains(text(), '" + portfolio + "')]")
            click_js( portfolio_option )
          
        biq_check_locator = "xpath=//input[@id='mat-checkbox-2-input']"
        if str(BIQV2Default) == "N":
            if is_checkbox_selected(biq_check_locator):
                click_js( find_element_with_locator( biq_check_locator) )
        elif str(BIQV2Default) == "Y":
            if not is_checkbox_selected( biq_check_locator ):
                click_js( find_element_with_locator( biq_check_locator ) )
        report("Set My Settings in V2", "Details should be filled", "Details are filled properly", "PASS")
        
        #  Save and verify
        saveButton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Save']")))
        click_js(saveButton)
        subscriberButton = WebDriverWait(driver, Environment.wait_time_my_settings_v2).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Subscriber:')]")))
        subcodetext = subscriberButton.text
        if str(subscriber) in subcodetext:
            report("Save My Settings in V2", "My Settings should be saved", "My Settings set successfully", "PASS")
        else:
            report("Set My Settings in V2", "My Settings should be set", "My Settings not set successfully", "FAIL")
            
    except Exception as e:
        report("Set My Settings in V2", "My Settings should be set", "My Settings not set successfully " + e.__str__(),
               "FAIL")


def validate_default_scoring_model(scoring_model):
    try:
        driver = open_or_get_browser()
        wait = WebDriverWait(driver, 10)
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//mat-select[contains(@class,'report__select-dropdown')]")))
        scoring_model_text = driver.find_element(By.XPATH, 
            "//mat-select[@id = 'scoring-model-select']/div/div/span/span").text
        if str(scoring_model) in scoring_model_text:
            report("Validate Default Scoring Model", "Default scoring model should be set",
                   "Default Scoring Model set successfully", "PASS")
        else:
            report("Validate Default Scoring Model", "Default scoring model should be set",
                   "Default Scoring Model not set successfully", "FAIL")
    except Exception as e:
        report("Validate Default Scoring Model", "Default scoring model should be set",
               "Default Scoring Model not set successfully" + e.__str__(), "FAIL")


def validate_default_portfolio(portfolio):
    try:
        driver = open_or_get_browser()
        wait = WebDriverWait(driver, 10)
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Portfolio Selected')]")))
        time.sleep(2)
        portfolio_text = driver.find_element(By.XPATH, "//div[contains(text(),'Portfolio Selected')]/..//h1").text
        print( str(portfolio_text) )
        if str(portfolio) in portfolio_text:
            report("Validate Default Portfolio", "Default Portfolio should be set",
                   "Default Portfolio set successfully", "PASS")
        else:
            report("Validate Default Portfolio", "Default Portfolio should be set",
                   "Default Portfolio not set successfully", "FAIL")
    except Exception as e:
        report("Validate Default Portfolio", "Default Portfolio should be set",
               "Default Portfolio not set successfully" + e.__str__(), "FAIL")


# def validate_back_to_v1():
#     try:
#         driver = open_or_get_browser()
#         wait = WebDriverWait(driver, 10)
#         wait.until(
#             EC.visibility_of_element_located((By.XPATH, "//div[@ng-reflect-trigger='https://stg1-ss1.experian.com/']//..")))
#         driver.find_element(By.XPATH, "//div[@ng-reflect-trigger='https://stg1-ss1.experian.com/']//..").click()
#         if driver.find_element(By.XPATH, "//div[@id='body_group']/div[1]/h1").is_displayed():
#             report("Go back to BIQ V1 ", "User Should be able to view BIQ V1 Dashboard",
#                    "Dashboard is visible", "PASS")
#         else:
#             report("Go back to BIQ V1 ", "User Should be able to view BIQ V1 Dashboard",
#                    "Dashboard is not visible", "FAIL")
#     except Exception as e:
#         
#         
#         report("Go back to BIQ V1 ", "User Should be able to view BIQ V1 Dashboard",
#                    "Dashboard is not visible"+e.__str__(), "FAIL")

# def validate_login_interface(username,BIQV2Default):
#     try:
#         driver = open_or_get_browser()
#         driver.get(get_biq_url())
#         time.sleep(2)
#         driver.find_element(By.ID, "user").send_keys(username)
#         password = UserDetails.userDetails[username]
#         time.sleep(1)
#         driver.find_element(By.ID, "password").send_keys(password)
#         driver.find_element(By.XPATH, "//button[contains(text(), 'Log In')]").click()
#         time.sleep(2)
#         if BIQV2Default == 'N':
#             if len(driver.find_elements(By.XPATH, "//div[@id='body_group']/div[1]/h1")) > 0:
#                 report("Validate user landed in V1 by default ", "User Should be able to view V1 Dashboard",
#                        "User logged in and V1 Dashboard is visible", "PASS")
#             else:
#                 report("Validate user landed in V1 by default ", "User Should be able to view V1 Dashboard",
#                        "User logged in and V1 Dashboard is not visible", "FAIL")
#             CommonBIQKeywords.logout_from_biq()
#         elif BIQV2Default == 'Y':
#             if len(driver.find_elements(By.XPATH, "//div[@ng-reflect-trigger='https://stg1-ss1.experian.com/']//..")) > 0:
#                 report("Validate user landed in V2 by default ", "User Should be able to view V2 Dashboard",
#                        "User logged in and V2 Dashboard is visible", "PASS")
#             else:
#                 report("Validate user landed in V2 by default ", "User Should be able to view V2 Dashboard",
#                        "User logged in and V2 Dashboard is not visible", "FAIL")
#             CommonBIQKeywords.logout_from_biq2()
#     except Exception as e:
#         
#         
#         report("Validate user landed in BIQ"+DefaultInterface+" by default ", "User Should be able to view BIQ"+DefaultInterface+" Dashboard",
#                "User logged in and V"+DefaultInterface+"Dashboard is not visible"+e.__str__(), "FAIL")
