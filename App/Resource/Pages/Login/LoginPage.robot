###
# POM for Login page
###
*** Settings ***
Documentation  BusinessIQ web application page object.
Library  SeleniumLibrary


*** Variables ***
${biq.login.close}                                css=#dialog div:nth-of-type(2) button.mdl-button.mdl-button--primary
${biq.login.contact_us}                           css=#lwrapper div:nth-of-type(3) ul.footer-links li:nth-of-type(3) a
${biq.login.forgot_password}                      css=button.forget-password-button.mdl-button.mdl-js-button.mdl-button--inverted.mdl-js-ripple-effect.mdl-button--primary
${biq.login.legal_terms_conditions}               css=#lwrapper div:nth-of-type(3) ul.footer-links li:nth-of-type(1) a
${biq.login.log_in}                               id=okta-signin-submit
${biq.login.forgot_password_link}                 css=a.link.js-forgot-password
${biq.login.page_loaded_text}                     or registered trademarks of Experian Information Solutions, Inc
${biq.login.page_url}                             /App/login.html
${biq.login.playarrow_watch_the_video}            css=a.mdl-button.mdl-js-button.mdl-button--raised.mdl-js-ripple-effect.mdl-button--primary
${biq.login.privacy_policy}                       css=#lwrapper div:nth-of-type(3) ul.footer-links li:nth-of-type(2) a
${biq.login.read_our_training_docs_arrowforward}  css=a.read__training-button.mdl-button.mdl-js-button.mdl-button--stroked.mdl-js-ripple-effect
${biq.login.username}                             id=okta-signin-username
${biq.login.password}                             id=okta-signin-password
${biq.login.remembermecheckbox}                   id=input41
${biq.login.trouble_logging_in}                   css=button.faq-button.mdl-button.mdl-js-button.mdl-button--inverted.mdl-js-ripple-effect.mdl-button--primary
${biq.login.error_alert}                          xpath=//div[@id='okta-sign-in']//form[@action='/App/login.html']/div[1]//div[@role='alert']/p

*** Keywords ***
Click Close Button
    [Documentation]  Click on Close Button.
    Click Button  ${biq.login.close}

Click Contact Us Link
    [Documentation]  Click on Contact Us Link.
    Click Link  ${biq.login.contact_us}

Click Forgot Password Button
    [Documentation]  Click on Forgot Password Button.
    Click Button  ${biq.login.forgot_password}

Click Legal Terms Conditions Link
    [Documentation]  Click on Legal Terms Conditions Link.
    Click Link  ${biq.login.legal_terms_conditions}

Click Log In Button
    [Documentation]  Click on Log In Button.
    Click Button  ${biq.login.log_in}

Click Forgot Password Link
    [Documentation]  Click on Forgot Password Link.
    Click Link  ${biq.login.forgot_password_link}

Click Playarrow Watch The Video Link
    [Documentation]  Click on Playarrow Watch The Video Link.
    Click Link  ${biq.login.playarrow_watch_the_video}

Click Privacy Policy Link
    [Documentation]  Click on Privacy Policy Link.
    Click Link  ${biq.login.privacy_policy}

Click Read Our Training Docs Arrowforward Link
    [Documentation]  Click on Read Our Training Docs Arrowforward Link.
    Click Link  ${biq.login.read_our_training_docs_arrowforward}

Click Trouble Logging In Button
    [Documentation]  Click on Trouble Logging In Button.
    Click Button  ${biq.login.trouble_logging_in}

Enter Credentials
    [Arguments]  ${username}     ${password}
    Set Username Field       ${username}
    Set Password Field      ${password} 

Set Username Field
    [Arguments]  ${username_value}=USERNAME
    [Documentation]  Set value to Username field.
    Input Text  ${biq.login.username}  ${username_value}

Set Password Field
    [Arguments]  ${password_value}=PASSWORD
    [Documentation]  Set value to Password field.
    Input Text  ${biq.login.password}  ${password_value}

Set Remember Me Checkbox Field
    [Documentation]  Set "Remember me" Checkbox field.
    Select Checkbox  ${biq.login.remembermecheckbox}

Submit
    [Documentation]  Submit the form to target page.
    Click Log In Button

Unset Remember Me Checkbox Field
    [Documentation]  Unset Recordarme Checkbox field.
    Unselect Checkbox  ${biq.login.remembermecheckbox}

Verify Login Page Loaded
    [Documentation]  Verify that the page loaded completely.
    Wait Until Page Contains  ${biq.login.page_loaded_text}

Verify Login Page Url
    [Documentation]  Verify that current page URL matches the expected URL.
    Location Should Contain  ${biq.login.page_url}

Verify Login Error Message
    [Arguments]  ${ExpectedErrorMessage}
    Wait Until Element Is Visible    ${biq.login.error_alert}  
    Page Should Contain    ${ExpectedErrorMessage}

Verify Not In Login Page
    Wait Until Location Does Not Contain    ${biq.login.page_url}