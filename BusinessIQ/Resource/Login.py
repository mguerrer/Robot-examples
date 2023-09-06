from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from robot.libraries.BuiltIn import BuiltIn
from FrameworkKeywords import open_or_get_browser, report, close_browser
import time
import Environment
import UserDetails
import requests
import LoginPage 

def where_am_i_after_login():
    elements_to_wait_for: str=[LoginPage.v1_dashboard_msg,LoginPage.v2_dashboard_page,LoginPage.securityquestions_title_text]
    page_index_found = LoginPage.element_in_array_is_present(elements_to_wait_for)
    return page_index_found
    
    
def fill_and_submit_login_details(username, password):
  
    try:
        LoginPage.enter_credentials(username, password)
        LoginPage.click_log_in_button()
        
    except Exception as e:
        BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        report("Fill BIQ login details", "Login details should be filled", "Exception with message: " + str(e),
               "FAILED")

def login_to_biq(username):
    """Perform the login flow for a user identified by ID.  After complete it will return a page number found after login or -1 on error."""
    
    try:
        password = UserDetails.userDetails[username]
        LoginPage.goto_login_page()

        if LoginPage.login_page_is_loaded():
            report("Open BIQ", "BIQ login page should open", "BIQ login page opened", "PASS")
            fill_and_submit_login_details(username, password)
            page = where_am_i_after_login()
            BuiltIn().log_to_console("Attempting to login...")

            if page == 0: # V1 dashboard
                BuiltIn().log_to_console("I am in Page V1 dashboard after login")
                report("Login to BIQ with the user " + username, "User Should be able to view V1 Dashboard",
                       "V1 Dashboard is visible", "PASS")
            elif page == 1: # V2 Dashboard
                BuiltIn().log_to_console("I am in Page V2 dashboard after login")
                report("Login to BIQ with the user " + username, "User Should be able to view V2 Dashboard",
                    "V2 Dashboard is visible", "PASS")
                go_to_biq_v1()
            elif page == 2: # Security question
                BuiltIn().log_to_console("I am in Page Security Question after login")
                report("Security Question Page", "User Should be able to view Security question page",
                    "Security Question page is visible", "PASSED")
                security_answer = Environment.security_answer
                LoginPage.answer_security_question( security_answer )
            else:
                BuiltIn().log_to_console("FAILED other unknown page is in current location.")
                report("Login to BIQ with the user " + username, "User Should be able to view Dashboard",
                    "Login unsuccessful", "FAILED")
                BuiltIn().set_test_variable("${testcase_status}", "FAIL")
            return page
        else:
            BuiltIn().log_to_console("BIQ login page did not open.")
            report("Open BIQ", "BIQ login page should open", "BIQ login page did not open", "FAIL")
            BuiltIn().set_test_variable("${testcase_status}", "FAIL")
            return -1  # Failure

    except Exception as e:
        BuiltIn().log_to_console("BIQ Exception."+str(e))
        BuiltIn().log(str(e))
        BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        report("Login to BIQ with the user " + username, "Exception not expected",
               "Exception with message: " + str( e ), "FAILED")
        return -1

def attempt_to_login_with_locked_account(username):
    password = UserDetails.userDetails[username]
    security_answer = Environment.security_answer
    try:
        LoginPage.goto_login_page()

        if LoginPage.login_page_is_loaded():
            report("Open BIQ", "BIQ login page should open", "BIQ login page opened", "PASS")
            fill_and_submit_login_details(username, password)
            if LoginPage.locked_account_msg_is_present():
                report("Login to BIQ with the locked user " + username, "User can not login with locked aacount", "V1/V2 Dashboard is not visible", "PASS")
                msg = LoginPage.get_locked_account_msg()
                if  "locked" in msg:
                    report("Login to BIQ with the locked user " + username, "User can not login with locked aacount",
                        "Message ["+msg+"] visible", "PASS")
            else:
                report("Login to BIQ with the locked user " + username, "User can not login with locked aacount",
                       "Login successful???", "FAILED")
                BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        else:
            report("Open BIQ", "BIQ login page should open", "BIQ login page did not open", "FAIL")
            BuiltIn().set_test_variable("${testcase_status}", "FAIL")
            

    except Exception as e:
        BuiltIn().log(str(e))
        BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        report("Login to BIQ with the locked user " + username, "Exception not expected",
               "Exception with message: " + str( e ), "FAILED")

