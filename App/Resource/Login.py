from selenium.webdriver.common.by import By
from robot.libraries.BuiltIn import BuiltIn
from FrameworkKeywords import *
import time
import Environment
import UserDetails

###
# POM for Login page
###

# Login locators
close_window                         = "css selector=#dialog div:nth-of-type(2) button.mdl-button.mdl-button--primary"
contact_us                           = "css selector=#lwrapper div:nth-of-type(3) ul.footer-links li:nth-of-type(3) a"
forgot_password                      = "css selector=button.forget-password-button.mdl-button.mdl-js-button.mdl-button--inverted.mdl-js-ripple-effect.mdl-button--primary"
legal_terms_conditions               = "css selector=#lwrapper div:nth-of-type(3) ul.footer-links li:nth-of-type(1) a"
log_in                               = "xpath=//input[@id='okta-signin-submit']"
page_loaded_text                     = "or registered trademarks of Experian Information Solutions, Inc"
playarrow_watch_the_video            = "css selector=a.mdl-button.mdl-js-button.mdl-button--raised.mdl-js-ripple-effect.mdl-button--primary"
privacy_policy                       = "css selector=#lwrapper div:nth-of-type(3) ul.footer-links li:nth-of-type(2) a"
read_our_training_docs_arrowforward  = "css selector=a.read__training-button.mdl-button.mdl-js-button.mdl-button--stroked.mdl-js-ripple-effect"
username_input                       = "xpath=//input[@id='okta-signin-username']"
password_input                       = "xpath=//input[@id='okta-signin-password']"
banner_maintenance                   = "xpath=//div[@id='banner']"
remembermecheckbox                   = "xpath=//div[@id='okta-sign-in']//form[@action='/access/login.html']/div[1]/div[@class='o-form-fieldset-container']/div[3]//label[.='Remember me']"
trouble_logging_in                   = "css selector=button.faq-button.mdl-button.mdl-js-button.mdl-button--inverted.mdl-js-ripple-effect.mdl-button--primary"
error_alert                          = "xpath=//div[@role='alert']/p"
# Security question locators
securityquestions_title                             = "xpath=//h2[@data-se='o-form-head']"
securityquestions_question                          = "xpath=//form[@id='form60']/div/div/div/div/label"
securityquestions_answer                            = "xpath=//input[@name='answer']"
securityquestions_checkbox_rememberInThisDevice     = "xpath=//input[@name='rememberDevice']"
securityquestions_checkbox_submitButton             = "xpath=//input[@type='submit']"
securityquestions_title_text                        = "xpath=//h2[text()='Security Question']"
securityquestions_locked_account_msg                = "xpath=//p[text()='Your account is locked. Please contact your administrator.']"

# Forgot_password locators
forgotpassword_back_to_sign_in     = "css selector=a.link.help.js-back"
forgotpassword_email_or_username   = "id=account-recovery-username"
forgotpassword_okta                = "css selector=a.inline-block.notranslate"
forgotpassword_page_loaded_text    = "SMS can only be used if a mobile phone number has been configured"
forgotpassword_page_url            = "https://experian-nab.oktapreview.com/signin/forgot-password"
forgotpassword_privacy_policy      = "css selector=a.inline-block.margin-l-10"
forgotpassword_reset_via_email     = "css selector=a.button.button-primary.button-wide.email-button.link-button"
forgotpassword_reset_via_sms       = "css selector=a.button.button-primary.button-wide.sms-button.link-button"

# Other locators
v1_dashboard_msg                   = "xpath=//div[@class='title_bar']/h1[contains(text(),'Welcome to BusinessIQ!')]"
v2_dashboard_page                  = "xpath=//section[@id='dashboard-page']"
back_to_v1_button                  = "xpath=//a/div[contains(text(),'Back To BusinessIQ V1')]"
support_page_text                  = "xpath=//p[contains(text(),'For issues with logging in, forgot your password, or other unexpected errors')]"
legal_terms_conditions_page_text   = "xpath=//h2[text()='Legal Terms']"
privacy_policy_page_text           = "xpath=//div[@id='mainTop']/section/div//h1[@class='text-raspberry']"
credit_risk_mgmt_page_text         = "xpath=//div[@id='mainTop']/section/div//p[.='Manage risk and uncover opportunities all in one solution']"
pdf_file_body_element              = "xpath=//body/embed[@type='application/pdf']"
V1_logout_link                     = "id=logout"
V2_user_menu_button                = "xpath=//button[@id='user-menu-btn']"
V2_logout_link                     = "xpath=//div[@id='mat-menu-panel-0']/div/div[@class='mat-menu-content ng-tns-c140-1']/button[2]"
goto_V2_button                     = "xpath=//div[@id='branding']//a[@href='/App/resources/v2/']"
scheduled_maintenance_alert        = "xpath=//h4/b"
okta_password_expired              = "xpath=//h2[.='Your Okta password has expired']"
unsuccessful_login_reason          = "xpath=//h2[.='Unsuccessful Login to BusinessIQ ']/../../../div/div/span"

