from FrameworkKeywords import open_or_get_browser, report
import time
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import Environment


def goto_my_settings():
    driver = open_or_get_browser()
    wait = WebDriverWait(driver, 10)
    try:
        driver.find_element(By.XPATH, "//button[@id='user-menu-btn']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[text()=' My Settings ']").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Settings']")))
        if len(driver.find_elements(By.XPATH, "//h2[text()='Settings']")) > 0:
            time.sleep(3)
            report("Open V2 my settings page", "My settings page should be opened", "My settings page opened", "PASSED")
        else:
            report("Open V2 my settings page", "My settings page should be opened", "My settings page did not open",
                   "FAILED")
            BuiltIn().set_test_variable("${testcase_status}", "FAIL")

    except Exception as e:
        BuiltIn().log(e.message)
        BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        report("Open my settings page", "My settings page should be opened", "My settings page not opened", "FAILED")


def validate_subscriber(subscriber):
    try:
        driver = open_or_get_browser()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(By.XPATH,  "//span[contains(text(), 'Subscriber:')]"))
        time.sleep(5)
        subcodetext = driver.find_element(By.XPATH, "//span[contains(text(), 'Subscriber:')]").text
        print (subcodetext)
        if str(subscriber) in subcodetext:
            report("Check default subscriber", "Subscriber " + subscriber + " should be default",
                   "Subscriber " + str(subscriber) + " is default",
                   "PASS")
        else:
            report("Check default subscriber", "Subscriber " + subscriber + " should be default",
                   "Subscriber " + str(subscriber) + " is not set default",
                   "FAILED")
            BuiltIn().set_test_variable("${testcase_status}", "FAIL")
    except Exception as e:
        BuiltIn().log(e.message)
        BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        report("Check default subscriber", "Subscriber " + subscriber + " should be default",
               "Subscriber " + str(subscriber) + " is not set default",
               "FAILED")