def go_to_biq_v2():
    try:
        LoginPage.click_goto_V2_button()
        LoginPage.wait_until_V2_dashboard_page_is_loaded()
        if LoginPage.V2_dashboard_page_is_loaded():
            report("go to BIQ V2", "User should be in BIQ V2", "User is in BIQ V2", "PASSED")
        else:
            report("go to BIQ V2", "User should be in BIQ V2", "User is not BIQ V2", "FAILED")
        
    except Exception as e:
        BuiltIn().log(str( e ))
        BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        report("go to BIQ V2", "User should be in BIQ V2", "Exception with message: " + str( e ), "FAILED")


def go_to_biq_v1():
    driver = open_or_get_browser()
    try:
        if len(driver.find_elements(By.XPATH, "//a/div[contains(text(),'Back To BusinessIQ V1')]")) > 0:
            driver.find_element(By.XPATH, "//a/div[contains(text(),'Back To BusinessIQ V1')]").click()
            time.sleep(3)
            if not driver.find_element(By.XPATH, "//div[@id='body_group']/div[1]/h1").is_displayed():
                report("Click back to V1 button", "V1 dashboard will be shown", "V1 Dashboard is not visible", "FAILED")
                BuiltIn().set_test_variable("${testcase_status}", "FAIL")
    except Exception as e:
        BuiltIn().log(str( e ))
        BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        report("Click back to V1 button", "V1 dashboard will be shown", "Exception with message: " + str( e ),
               "FAILED")


def validate_v1_dashboard_is_shown():
    try:
        if LoginPage.v1_dashboard_msg_is_present():
            report("V1 dashboard visiblity", "V1 Dashboard should be seen", "V1 Dashboard is seen", "PASSED")
        else:
            report("V1 dashboard visiblity", "V1 Dashboard should be seen", "V1 Dashboard is not seen", "FAILED")
    except Exception as e:
        BuiltIn().log(str( e ))
        BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        report("V1 dashboard visiblity", "V1 Dashboard should be seen", "V1 Dashboard is not seen" + str( e ),
               "FAILED")


def validate_v2_dashboard_is_shown():
    try:
        LoginPage.wait_until_locator_is_visible( LoginPage.v2_dashboard_page )
        if LoginPage.v2_dashboard_page_is_present():
            report("V2 dashboard visiblity", "V2 Dashboard should be seen", "V2 Dashboard is seen", "PASSED")
        else:
            report("V2 dashboard visiblity", "V2 Dashboard should be seen", "V2 Dashboard is not seen", "FAILED")
    except Exception as e:
        BuiltIn().log(str( e ))
        BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        report("V2 dashboard visiblity", "V2 Dashboard should be seen", "V2 Dashboard is not seen" + str( e ),
               "FAILED")


# def login_to_biq_default(username):
#     """
#     This function is used to login in BIQ when BIQ login page is already opened
#     :param username:
#     :return:
#     """
#     driver = open_or_get_browser()
#     password = UserDetails.userDetails[username]
#     security_answer = Environment.security_answer
#     try:
#         fill_and_submit_login_details(username, password, security_answer)
#         time.sleep(4)
#         if len(driver.find_elements(By.XPATH, "//a/div[contains(text(),'Back To BusinessIQ V1')]")) > 0 or len(driver.find_elements(By.XPATH, "//div[@id='body_group']/div[1]/h1")) > 0:
#             report("Login to BIQ with the user " + username, "User Should be able to view Dashboard",
#                    "Dashboard is visible", "PASS")
#         else:
#             report("Login to BIQ with the user " + username, "User Should be able to view Dashboard",
#                    "Dashboard is not visible", "FAILED")
#             BuiltIn().set_test_variable("${testcase_status}", "FAIL")
#     except Exception as e:
#         BuiltIn().log(str( e ))
#         BuiltIn().set_test_variable("${testcase_status}", "FAIL")
#         report("Login to BIQ with the user " + username, "User Should be able to view Dashboard",
#                "Dashboard is not visible", "FAILED")


