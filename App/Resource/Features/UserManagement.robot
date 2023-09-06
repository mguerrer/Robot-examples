*** Settings ***
Resource    ${EXECDIR}/BusinessIQ/Resource/Common.robot
Resource    ${EXECDIR}/BusinessIQ/Resource/Pages/Login/LoginPage.robot
Resource    ${EXECDIR}/BusinessIQ/Resource/Pages/Login/LoginSecurityQuestion.robot
Resource    ${EXECDIR}/BusinessIQ/Data/DataManager.robot

*** Keywords ***
Navigate To Login Page
    ${SignInUrl} =  Catenate  SEPARATOR=/  ${BASE_URL.${ENVIRONMENT}}  ${LOGIN_URL}
    go to  ${SignInUrl}

Attempt Login With UserName Only
    [Arguments]  ${username}
    ${password}    Get User Password    ${username}
    LoginPage.Enter Credentials  ${username}    ${password}
    Submit and complete flow

Attempt Login With UserName And Password
    [Arguments]  ${username}    ${password}
    LoginPage.Enter Credentials  ${username}    ${password}
    Submit and complete flow

Attempt Login With UserName And Password Without Validation
    [Arguments]  ${username}    ${password}
    LoginPage.Enter Credentials  ${username}    ${password}
    LoginPage.Submit


Attempt Login With Credentials
    [Arguments]  ${credentials}
    LoginPage.Enter Credentials  ${credentials[0]}    ${credentials[1]}
    Submit and complete flow

Submit and complete flow
    LoginPage.Submit
    If Security Question Appears Then Answer
    LoginPage.Verify Not In Login Page

Verify Login Page Error Message
    [Arguments]  ${ExpectedErrorMessage}
    ${page_text}=    Get Source
    Should Contain    ${page_text}    ${ExpectedErrorMessage}

Attempt Login With Credentials Without Validation
    [Arguments]  ${credentials}
    LoginPage.Enter Credentials  ${credentials[0]}    ${credentials[1]}
    LoginPage.Submit