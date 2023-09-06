###
# POM for Login page security questions
###
*** Settings ***
Documentation  BusinessIQ web application page object.
Library    SeleniumLibrary


*** Variables ***
${biq.login.securityquestions.title}       xpath=//h2[@data-se='o-form-head']
${biq.login.securityquestions.question}    xpath=//form[@id='form60']/div/div/div/div/label
${biq.login.securityquestions.answer}      xpath=//input[@name='answer']
${biq.login.securityquestions.checkbox.rememberInThisDevice}      xpath=//input[@name='rememberDevice']
${biq.login.securityquestions.checkbox.submitButton}      xpath=//input[@type='submit']

*** Keywords ***
If Security Question Appears Then Answer
    Sleep    5 seconds
    ${count}=    Get Element Count    ${biq.login.securityquestions.question}
    IF    ${count} == 1 
        Wait Until Element Is Visible     ${biq.login.securityquestions.question}    timeout=0.5 seconds
        Log To Console    Questions  
        ${question} =    Get Text    ${biq.login.securityquestions.question}
        Log To Console    Question:    ${question} 
        Input Text    ${biq.login.securityquestions.answer}    cholito
        Wait Until Element Is Enabled    ${biq.login.securityquestions.checkbox.submitButton}
        Click Element    ${biq.login.securityquestions.checkbox.submitButton}
    ELSE  
        Log To Console    No Questions  
    END