def logout_from_biq():
    try:
        page = where_am_i_after_login()

        if LoginPage.v1_dashboard_msg_is_present(): # in V1
            BuiltIn().log_to_console("LOGOUT on V1")
            LoginPage.click_V1_logout_link()

        elif LoginPage.v2_dashboard_page_is_present(): # in V2
            BuiltIn().log_to_console("LOGOUT on V2")
            LoginPage.click_V2_logout_link()

        else:
            BuiltIn().log_to_console("LOGOUT FAILED: NOT IN DASHBOARD")
            report("Logout from BIQ", "User should be logged in or Logout button visible", "logout unsuccessful", "FAILED")
            BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        
        BuiltIn().log_to_console("WAIT LOGIN PAGE")
                
        if LoginPage.wait_until_login_page_is_loaded():
            BuiltIn().log_to_console("LOGOUT SUCCESS")
            report("Logout from BIQ", "User should be logged out", "User logged out from BIQ", "PASSED")
        else:
            BuiltIn().log_to_console("LOGOUT FAILED")
            report("Logout from BIQ", "User should be logged out", "logout unsuccessful", "FAILED")
            BuiltIn().set_test_variable("${testcase_status}", "FAIL")
    except Exception as e:
        BuiltIn().log_to_console("LOGOUT EXCEPTION"+str( e ))
        BuiltIn().log(str( e ))
        report("Logout from BIQ", "User should be logged out", "logout unsuccessful" + str( e ), "FAILED")
        BuiltIn().set_test_variable("${testcase_status}", "FAIL")


def validate_forgot_password_link():
    try:
        LoginPage.goto_login_page()

        if LoginPage.login_page_is_loaded():
            LoginPage.click_forgot_password_link()
            if LoginPage.verify_forgot_password_page_loaded():
                report("Validate Forgot Password Link", "Forgot Password link should land user to password recovery page",
                    "Password Recovery page is successfully opened", "PASSED")
                LoginPage.browser_back()
                if LoginPage.login_page_is_loaded():
                    report("Go back to login page",
                        "Login page should be visible", "Login Page is visible", "PASSED")
                else:
                    report("Go back to login page",
                        "Login page should be visible", "Login Page is not visible", "FAILED")
                    BuiltIn().set_test_variable("${testcase_status}", "FAIL")
            else:
                report("Validate Forgot Password Link", "Forgot Password link should land user to password recovery page",
                    "Password Recovery page is not opening", "FAILED")
                BuiltIn().set_test_variable("${testcase_status}", "FAIL")
    except Exception as e:
        BuiltIn().log(str( e ))
        BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        report("Validate Forgot Password Link", "Forgot Password link should land user to password recovery page",
               "Password Recovery page is not opening" + str( e ), "FAILED")


def validate_trouble_logging_in_link():
    try:
        LoginPage.goto_login_page()

        if LoginPage.login_page_is_loaded():
            LoginPage.click_trouble_logging_in_button()
        if LoginPage.verify_suport_page_loaded():
            report("Validate Trouble Logging in Link", "Trouble Logging In link should land user to Support page",
                   "Support page is successfully opened", "PASSED")
            LoginPage.browser_back()
            if LoginPage.login_page_is_loaded():
                report("Go back to login page", "Login page should be visible", "Login Page is visible", "PASSED")
            else:
                report("Go back to login page", "Login page should be visible", "Login Page is not visible", "FAILED")
                BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        else:
            report("Validate Trouble Logging in Link", "Trouble Logging In link should land user to Support page",
                   "Support page is not opening", "FAILED")
            BuiltIn().set_test_variable("${testcase_status}", "FAIL")
    except Exception as e:
        BuiltIn().log(str( e ))
        BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        report("Validate Trouble Logging in Link", "Trouble Logging In link should land user to Support page",
               "Support page is not opening" + str( e ), "FAILED")