# Login page keywords
def goto_login_page():
    """Loads login page."""
    login_url = get_biq_url() + "login.html"
    BuiltIn().log_to_console("goto_login_page: " + login_url)
    driver = open_or_get_browser()
    if driver == None:
        BuiltIn().fail("No webdriver session.")
    driver.get(login_url)
    report("Open BIQ", "BIQ login page should be opened", "BIQ Opened", "PASS")

def click_playarrow_watch_the_video_link():
    """ Click on Playarrow Watch The Video Link."""
    element = find_element_with_locator( playarrow_watch_the_video )
    click_js( element )

def click_privacy_policy_link():
    """ Click on Privacy Policy Link."""
    click_locator( privacy_policy )

def click_read_our_training_docs_arrowforward_link():
    """ Click on Read Our Training Docs Arrowforward Link."""
    element = find_element_with_locator( read_our_training_docs_arrowforward )
    click_js( element )

def click_trouble_logging_in_button():
    """ Click on Trouble Logging In Button."""
    click_locator(  trouble_logging_in )

def enter_credentials(username:str, password:str):
    send_keys( username_input, username )
    send_keys( password_input, password, verbose=False )

def login_page_is_loaded():
    """ Verify that the page loaded completely."""
    c1 = element_is_checked(username_input)
    c2 = element_is_checked(password_input)
    return (c1 and c2 )

def wait_until_login_page_is_loaded():
    """ Verify that the page loaded completely."""
    c1 = wait_until_locator_is_present(username_input)
    c2 = wait_until_locator_is_present(password_input)
    return (c1 and c2 )

def verify_login_error_message( ExpectedErrorMessage: str ):
    """ Verify that current page display error message."""
    wait_until_locator_is_present( error_alert  )
    return page_should_contain( ExpectedErrorMessage )

def verify_not_in_login_page():
    """ Verify that current page display error message."""
    wait_until_location_does_not_contain( get_biq_url() )
    
def security_question_is_present():
    """Indicates if security question is shown"""
    return element_is_checked( securityquestions_title_text )

def answer_security_question( security_answer: str ):
    send_keys( securityquestions_answer, security_answer, verbose=False )
    click_locator( securityquestions_checkbox_rememberInThisDevice )
    click_locator( securityquestions_checkbox_submitButton )
    
def set_input_field(locator, value):
    send_keys(locator, value)
    driver = open_or_get_browser()
    driver.press_keys(locator, 'TAB')
    
def back_to_v1_button_is_present():
    return element_is_checked( back_to_v1_button )

def v1_dashboard_msg_is_present():
    return element_is_checked( v1_dashboard_msg )

def v2_dashboard_page_is_present():
    return element_is_checked( V2_user_menu_button )

def locked_account_msg_is_present():
    return element_is_checked( securityquestions_locked_account_msg )

def forgot_password_link_is_present():
    return element_is_checked( forgot_password )

def click_forgot_password_link():
    return click_locator( forgot_password )

def verify_forgot_password_page_loaded():
    ''' Verify that the page loaded completely.'''
    c1 = element_is_checked(forgotpassword_back_to_sign_in)
    c2 = element_is_checked(forgotpassword_email_or_username)
    c3 = element_is_checked(forgotpassword_reset_via_email)
    c4 = element_is_checked(forgotpassword_reset_via_sms)
    return c1 and c2 and c3 and c4

def verify_suport_page_loaded():
    ''' Verify that the support page loaded.'''
    return element_is_checked(support_page_text)

