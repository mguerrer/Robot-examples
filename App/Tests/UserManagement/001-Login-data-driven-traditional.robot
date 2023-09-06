*** Settings ***
Documentation  Demonstrate Login with POM
Resource    ${EXECDIR}/BusinessIQ/Resource/Common.robot
Resource    ${EXECDIR}/BusinessIQ/Resource/Features/UserManagement.robot

Suite Setup    DataCsv

Test Setup  Begin Web Test
Test Teardown  End Web Test

*** Variables ***
${Scenarios}   

*** Test Cases ***
Invalid login scenarios should display correct error messages
    [Template]  Test Multiple Login Scenarios
        fake1    pwd1    Sign in failed!

*** Keywords ***
Test Multiple Login Scenarios
    [Arguments]  @{Scenarios}
    Navigate To Login Page
    Attempt Login With Credentials Without Validation  ${Scenarios}
    Verify Login Page Error Message  ${Scenarios[2]}

DataCsv
    ${list}=    Get CSV Data    ${PATH_CSV}
    Set Global Variable    ${Scenarios}   ${list}     