def validate_legal_terms_and_conditions():
    try:
        LoginPage.goto_login_page()

        if LoginPage.login_page_is_loaded():
            LoginPage.click_legal_terms_conditions_link()
            new_handle = LoginPage.get_window_handle_by_title("Online Legal Term on Experian.com")
            LoginPage.switch_to_window_by_handle( new_handle )
            if LoginPage.verify_legal_terms_conditions_page_loaded():
                report("Validate Legal Terms And Conditions Link",
                    "Terms and Conditions link should land user to Appropriate page",
                    "Page is successfully opened", "PASSED")
                LoginPage.open_or_get_browser().close()
            else:
                report("Validate Legal Terms And Conditions Link",
                    "Terms and Conditions link should land user to Appropriate page",
                    "Page is not opening", "FAILED")
                BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        else:
            report("Go to login page",
                   "Login page should be visible", "Login Page is not visible", "FAILED")
            BuiltIn().set_test_variable("${testcase_status}", "FAIL")

    except Exception as e:
        BuiltIn().log(str( e ))
        BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        report("Validate Legal Terms And Conditions Link",
               "Terms and Conditions link should land user to Appropriate page",
               "Page is not opening" + str( e ), "FAILED")


def validate_privacy_policy_link():
    try:
        LoginPage.goto_login_page()

        if LoginPage.login_page_is_loaded():
            LoginPage.click_privacy_policy_link()
            new_handle = LoginPage.get_window_handle_by_title("Privacy Policy at Experian.com")
            LoginPage.switch_to_window_by_handle( new_handle )

            if LoginPage.verify_privacy_policy_page_loaded():
                report("Validate Privacy Policy Link",
                        "Privacy Policy link should land user to Privacy Terms page", "Page is successfully opened",
                        "PASSED")
                LoginPage.open_or_get_browser().close()
            else:
                report("Validate Privacy Policy Link",
                        "privacy Policy link should land user to Privacy terms page", "Page is not opening", "FAILED")
                BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        else:
            report("Go to login page",
                   "Login page should be visible", "Login Page is not visible", "FAILED")
            BuiltIn().set_test_variable("${testcase_status}", "FAIL")

    except Exception as e:
        BuiltIn().log(str( e ))
        BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        report("Validate Privacy Policy Link",
               "privacy Policy link should land user to Privacy terms page",
               "Page is not opening" + str( e ), "FAILED")


def validate_contact_us_link():
    try:
        LoginPage.goto_login_page()

        if LoginPage.login_page_is_loaded():            
            LoginPage.click_contact_us_link()
            new_handle = LoginPage.get_window_handle_by_title("BusinessIQ Support from Experian")
            LoginPage.switch_to_window_by_handle( new_handle )
            if LoginPage.verify_suport_page_loaded():
                report("Validate Contact Us Link",
                        "Contact Us link should land user to Support page", "Page is successfully opened", "PASSED")
                LoginPage.open_or_get_browser().close()
            else:
                report("Validate Contact Us Link",
                        "Contact Us link should land user to Support page", "Page is not opening", "FAILED")
                BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        else:
            report("Go to login page", "Login page should be visible", "Login Page is not visible", "FAILED")
            BuiltIn().set_test_variable("${testcase_status}", "FAIL")

    except Exception as e:
        BuiltIn().log(str( e ))
        BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        report("Validate Contact Us Link",
               "Contact Us link should land user to Support page", "Page is not opening" + str( e ), "FAILED")