def verify_legal_terms_conditions_page_loaded():
    ''' Verify that the legal terms page loaded.'''
    return element_is_checked(legal_terms_conditions_page_text)

def verify_privacy_policy_page_loaded():
    ''' Verify that privacy policy page loaded.'''
    return element_is_checked(privacy_policy_page_text)

def verify_credit_risk_mgmt_page_loaded():
    ''' Verify that privacy policy page loaded.'''
    return element_is_checked(credit_risk_mgmt_page_text)

def verify_product_brochure_page_loaded():
    ''' Verify that product brochure page loaded.'''
    c1= location_should_contain("businessiq2.0-product-brochure.pdf")
    c2= element_is_checked( pdf_file_body_element)
    return c1 and c2

def click_V1_logout_link():
    """ Click "Sign off" link on V1 dashboard."""
    click_locator(  V1_logout_link )
    
def click_V2_logout_link():
    """ Click "Sign off" link on V2 dashboard."""
    click_locator( V2_user_menu_button )
    
def click_goto_V2_button():
    """ Click "Sign off" link on V1 dashboard."""
    click_locator(  goto_V2_button )
   # wait_for_page_to_load_and_get()

def V2_dashboard_page_is_loaded():
    ''' Verify that product brochure page loaded.'''
    return element_is_checked( V2_user_menu_button)

def wait_until_V2_dashboard_page_is_loaded():
    ''' Verify that product brochure page loaded.'''
    wait_until_locator_is_present( V2_user_menu_button )
    return element_is_checked( V2_user_menu_button)

SCHEDULED_MAINTENANCE_ALERT=0
ERROR_ALERT=1
SECURITY_QUESTION_PAGE=2
V1_DASHBOARD_PAGE=3
V2_DASHBOARD_PAGE=4
OKTA_PASSWORD_EXPIRED=5
UNSUCCESSFUL_LOGIN=6

def where_am_i_after_login():
    elements_to_wait_for: str=[scheduled_maintenance_alert,error_alert,securityquestions_title_text,goto_V2_button,V2_user_menu_button,okta_password_expired,unsuccessful_login_reason]
    BuiltIn().log_to_console(message="WHERE AM I AFTER LOGIN?...", no_newline=True)
    page_index_found = element_in_array_is_present(elements_to_wait_for, 2*Environment.retry_times)
    BuiltIn().log_to_console("")
    return page_index_found
    
 # Login keywords   

def fill_and_submit_login_details(username, password):
    try:
        enter_credentials(username, password)
        click_locator( log_in )
    except Exception as e:
        report("Fill BIQ login details", "Login details should be filled", "Exception with message: " + e.__str__(),
               "FAIL")

def login_to_biq(username):
    """Perform the login flow for a user identified by ID.  After complete it will return a page number found after login or -1 on error."""
    password = UserDetails.userDetails[username]
    try:
        BuiltIn().log_to_console("\nLOGIN:Attempting to login...")
        if Environment.env_name == "dev": 
            login_url = get_biq_url() + "dashboard/home?ct-remote-user=" + username
            open_or_get_browser().get(login_url)
        else:    
            goto_login_page()
            fill_and_submit_login_details(username, password)
        page = where_am_i_after_login()

        if page == V1_DASHBOARD_PAGE: # V1 dashboard
            report("Login to BIQ with the user " + username, "User Should be able to view V1 Dashboard",
                    "V1 Dashboard is visible", "PASS")
            #wait_until_locator_is_present("xpath=//li[contains(text(), 'Subcode : ')]")
        elif page == ERROR_ALERT: # Error alert
            BuiltIn().fail("There is a login failure:"+ get_text(error_alert))
        elif page == V2_DASHBOARD_PAGE: # V2 Dashboard
            report("Login to BIQ with the user " + username, "User Should be able to view V2 Dashboard",
                "V2 Dashboard is visible", "PASS")
        elif page == SECURITY_QUESTION_PAGE: # Security question
            report("Security Question Page", "User Should be able to view Security question page",
                "Security Question page is visible", "PASS")
            security_answer = Environment.security_answer
            answer_security_question(security_answer)
            page = where_am_i_after_login()
            if page == UNSUCCESSFUL_LOGIN:
                BuiltIn().fail( get_text(unsuccessful_login_reason, not_empty=True))
        elif page == SCHEDULED_MAINTENANCE_ALERT:
            BuiltIn().fail( get_text(scheduled_maintenance_alert))
        elif page == OKTA_PASSWORD_EXPIRED:
            BuiltIn().fail( 'Your Okta password has expired')
        elif page == UNSUCCESSFUL_LOGIN:
            BuiltIn().fail( get_text(unsuccessful_login_reason, not_empty=True))
        else:
            report("Login to BIQ with the user " + username, "User Should be able to view Dashboard",
                "Login unsuccessful", "FAIL")
        return page
    except Exception as e:
        report("Login to BIQ with the user " + username, "Exception not expected",
               "Exception with message: " + e.__str__(), "FAIL")

