*** Settings ***
Documentation     Example test cases using the data-driven testing approach.
Test Template     Login
Resource    ${EXECDIR}/App/Resource/Common.robot
Resource    ${EXECDIR}/App/Resource/Features/UserManagement.robot
Resource    ${EXECDIR}/App/Resource/Pages/Home/Home.robot
Test Setup  Common.Begin Web Test
Test Teardown  Common.End Web Test

*** Test Cases ***     User        Password    Expected
Normal connection      auto_user   Indigo4!    OK 

Incomplete data        [Template]        Login should fail
                        unknownuser      ${EMPTY}             Invalid username or password.
                        ${EMPTY}         password             Invalid username or password.

*** Keywords ***
Login
    [Arguments]    ${user}    ${password}    ${expected}
    [Tags]    robot:continue-on-failure
        Navigate To Login Page
        Attempt Login With UserName Only   ${user}

Login should fail
    [Arguments]    ${user}    ${password}    ${expected}
    [Tags]    robot:continue-on-failure
        Navigate To Login Page
        Enter Credentials    ${user}    ${password}
        Click Log In Button
        LoginPage.Verify Login Error Message    ${expected}