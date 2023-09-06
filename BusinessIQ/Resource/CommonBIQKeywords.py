from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from robot.libraries.BuiltIn import BuiltIn
from FrameworkKeywords import open_or_get_browser, report
import time
import Environment
import UserDetails
from selenium.webdriver.common.keys import Keys


def logout_from_biq():
    driver = open_or_get_browser()
    wait = WebDriverWait(driver, 40)
    try:
        driver.find_element(By.XPATH, "//a[text()='Sign off']").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='okta-signin-username']")))
        if len(driver.find_elements(By.XPATH, "//input[@id='okta-signin-submit']")) > 0:
            report("Logout from BIQ", "User should be logged out", "User logged out from BIQ", "PASSED")
            driver.quit()
            driver.session_id = None
        else:
            report("Logout from BIQ", "User should be logged out", "logout unsuccessful", "FAILED")
            BuiltIn().set_test_variable("${testcase_status}", "FAIL")
            driver.quit()
            driver.session_id = None

    except Exception as e:
        BuiltIn().log(e.message)
        report("Logout from BIQ", "User should be logged out", "logout unsuccessful"+e.__str__(), "FAILED")
        driver.quit()
        driver.session_id = None
        BuiltIn().set_test_variable("${testcase_status}", "FAIL")


def change_subscriber(subcode):
    try:
        driver = open_or_get_browser()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[text()='Change subscriber']").click()
        time.sleep(2)
        if driver.find_element(By.XPATH, 
                "//button[@id='saveChangeSubcriber']/span[text()='Save Changes']").is_displayed():
            driver.find_element(By.XPATH, "//input[@name='subcode' and @value='" + str(subcode) + "']").click()
            BuiltIn().log("********  subcode " + str(subcode) + " selected *************")
            driver.find_element(By.XPATH, "//input[@id='selectSubcodeCheckbox']").click()
            driver.find_element(By.XPATH, "//button[@id='saveChangeSubcriber']/span[text()='Save Changes']").click()
            time.sleep(3)

        subcodetext = driver.find_element(By.XPATH, "//li[contains(text(), 'Subcode : ')]").text
        if str(subcode) in subcodetext:
            report("Change subscriber", "Subscriber should be changed", "Subscriber " + str(subcode) + " is selected",
                   "PASS")
        else:
            report("Change subscriber", "Subscriber should be changed", "Subscriber update failed", "FAIL")
            BuiltIn().set_test_variable("${testcase_status}", "FAIL")

    except Exception as e:
        BuiltIn().log(e.message)
        BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        report("Change Subscriber", "Subscriber should be changed", "Subscriber is not changed", "FAIL")


def change_subscriber_v2(subscriber):
    try:
        driver = open_or_get_browser()
        wait = WebDriverWait(driver, 10)
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[contains(text(), 'Subscriber:')]").click()
        time.sleep(Environment.wait_time_subcode_portfolio_v2)
        if driver.find_element(By.XPATH, 
                "//input[@data-placeholder= 'Select Subcode']").is_displayed():
            driver.find_element(By.XPATH, "//input[@data-placeholder= 'Select Subcode']").clear()
            driver.find_element(By.XPATH, "//input[@data-placeholder= 'Select Subcode']").send_keys(subscriber)
            time.sleep(1)
            driver.find_element(By.XPATH, 
                "//span[@class = 'mat-option-text' and contains(text(), '" + str(subscriber) + "')]").click()
            BuiltIn().log("********  subcode " + str(subscriber) + " selected *************")
            driver.find_element(By.XPATH, "//input[@id = 'mat-checkbox-1-input']//..").click()
            driver.find_element(By.XPATH, "//button//span[text() = ' Save ']").click()
        time.sleep(Environment.wait_time_subcode_portfolio_v2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Subscriber:')]")))
        subcodetext = driver.find_element(By.XPATH, "//span[contains(text(), 'Subscriber:')]").text
        if str(subscriber) in subcodetext:
            report("Change subscriber", "Subscriber should be changed",
                   "Subscriber " + str(subscriber) + " is selected",
                   "PASS")
        else:
            report("Change subscriber", "Subscriber should be changed", "Subscriber update failed", "FAIL")
            BuiltIn().set_test_variable("${testcase_status}", "FAIL")

    except Exception as e:
        BuiltIn().log(e.message)
        BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        report("Change Subscriber", "Subscriber should be changed", "Subscriber is not changed", "FAIL")


def logout_from_biq2():
    try:
        driver = open_or_get_browser()
        # driver.find_element(By.ID, ("body").sendKeys(Keys.CONTROL, Keys.SUBTRACT)
        # time.sleep(5)
        # driver.execute_script("document.body.style.zoom='80%'")
        # time.sleep(5)
        driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, 
            "//button[@id='user-menu-btn']"))
        # driver.find_element(By.XPATH, "//button[@id='user-menu-btn']").click()
        time.sleep(1)
        # driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, 
        #     "//button[contains(text(),'Logout')]"))
        driver.find_element(By.XPATH, "//button[contains(text(),'Logout')]").click()
        time.sleep(3)
        # driver.execute_script("document.body.style.zoom='100%'")
        # time.sleep(5)
        if driver.find_element(By.XPATH, "//input[@id='okta-signin-username']").is_displayed():
            report("Logout from BIQ V2", "User should be logged out", "User logged out from BIQ", "PASSED")
            driver.quit()
            driver.session_id = None
        else:
            report("Logout from BIQ V2", "User should be logged out", "logout unsuccessful", "FAILED")
            BuiltIn().set_test_variable("${testcase_status}", "FAIL")
            driver.quit()
            driver.session_id = None

    except Exception as e:
        BuiltIn().log(e.message)
        report("Logout from BIQ V2", "User should be logged out", "logout unsuccessful"+e.__str__()
               , "FAILED")
        driver.quit()
        driver.session_id = None
        BuiltIn().set_test_variable("${testcase_status}", "FAIL")