def attempt_to_login_with_locked_account(username):
    password = UserDetails.userDetails[username]
    try:
        goto_login_page()
        if login_page_is_loaded():
            report("Open BIQ", "BIQ login page should open", "BIQ login page opened", "PASS")
            fill_and_submit_login_details(username, password)
            if locked_account_msg_is_present():
                report("Login to BIQ with the locked user " + username, "User can not login with locked account", "V1/V2 Dashboard is not visible", "PASS")
                msg = get_text( securityquestions_locked_account_msg )
                if "locked" in msg:
                    report("Login to BIQ with the locked user " + username, "User can not login with locked account",
                        "Message ["+msg+"] visible", "PASS")
                else:
                    BuiltIn().fail("Message of locked account not visible.")                    
            else:
                BuiltIn().fail("Message of locked account not visible.")     
        else:
            BuiltIn().fail("BIQ login page did not open")
    except Exception as e:
        report("Login to BIQ with the locked user " + username, "Exception not expected",
               "Exception: " + e.__str__(), "FAIL")

def go_to_biq_v2():
    try:
        if "BusinessIQ/resources/v2/dashboard" in get_driver().current_url:
            report("go to BIQ V2", "User should be in BIQ V2", "User is in BIQ V2", "PASS")
            return
        click_goto_V2_button()
        wait_until_V2_dashboard_page_is_loaded()
        if V2_dashboard_page_is_loaded():
            report("go to BIQ V2", "User should be in BIQ V2", "User is in BIQ V2", "PASS")
        else:
            report("go to BIQ V2", "User should be in BIQ V2", "User is not BIQ V2", "FAIL")
        
    except Exception as e:
        report("go to BIQ V2", "User should be in BIQ V2", "Exception with message: " + e.__str__(), "FAIL")

def go_to_biq_v1():
    driver = open_or_get_browser()
    try:
        if len(driver.find_elements(By.XPATH, "//a/div[contains(text(),'Back To BusinessIQ V1')]")) > 0:
            driver.find_element(By.XPATH, "//a/div[contains(text(),'Back To BusinessIQ V1')]").click()
            time.sleep(3)
            if not driver.find_element(By.XPATH, "//div[@id='body_group']/div[1]/h1").is_displayed():
                report("Click back to V1 button", "V1 dashboard will be shown", "V1 Dashboard is not visible", "FAIL")
    except Exception as e:
        report("Click back to V1 button", "V1 dashboard will be shown", "Exception with message: " + e.__str__(),
               "FAIL")

def validate_v1_dashboard_is_shown():
    if v1_dashboard_msg_is_present():
        report("V1 dashboard visiblity", "V1 Dashboard should be seen", "V1 Dashboard is seen", "PASS")
    else:
        report("V1 dashboard visiblity", "V1 Dashboard should be seen", "V1 Dashboard is not seen", "FAIL")

def validate_v2_dashboard_is_shown():
    if v2_dashboard_page_is_present():
        report("V2 dashboard visiblity", "V2 Dashboard should be seen", "V2 Dashboard is seen", "PASS")
    else:
        report("V2 dashboard visiblity", "V2 Dashboard should be seen", "V2 Dashboard is not seen", "FAIL")

