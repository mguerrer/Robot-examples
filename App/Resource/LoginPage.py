###
# POM for Login page
###


from FrameworkKeywords import *
from robot.libraries.BuiltIn import BuiltIn
import Environment

# Login locators
close_window                         = "css_selector=#dialog div:nth-of-type(2) button.mdl-button.mdl-button--primary"
contact_us                           = "css_selector=#lwrapper div:nth-of-type(3) ul.footer-links li:nth-of-type(3) a"
forgot_password                      = "css_selector=button.forget-password-button.mdl-button.mdl-js-button.mdl-button--inverted.mdl-js-ripple-effect.mdl-button--primary"
legal_terms_conditions               = "css_selector=#lwrapper div:nth-of-type(3) ul.footer-links li:nth-of-type(1) a"
log_in                               = "id=okta-signin-submit"
page_loaded_text                     = "or registered trademarks of Experian Information Solutions, Inc"
page_url                             = "login.html"
playarrow_watch_the_video            = "css_selector=a.mdl-button.mdl-js-button.mdl-button--raised.mdl-js-ripple-effect.mdl-button--primary"
privacy_policy                       = "css_selector=#lwrapper div:nth-of-type(3) ul.footer-links li:nth-of-type(2) a"
read_our_training_docs_arrowforward  = "css_selector=a.read__training-button.mdl-button.mdl-js-button.mdl-button--stroked.mdl-js-ripple-effect"
username_input                       = "id=okta-signin-username"
password_input                       = "id=okta-signin-password"
remembermecheckbox                   = "id=input41"
trouble_logging_in                   = "css_selector=button.faq-button.mdl-button.mdl-js-button.mdl-button--inverted.mdl-js-ripple-effect.mdl-button--primary"
error_alert                          = "xpath=//div[@= By.ID( \"'okta-sign-in']//form[@action='/App/html']/div[1]//div[@role='alert']/p"
# Security question locators
securityquestions_title                             = "xpath=//h2[@data-se='o-form-head']"
securityquestions_question                          = "xpath=//form[@id='form60']/div/div/div/div/label"
securityquestions_answer                            = "xpath=//input[@name='answer']"
securityquestions_checkbox_rememberInThisDevice     = "xpath=//input[@name='rememberDevice']"
securityquestions_checkbox_submitButton             = "xpath=//input[@type='submit']"
securityquestions_title_text                        = "xpath=//h2[text()='Security Question']"
securityquestions_locked_account_msg                = "css_selector=div[role='alert'] > p"

# Forgot_password locators
forgotpassword_back_to_sign_in     = "css_selector=a.link.help.js-back"
forgotpassword_email_or_username   = "id=account-recovery-username"
forgotpassword_okta                = "css_selector=a.inline-block.notranslate"
forgotpassword_page_loaded_text    = "SMS can only be used if a mobile phone number has been configured"
forgotpassword_page_url            = "https://experian-nab.oktapreview.com/signin/forgot-password"
forgotpassword_privacy_policy      = "css_selector=a.inline-block.margin-l-10"
forgotpassword_reset_via_email     = "css_selector=a.button.button-primary.button-wide.email-button.link-button"
forgotpassword_reset_via_sms       = "css_selector=a.button.button-primary.button-wide.sms-button.link-button"

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
V2_logout_link                     = "xpath=(//button[@role='menuitem'])[2]"
goto_V2_button                     = "xpath=//div[@id='branding']//a[@href='/App/resources/v2/']"

# Login page keywords
def goto_login_page():
    """Loads login page only if is not already loaded."""
    BuiltIn().log_to_console( "goto_login_page "+page_url)
    driver = open_or_get_browser()
    if ( page_url not in driver.current_url):
        url = Environment.biq_url+page_url
        driver.get(Environment.biq_url+page_url)
        driver.maximize_window()
        wait_until_login_page_is_loaded()
    
def click_close_button():
    """ Click on Close Button."""
    click_locator( close_window )

def click_contact_us_link():
    """ Click on Contact Us Link."""
    click_locator( contact_us )

def click_forgot_password_button():
    """ Click on Forgot Password Button."""
    click_locator(  forgot_password )

def click_legal_terms_conditions_link():
    """ Click on Legal Terms Conditions Link."""
    click_locator( legal_terms_conditions )

def click_log_in_button():
    """ Click on Log In Button."""
    click_locator( log_in )

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
    send_keys( password_input, password )

def set_username_field(  username_value: str):
    """ Set value to Username field."""
    send_keys( username_input,  username_value )

def set_password_field( password_value: str ):
    """ Set value to Password field."""
    send_keys( password_input,  password_value )

def click_remember_me_checkbox_field():
    """ Set "Remember me" Checkbox field."""
    click_locator(  remembermecheckbox )

def login_page_is_loaded():
    """ Verify that the page loaded completely."""
    c1 = element_is_present(username_input)
    c2 = element_is_present(password_input)
    return (c1 and c2 )

def wait_until_login_page_is_loaded():
    """ Verify that the page loaded completely."""
    c1 = wait_until_locator_is_visible(username_input)
    c2 = wait_until_locator_is_visible(password_input)
    return (c1 and c2 )