def open_biq_dashboard():
    driver = open_or_get_browser()
    try:
        driver.find_element(By.XPATH, "//a[text()='Home']").click()
        time.sleep(2)
        if len(driver.find_elements(By.XPATH, 
                "//div[@class='title_bar']/h1[contains(text(),'Welcome to BusinessIQ!')]")) > 0:
            report("Open BIQ dashboard","BIQ dashboard should be visible","BIQ dashboard is visible","PASSED")
        else:
            report("Open BIQ dashboard", "BIQ dashboard should be visible", "BIQ dashboard is not visible", "FAILED")
    except Exception as e:
        BuiltIn().log(e.message)
        BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        report("Open BIQ dashboard", "BIQ dashboard should be visible", "BIQ dashboard is not visible"+e.__str__(), "FAILED")


def go_to_biq2_dashboard():
    try:
        driver = open_or_get_browser()
        time.sleep(3)
        driver.find_element(By.XPATH, "//mat-icon[contains(text(),'dashboard')]/..").click()
        time.sleep(3)
        report("open biq2 dashboard", "biq2 dashboard should be seen",
               "biq2 dashboard visible", "PASSED")
    except Exception as e:
        BuiltIn().log(e.message)
        BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        report("open biq2 dashboard", "biq2 dashboard should be seen",
               "biq2 dashboard not visible" + e.__str__(), "FAILED")

def validate_pagination_for_grid_biqv2(title):
    try:
        driver = open_or_get_browser()
        wait = WebDriverWait(driver, 40)
        wait.until(EC.visibility_of_element_located(By.XPATH,  "//mat-card-title[contains(text(),'"+str(title)+"')]/../../..//tbody/tr[1]"))
        items = driver.find_element(By.XPATH, "//mat-card-title[contains(text(),'"+str(title)+"')]/../../..//div[@class='mat-paginator-range-label']").text
        if "1" in items and "10" in items:
            report("validate numbering before moving to next page","numbering should show 1-10","numbering is showing as expected","PASSED")
        else:
            report("validate numbering before moving to next page", "numbering should show 1-10",
                   "numbering is not showing as expected", "FAILED")
            BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        driver.find_element(By.XPATH, "//mat-card-title[contains(text(),'"+str(title)+"')]/../../..//button[@class='mat-focus-indicator mat-tooltip-trigger mat-paginator-navigation-next mat-icon-button mat-button-base']").click()
        time.sleep(5)
        wait.until(EC.visibility_of_element_located(By.XPATH,  "//mat-card-title[contains(text(),'"+str(title)+"')]/../../..//tbody/tr[1]"))
        items_after_click = driver.find_element(By.XPATH, "//mat-card-title[contains(text(),'"+str(title)+"')]/../../..//div[@class='mat-paginator-range-label']").text
        if "11" in items_after_click and "20" in items_after_click:
            report("validate numbering after moving to next page","numbering should show 11-20","numbering is showing as expected","PASSED")
        else:
            report("validate numbering before moving to next page", "numbering should show 11-20",
                   "numbering is not showing as expected", "FAILED")
            BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        number_of_items_before_click=len(driver.find_elements(By.XPATH, "//mat-card-title[contains(text(),'"+str(title)+"')]/../../..//tbody/tr"))
        if str(number_of_items_before_click) == "10":
            report("validate number of items in table before click","number of items before click should be 10",
                   "number of items showing as expected","PASSED")
        else:
            report("validate number of items in table before click", "number of items before click should be 10",
                   "number of items not showing as expected", "FAILED")
            BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        driver.find_element(By.XPATH, "//mat-card-title[contains(text(),'"+str(title)+"')]/../../..//div[@class='mat-paginator-container']/div/mat-form-field/div/div/div/mat-select/div").click()
        driver.find_element(By.XPATH, "//mat-option/span[contains(text(),'25')]").click()
        time.sleep(5)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//mat-card-title[contains(text(),'" + str(title) + "')]/../../..//tbody/tr[1]")))
        number_of_items_after_click=len(driver.find_elements(By.XPATH, "//mat-card-title[contains(text(),'"+str(title)+"')]/../../..//tbody/tr"))
        if str(number_of_items_after_click) == "25":
            report("validate number of items in table before click","number of items before click should be 25",
                   "number of items showing as expected","PASSED")
        else:
            report("validate number of items in table before click", "number of items before click should be 25",
                   "number of items not showing as expected", "FAILED")
            BuiltIn().set_test_variable("${testcase_status}", "FAIL")
    except Exception as e:
        BuiltIn().log(e.message)
        BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        report("validate pagination for given list grid","proper pagination should be seen",
               "pagination not functioning as expected"+e.__str__(),"FAILED")