def logout_from_biq():
    try:
        if Environment.env_name == 'dev': 
            close_session()
            report("Logout from BIQ", "User should be logged out", "User logged out from BIQ", "PASS")
            return
            
        if element_is_checked(V1_logout_link): # in V1
            click_V1_logout_link()
        elif element_is_checked(V2_user_menu_button): # in V2
            click_V2_logout_link()
            clickjs_element_and_wait_next_element_with_retry(V2_logout_link, username_input )
        else:
            report("Logout from BIQ", "User should be logged in or Logout button visible", "logout unsuccessful", "FAIL")
        
        if wait_until_login_page_is_loaded():
            report("Logout from BIQ", "User should be logged out", "User logged out from BIQ", "PASS")
        else:
            report("Logout from BIQ", "User should be logged out", "logout unsuccessful", "FAIL")
    except Exception as e:
        report("Logout from BIQ", "User should be logged out", "logout unsuccessful" + e.__str__(), "FAIL")

def logout_from_biq_v2():
    try:
        if wait_until_locator_is_present(V2_user_menu_button): # in V2
            click_V2_logout_link()
            clickjs_element_and_wait_next_element_with_retry(V2_logout_link, username_input )
        else:
            report("Logout from BIQ", "User should be logged in or Logout button visible", "logout unsuccessful", "FAIL")
        
        if wait_until_login_page_is_loaded():
            report("Logout from BIQ", "User should be logged out", "User logged out from BIQ", "PASS")
        else:
            report("Logout from BIQ", "User should be logged out", "logout unsuccessful", "FAIL")
    except Exception as e:
        report("Logout from BIQ", "User should be logged out", "logout unsuccessful" + e.__str__(), "FAIL")

def validate_forgot_password_link():
    try:
        goto_login_page()

        if login_page_is_loaded():
            click_forgot_password_link()
            if verify_forgot_password_page_loaded():
                report("Validate Forgot Password Link", "Forgot Password link should land user to password recovery page",
                    "Password Recovery page is successfully opened", "PASS")
                browser_back()
                if login_page_is_loaded():
                    report("Go back to login page",
                        "Login page should be visible", "Login Page is visible", "PASS")
                else:
                    report("Go back to login page",
                        "Login page should be visible", "Login Page is not visible", "FAIL")
            else:
                report("Validate Forgot Password Link", "Forgot Password link should land user to password recovery page",
                    "Password Recovery page is not opening", "FAIL")
    except Exception as e:
        report("Validate Forgot Password Link", "Forgot Password link should land user to password recovery page",
               "Password Recovery page is not opening" + e.__str__(), "FAIL")


def validate_trouble_logging_in_link():
    try:
        goto_login_page()

        if login_page_is_loaded():
            click_trouble_logging_in_button()
        if verify_suport_page_loaded():
            report("Validate Trouble Logging in Link", "Trouble Logging In link should land user to Support page",
                   "Support page is successfully opened", "PASS")
            browser_back()
            if login_page_is_loaded():
                report("Go back to login page", "Login page should be visible", "Login Page is visible", "PASS")
            else:
                report("Go back to login page", "Login page should be visible", "Login Page is not visible", "FAIL")
        else:
            report("Validate Trouble Logging in Link", "Trouble Logging In link should land user to Support page",
                   "Support page is not opening", "FAIL")
    except Exception as e:
        report("Validate Trouble Logging in Link", "Trouble Logging In link should land user to Support page",
               "Support page is not opening" + e.__str__(), "FAIL")


def validate_legal_terms_and_conditions():
    try:
        goto_login_page()

        if login_page_is_loaded():
            click_locator( legal_terms_conditions )
            new_handle = get_window_handle_by_title("Online Legal Term on Experian.com")
            switch_to_window_by_handle( new_handle )
            if verify_legal_terms_conditions_page_loaded():
                report("Validate Legal Terms And Conditions Link",
                    "Terms and Conditions link should land user to Appropriate page",
                    "Page is successfully opened", "PASS")
                open_or_get_browser().close()
            else:
                report("Validate Legal Terms And Conditions Link",
                    "Terms and Conditions link should land user to Appropriate page",
                    "Page is not opening", "FAIL")
        else:
            report("Go to login page",
                   "Login page should be visible", "Login Page is not visible", "FAIL")
    
    except Exception as e:
        report("Validate Legal Terms And Conditions Link",
               "Terms and Conditions link should land user to Appropriate page",
               "Page is not opening" + e.__str__(), "FAIL")