def set_my_settings(subscriber, scoring_model, portfolio, BIQV2Default):
    driver = open_or_get_browser()
    wait = WebDriverWait(driver, 15)
    goto_my_settings()
    try:
        time.sleep(Environment.wait_time_my_settings_v2)
        driver.find_element(By.XPATH, "//span[text()='Select Subcode']/../../../input").clear()
        driver.find_element(By.XPATH, "//span[text()='Select Subcode']/../../../input").send_keys(str(subscriber))
        driver.find_element(By.XPATH, 
            "//span[@class = 'mat-option-text' and contains(text(), '" + str(subscriber) + "')]").click()
        BuiltIn().log("testttttt------------")
        if len(driver.find_elements(By.XPATH, "//input[@id='mat-checkbox-1-input' and @aria-checked='false']")) > 0:
            driver.find_element(By.XPATH, "//input[@id='mat-checkbox-1-input' and @aria-checked='false']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, 
            "//mat-select[@placeholder='Scoring Model Default']/div/div/span").click()
        time.sleep(2)
        driver.find_element(By.XPATH, 
            "//span[@class='mat-option-text' and contains(text(),' " + scoring_model + " ')]").click()
        time.sleep(2)
        if len(driver.find_elements(By.XPATH, "//div[contains(text(),'All Portfolios Available')]"))>0:
            pass
        else:
            driver.find_element(By.XPATH, "//input[@data-placeholder='Select Portfolio']").clear()
            driver.find_element(By.XPATH, "//input[@data-placeholder='Select Portfolio']").send_keys(portfolio)
            time.sleep(1)
            driver.find_element(By.XPATH, 
                "//span[@class= 'mat-option-text' and contains(text(), '" + portfolio + "')]").click()
        if str(BIQV2Default) == "N":
            time.sleep(1)
            if len(driver.find_elements(By.XPATH, "//input[@id='mat-checkbox-2-input' and @aria-checked='true']")) > 0:
                driver.find_element(By.XPATH, "//input[@id='mat-checkbox-2-input' and @aria-checked='true']/..").click()
        elif str(BIQV2Default) == "Y":
            if len(driver.find_elements(By.XPATH, "//input[@id='mat-checkbox-2-input' and @aria-checked='false']")) > 0:
                print ("inside if 2")
                driver.find_element(By.XPATH, "//input[@id='mat-checkbox-2-input' and @aria-checked='false']/..").click()
        report("Set My Settings in V2", "Details should be filled", "Details are filled properly", "PASS")
        saveButton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Save']")))
        saveButton.click()
        time.sleep(Environment.wait_time_my_settings_v2)
        subscriberButton = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Subscriber:')]")))
        #wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Subscriber:')]")))
        subcodetext = driver.find_element(By.XPATH, "//span[contains(text(), 'Subscriber:')]").text
        if str(subscriber) in subcodetext:
            report("Save My Settings in V2", "My Settings should be saved", "My Settings set successfully", "PASS")
        else:
            report("Set My Settings in V2", "My Settings should be set", "My Settings not set successfully", "FAILED")
            BuiltIn().set_test_variable("${testcase_status}", "FAIL")
    except Exception as e:
        BuiltIn().log(e.message)
        BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        report("Set My Settings in V2", "My Settings should be set", "My Settings not set successfully " + e.__str__(),
               "FAILED")


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
                   "Default Scoring Model set successfully", "PASSED")
        else:
            report("Validate Default Scoring Model", "Default scoring model should be set",
                   "Default Scoring Model not set successfully", "FAILED")
            BuiltIn().set_test_variable("${testcase_status}", "FAIL")
    except Exception as e:
        BuiltIn().log(e.message)
        BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        report("Validate Default Scoring Model", "Default scoring model should be set",
               "Default Scoring Model not set successfully" + e.__str__(), "FAILED")


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
                   "Default Portfolio set successfully", "PASSED")
        else:
            report("Validate Default Portfolio", "Default Portfolio should be set",
                   "Default Portfolio not set successfully", "FAILED")
            BuiltIn().set_test_variable("${testcase_status}", "FAIL")
    except Exception as e:
        BuiltIn().log(e.message)
        BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        report("Validate Default Portfolio", "Default Portfolio should be set",
               "Default Portfolio not set successfully" + e.__str__(), "FAILED")


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
#                    "Dashboard is not visible", "FAILED")
#     except Exception as e:
#         BuiltIn().log(e.message)
#         BuiltIn().set_test_variable("${testcase_status}", "FAIL")
#         report("Go back to BIQ V1 ", "User Should be able to view BIQ V1 Dashboard",
#                    "Dashboard is not visible"+e.__str__(), "FAILED")

# def validate_login_interface(username,BIQV2Default):
#     try:
#         driver = open_or_get_browser()
#         driver.get(Environment.biq_url)
#         driver.maximize_window()
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
#                        "User logged in and V1 Dashboard is not visible", "Failed")
#             CommonBIQKeywords.logout_from_biq()
#         elif BIQV2Default == 'Y':
#             if len(driver.find_elements(By.XPATH, "//div[@ng-reflect-trigger='https://stg1-ss1.experian.com/']//..")) > 0:
#                 report("Validate user landed in V2 by default ", "User Should be able to view V2 Dashboard",
#                        "User logged in and V2 Dashboard is visible", "PASS")
#             else:
#                 report("Validate user landed in V2 by default ", "User Should be able to view V2 Dashboard",
#                        "User logged in and V2 Dashboard is not visible", "FAILED")
#             CommonBIQKeywords.logout_from_biq2()
#     except Exception as e:
#         BuiltIn().log(e.message)
#         BuiltIn().set_test_variable("${testcase_status}", "FAIL")
#         report("Validate user landed in BIQ"+DefaultInterface+" by default ", "User Should be able to view BIQ"+DefaultInterface+" Dashboard",
#                "User logged in and V"+DefaultInterface+"Dashboard is not visible"+e.__str__(), "FAILED")