def verify_login_page_url():
    """ Verify that current page URL matches the expected URL."""
    location_should_contain( page_url )

def verify_login_error_message( ExpectedErrorMessage: str ):
    """ Verify that current page display error message."""
    wait_until_locator_is_visible( error_alert  )
    page_should_contain( ExpectedErrorMessage )

def verify_not_in_login_page():
    """ Verify that current page display error message."""
    wait_until_location_does_not_contain( page_url )
    
def security_question_is_present():
    """Indicates if security question is shown"""
    return element_is_present( securityquestions_title_text )

def answer_security_question( security_answer: str ):
    send_keys( securityquestions_answer, security_answer )
    click_locator( securityquestions_checkbox_submitButton )
    
def set_input_field(locator, value):
    send_keys(locator, value)
    driver = open_or_get_browser()
    driver.press_keys(locator, 'TAB')
    
def back_to_v1_button_is_present():
    return element_is_present( back_to_v1_button )

def v1_dashboard_msg_is_present():
    return element_is_present( v1_dashboard_msg )

def v2_dashboard_page_is_present():
    return element_is_present( v2_dashboard_page )

def locked_account_msg_is_present():
    return element_is_present( securityquestions_locked_account_msg )

def get_locked_account_msg():
    return get_text( securityquestions_locked_account_msg )

def forgot_password_link_is_present():
    return element_is_present( forgot_password )

def click_forgot_password_link():
    return click_locator( forgot_password )

# Forgot_password keywords
# Click Back To Sign In Link
#     [Documentation]  Click on Back To Sign In Link.
#     Click Link  ${forgotpassword.back_to_sign_in}

# Click Okta Link
#     [Documentation]  Click on Okta Link.
#     Click Link  ${forgotpassword.okta}

# Click Privacy Policy Link
#     [Documentation]  Click on Privacy Policy Link.
#     Click Link  ${forgotpassword.privacy_policy}

# Click Reset Via Email Link
#     [Documentation]  Click on Reset Via Email Link.
#     Click Link  ${forgotpassword.reset_via_email}

# Click Reset Via Sms Link
#     [Documentation]  Click on Reset Via Sms Link.
#     Click Link  ${forgotpassword.reset_via_sms}

# Fill
#     [Documentation]  Fill every fields in the page.
#     ForgotPassword.Set Email Or Username Text Field

# Set Email Or Username Text Field
#     [Arguments]  ${email_or_username_value}=${DATA['EMAIL_OR_USERNAME']}
#     [Documentation]  Set value to Email Or Username Text field.
#     Input Text  ${forgotpassword.email_or_username}  ${email_or_username_value}

def verify_forgot_password_page_loaded():
    ''' Verify that the page loaded completely.'''
    c1 = element_is_present(forgotpassword_back_to_sign_in)
    c2 = element_is_present(forgotpassword_email_or_username)
    c3 = element_is_present(forgotpassword_reset_via_email)
    c4 = element_is_present(forgotpassword_reset_via_sms)
    return c1 and c2 and c3 and c4

# Verify Page Url
#     [Documentation]  Verify that current page URL matches the expected URL.
#     Location Should Contain  ${forgotpassword.page_url}
def verify_suport_page_loaded():
    ''' Verify that the support page loaded.'''
    return element_is_present(support_page_text)

def verify_legal_terms_conditions_page_loaded():
    ''' Verify that the legal terms page loaded.'''
    return element_is_present(legal_terms_conditions_page_text)

def verify_privacy_policy_page_loaded():
    ''' Verify that privacy policy page loaded.'''
    return element_is_present(privacy_policy_page_text)

def verify_credit_risk_mgmt_page_loaded():
    ''' Verify that privacy policy page loaded.'''
    return element_is_present(credit_risk_mgmt_page_text)

def verify_product_brochure_page_loaded():
    ''' Verify that product brochure page loaded.'''
    c1= location_should_contain("businessiq2.0-product-brochure.pdf")
    c2= element_is_present( pdf_file_body_element)
    return c1 and c2

def click_V1_logout_link():
    """ Click "Sign off" link on V1 dashboard."""
    click_locator(  V1_logout_link )
    
def click_V2_logout_link():
    """ Click "Sign off" link on V2 dashboard."""
    click_locator( V2_user_menu_button )
    logout_link = find_element_with_locator(V2_logout_link)
    wait_until_locator_is_visible( V2_logout_link )
    click_locator( V2_logout_link )
    
def click_goto_V2_button():
    """ Click "Sign off" link on V1 dashboard."""
    click_locator(  goto_V2_button )
   # wait_for_page_to_load_and_get()

def V2_dashboard_page_is_loaded():
    ''' Verify that product brochure page loaded.'''
    return element_is_present( V2_user_menu_button)

def wait_until_V2_dashboard_page_is_loaded():
    ''' Verify that product brochure page loaded.'''
    wait_until_locator_is_visible( V2_user_menu_button )
    return element_is_present( V2_user_menu_button)