def validate_privacy_policy_link():
    try:
        goto_login_page()

        if login_page_is_loaded():
            click_privacy_policy_link()
            new_handle = get_window_handle_by_title("Privacy Policy at Experian.com")
            switch_to_window_by_handle( new_handle )

            if verify_privacy_policy_page_loaded():
                report("Validate Privacy Policy Link",
                        "Privacy Policy link should land user to Privacy Terms page", "Page is successfully opened",
                        "PASS")
                open_or_get_browser().close()
            else:
                report("Validate Privacy Policy Link",
                        "privacy Policy link should land user to Privacy terms page", "Page is not opening", "FAIL")
        else:
            report("Go to login page",
                   "Login page should be visible", "Login Page is not visible", "FAIL")
    
    except Exception as e:
        report("Validate Privacy Policy Link",
               "privacy Policy link should land user to Privacy terms page",
               "Page is not opening" + e.__str__(), "FAIL")


def validate_contact_us_link():
    try:
        goto_login_page()

        if login_page_is_loaded():            
            click_locator( contact_us )
            new_handle = get_window_handle_by_title("BusinessIQ Support from Experian")
            switch_to_window_by_handle( new_handle )
            if verify_suport_page_loaded():
                report("Validate Contact Us Link",
                        "Contact Us link should land user to Support page", "Page is successfully opened", "PASS")
                open_or_get_browser().close()
            else:
                report("Validate Contact Us Link",
                        "Contact Us link should land user to Support page", "Page is not opening", "FAIL")
        else:
            report("Go to login page", "Login page should be visible", "Login Page is not visible", "FAIL")
    
    except Exception as e:
        report("Validate Contact Us Link",
               "Contact Us link should land user to Support page", "Page is not opening" + e.__str__(), "FAIL")


def validate_watch_the_video_link():
    try:
        goto_login_page()

        if login_page_is_loaded():            
            click_playarrow_watch_the_video_link()
            new_handle = get_window_handle_by_title("Credit Risk Management at Experian.com")
            switch_to_window_by_handle( new_handle )
            if verify_credit_risk_mgmt_page_loaded():
                report("Validate Watch The Video Link", "Watch The Video link should land user to Appropriate page",
                    "Page is successfully opened", "PASS")
                open_or_get_browser().close()
            else:
                report("Validate Watch The Video Link", "Watch The Video link should land user to Appropriate page",
                    "Page is not opening", "FAIL")
        else:
            report("Go to login page", "Login page should be visible", "Login Page is not visible", "FAIL")
    
    except Exception as e:
        report("Validate Watch The Video Link", "Watch The Video link should land user to Appropriate page",
               "Page is not opening"+e.__str__(), "FAIL")


def validate_read_our_training_docs_link():
    try:
        goto_login_page()

        if login_page_is_loaded():  
            click_read_our_training_docs_arrowforward_link()
            new_handle = get_window_handle_by_title("") # Emerging window has '' title
            switch_to_window_by_handle( new_handle )

            if verify_product_brochure_page_loaded():
                report("Validate Read Our Training Docs link", "Pdf should open on clicking the link",
                    "Pdf successfully opened on clicking the link", "PASS")
            else:
                report("Validate Read Our Training Docs link", "Pdf should open on clicking the link",
                    "Pdf not opening on clicking the link", "FAIL")
                open_or_get_browser().close()
        else:
            report("Go back to login page", "Login page should be visible", "Login Page is not visible", "FAIL")
    
    except Exception as e:
        report("Validate Read Our Training Docs link", "Pdf should open on clicking the link",
                    "Pdf not opening on clicking the link:"+ e.__str__(), "FAIL")


def login_with_wrong_credentials(username):
    try:
        driver = open_or_get_browser()
        goto_login_page()
        fill_and_submit_login_details(username, "Abcdefgh12345678")
        if len(driver.find_elements(By.XPATH, "//p[text()='Sign in failed!']")):
            report("Login to BIQ with wrong credentials", "Error message will be shown",
                   "Error message is visible", "PASS")
        else:
            report("Login to BIQ with wrong credentials", "Error message will be shown",
                   "Error message is not shown", "FAIL")
    except Exception as e:
        report( "Login to BIQ with wrong credentials", "Error message will be shown",
                "Error message is not visible" + e.__str__(), "FAIL")