def validate_watch_the_video_link():
    try:
        LoginPage.goto_login_page()

        if LoginPage.login_page_is_loaded():            
            LoginPage.click_playarrow_watch_the_video_link()
            new_handle = LoginPage.get_window_handle_by_title("Credit Risk Management at Experian.com")
            LoginPage.switch_to_window_by_handle( new_handle )
            if LoginPage.verify_credit_risk_mgmt_page_loaded():
                report("Validate Watch The Video Link", "Watch The Video link should land user to Appropriate page",
                    "Page is successfully opened", "PASSED")
                LoginPage.open_or_get_browser().close()
            else:
                report("Validate Watch The Video Link", "Watch The Video link should land user to Appropriate page",
                    "Page is not opening", "FAILED")
                BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        else:
            report("Go to login page", "Login page should be visible", "Login Page is not visible", "FAILED")
            BuiltIn().set_test_variable("${testcase_status}", "FAIL")

    except Exception as e:
        BuiltIn().log(str( e ))
        BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        report("Validate Watch The Video Link", "Watch The Video link should land user to Appropriate page",
               "Page is not opening"+str( e ), "FAILED")


def validate_read_our_training_docs_link():
    try:
        LoginPage.goto_login_page()

        if LoginPage.login_page_is_loaded():  
            LoginPage.click_read_our_training_docs_arrowforward_link()
            new_handle = LoginPage.get_window_handle_by_title("") # Emerging window has '' title
            LoginPage.switch_to_window_by_handle( new_handle )

            if LoginPage.verify_product_brochure_page_loaded():
                report("Validate Read Our Training Docs link", "Pdf should open on clicking the link",
                    "Pdf successfully opened on clicking the link", "PASSED")
            else:
                report("Validate Read Our Training Docs link", "Pdf should open on clicking the link",
                    "Pdf not opening on clicking the link", "FAILED")
                BuiltIn().set_test_variable("${testcase_status}", "FAIL")
            LoginPage.open_or_get_browser().close()
        else:
            report("Go back to login page", "Login page should be visible", "Login Page is not visible", "FAILED")
            BuiltIn().set_test_variable("${testcase_status}", "FAIL")

    except Exception as e:
        BuiltIn().log(str( e ))
        BuiltIn().set_test_variable("${testcase_status}", "FAIL")


def login_with_wrong_credentials(username):
    driver = open_or_get_browser()
    driver.get(Environment.biq_url)
    driver.maximize_window()
    time.sleep(2)
    security_answer = Environment.security_answer
    try:
        fill_and_submit_login_details(username, "Abcdefgh12345678", security_answer)
        if len(driver.find_elements(By.XPATH, "//p[text()='Sign in failed!']")) > 0:
            report("Login to BIQ with wrong credentials", "User Should be able to view error message",
                   "error message is visible", "PASSED")
        else:
            report("Login to BIQ with wrong credentials", "User Should be able to view error message",
                   "error message is not visible", "FAILED")
            BuiltIn().set_test_variable("${testcase_status}", "FAIL")

    except Exception as e:
        BuiltIn().log(str( e ))
        BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        report("Login to BIQ with wrong credentials", "User Should be able to view error message",
               "error message is not visible" + str( e ), "FAILED")


def login_with_security_question_enabled_user(username, security_answer):
    try:
        driver = open_or_get_browser()
        driver.get(Environment.biq_url)
        driver.maximize_window()
        wait = WebDriverWait(driver, 40)
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='okta-signin-username']").send_keys(username)
        password = UserDetails.userDetails[username]
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='okta-signin-password']").send_keys(password)
        driver.find_element(By.XPATH, "//input[@id='okta-signin-submit']").click()
        time.sleep(4)
        if len(driver.find_elements(By.XPATH, "//h2[text()='Security Question']")) > 0:
            report("Security Question Page", "User Should be able to view Security question page",
                   "Security Question page is visible", "PASSED")
            driver.find_element(By.XPATH, "//input[@placeholder='Answer']").send_keys(security_answer)
            driver.find_element(By.XPATH, "//input[@type='submit']").click()
        else:
            report("Security Question Page", "User Should be able to view Security question page",
                   "Security Question page is not visible", "FAILED")
            BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        time.sleep(4)
        if len(driver.find_elements(By.XPATH, "//div[@id='body_group']/div[1]/h1")) > 0 or len(driver.find_elements(By.XPATH, "//a/div[contains(text(),'Back To BusinessIQ V1')]"))>0:
            report("Login to BIQ with the user " + username, "User Should be able to view Dashboard",
                   "Dashboard is visible", "PASS")
        else:
            report("Login to BIQ with the user " + username, "User Should be able to view Dashboard",
                   "Login unsuccessful", "FAILED")
            BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        if len(driver.find_elements(By.XPATH, "//div[@id='body_group']/div[1]/h1")) > 0:
            driver.find_element(By.XPATH, "//a[text()='Sign off']").click()
            wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='okta-signin-username']")))
            if len(driver.find_elements(By.XPATH, "//input[@id='okta-signin-submit']")) > 0:
                report("Logout from BIQ", "User should be logged out", "User logged out from BIQ", "PASSED")
            else:
                report("Logout from BIQ", "User should be logged out", "logout unsuccessful", "FAILED")
                BuiltIn().set_test_variable("${testcase_status}", "FAIL")

        elif len(driver.find_elements(By.XPATH, "//a/div[contains(text(),'Back To BusinessIQ V1')]")) > 0:
            driver.find_element(By.XPATH, "//button[@id='user-menu-btn']").click()
            time.sleep(1)
            driver.find_element(By.XPATH, "//button[contains(text(),'Logout')]").click()
            time.sleep(3)
            wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='okta-signin-username']")))
            if driver.find_element(By.XPATH, "//input[@id='okta-signin-username']").is_displayed():
                report("Logout from BIQ V2", "User should be logged out", "User logged out from BIQ", "PASSED")
            else:
                report("Logout from BIQ V2", "User should be logged out", "logout unsuccessful", "FAILED")
                BuiltIn().set_test_variable("${testcase_status}", "FAIL")

    except Exception as e:
        BuiltIn().log(str( e ))
        BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        report("Login to BIQ with the user " + username, "Exception not expected",
               "Exception with message: " + str( e ),
               "FAILED")


def validate_password_expired_user(username):
    driver = open_or_get_browser()
    driver.get(Environment.biq_url)
    driver.maximize_window()
    time.sleep(2)
    password = UserDetails.userDetails[username]
    security_answer = Environment.security_answer
    try:
        fill_and_submit_login_details(username, password, security_answer)
        if len(driver.find_elements(By.XPATH, "//h2[text()='Your Okta password has expired']")) > 0:
            report("Login to BIQ with expired password user", "User Should be able to view error message",
                   "error message is visible", "PASSED")
        else:
            report("Login to BIQ with expired password user", "User Should be able to view error message",
                   "error message is not visible", "FAILED")
            BuiltIn().set_test_variable("${testcase_status}", "FAIL")

    except Exception as e:
        BuiltIn().log(str( e ))
        BuiltIn().set_test_variable("${testcase_status}", "FAIL")
        report("Login to BIQ with expired password", "User Should be able to view error message",
               "error message is not visible" + str( e ), "FAILED")


def validate_login_page_is_visible_after_going_back():
    try:
        if LoginPage.wait_until_login_page_is_loaded():
            report("Click on back button",
                   "Login page should be visible", "Login Page is visible", "PASSED")
        else:
            report("Click on back button",
                   "Login page should be visible", "Login Page is not visible", "FAILED")
            BuiltIn().set_test_variable("${testcase_status}", "FAIL")

    except Exception as e:
        BuiltIn().log(str( e ))
        report("Click on back button",
               "Login page should be visible", "Login Page is not visible", "FAILED")
        BuiltIn().set_test_variable("${testcase_status}", "FAIL")