def login_with_security_question_enabled_user(username, security_answer):
    try:
        driver = open_or_get_browser()
        driver.get(get_biq_url())
        driver.find_element(By.XPATH, "//input[@id='okta-signin-username']").send_keys(username)
        password = UserDetails.userDetails[username]
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='okta-signin-password']").send_keys(password)
        driver.find_element(By.XPATH, "//input[@id='okta-signin-submit']").click()
        time.sleep(4)
        if len(driver.find_elements(By.XPATH, "//h2[text()='Security Question']")) > 0:
            report("Security Question Page", "User Should be able to view Security question page",
                   "Security Question page is visible", "PASS")
            driver.find_element(By.XPATH, "//input[@placeholder='Answer']").send_keys(security_answer)
            driver.find_element(By.XPATH, "//input[@type='submit']").click()
        else:
            report("Security Question Page", "User Should be able to view Security question page",
                   "Security Question page is not visible", "FAIL")
            time.sleep(4)
        if len(driver.find_elements(By.XPATH, "//div[@id='body_group']/div[1]/h1")) > 0 or len(driver.find_elements(By.XPATH, "//a/div[contains(text(),'Back To BusinessIQ V1')]"))>0:
            report("Login to BIQ with the user " + username, "User Should be able to view Dashboard",
                   "Dashboard is visible", "PASS")
        else:
            report("Login to BIQ with the user " + username, "User Should be able to view Dashboard",
                   "Login unsuccessful", "FAIL")
        if len(driver.find_elements(By.XPATH, "//div[@id='body_group']/div[1]/h1")) > 0:
            driver.find_element(By.XPATH, "//a[text()='Sign off']").click()
            if len(driver.find_elements(By.XPATH, "//input[@id='okta-signin-submit']")) > 0:
                report("Logout from BIQ", "User should be logged out", "User logged out from BIQ", "PASS")
            else:
                report("Logout from BIQ", "User should be logged out", "logout unsuccessful", "FAIL")
        
        elif len(driver.find_elements(By.XPATH, "//a/div[contains(text(),'Back To BusinessIQ V1')]")) > 0:
            driver.find_element(By.XPATH, "//button[@id='user-menu-btn']").click()
            time.sleep(1)
            driver.find_element(By.XPATH, "//button[contains(text(),'Logout')]").click()
            time.sleep(3)
            if driver.find_element(By.XPATH, "//input[@id='okta-signin-username']").is_displayed():
                report("Logout from BIQ V2", "User should be logged out", "User logged out from BIQ", "PASS")
            else:
                report("Logout from BIQ V2", "User should be logged out", "logout unsuccessful", "FAIL")
        
    except Exception as e:
        
        report("Login to BIQ with the user " + username, "Exception not expected",
               "Exception with message: " + e.__str__(),
               "FAIL")


def validate_password_expired_user(username):
    password = UserDetails.userDetails[username]
    security_answer = Environment.security_answer
    try:
        driver = open_or_get_browser()
        goto_login_page()
        fill_and_submit_login_details(username, password)
        if len(driver.find_elements(By.XPATH, "//h2[text()='Security Question']")) > 0:
            report("Security Question Page", "User Should be able to view Security question page",
                   "Security Question page is visible", "PASS")
            driver.find_element(By.XPATH, "//input[@placeholder='Answer']").send_keys(security_answer)
            driver.find_element(By.XPATH, "//input[@type='submit']").click()
            time.sleep(3)
        if len(driver.find_elements(By.XPATH, '//h2[text()="Your Okta password has expired"]')) > 0:
            report("Login to BIQ with expired password user", "Password expiry message will be shown",
                   "Password expiry message shown", "PASS")
        else:
            report("Login to BIQ with expired password user", "Password expiry message will be shown",
                   "Password expiry message was not shown", "FAIL")
    
    except Exception as e:
        report("Login to BIQ with expired password", "Password expiry message will be shown",
               "Exception: " + e.__str__(), "FAIL")


def validate_login_page_is_visible_after_going_back():
    try:
        if wait_until_login_page_is_loaded():
            report("Click on back button",
                   "Login page should be visible", "Login Page is visible", "PASS")
        else:
            report("Click on back button",
                   "Login page should be visible", "Login Page is not visible", "FAIL")
    
    except Exception as e:
        report("Click on back button",
               "Login page should be visible", "Login Page is not visible", "FAIL")
