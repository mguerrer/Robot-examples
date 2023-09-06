*** Settings ***
Documentation  Demonstrate Login with POM and CSV
Resource    ${EXECDIR}/BusinessIQ/Resource/Common.robot
Resource    ${EXECDIR}/BusinessIQ/Resource/Features/UserManagement.robot



Test Setup  Begin Web Test
Test Teardown  End Web Test

*** Test Cases ***
Should see correct error messages with invalid logins
    [Documentation]     This shows how to get data from CSV file and execute failed logins waiting for a message
    @{InvalidLoginScenarios} =    Get CSV Data    ${PATH_CSV}
    Accept list of lists as single arg    ${InvalidLoginScenarios}
    Accept multiple args    @{InvalidLoginScenarios}

#    Login with List Of Credentials    ${InvalidLoginScenarios}  FAIL!!!
    FOR  ${LoginScenario}    IN    @{InvalidLoginScenarios}
        Log To Console    ${LoginScenario} 
        Navigate To Login Page
        Attempt Login With UserName And Password Without Validation    ${LoginScenario[0]}    ${LoginScenario[1]}
        Verify Login Page Error Message  ${LoginScenario[2]}
    END

*** Keywords ***
Accept list of lists as single arg
    [Arguments]         ${arguments}
    length should be    ${arguments}       3
    length should be    ${arguments[0]}    3
    length should be    ${arguments[1]}    3

Accept multiple args
    [Arguments]         @{arguments}
    length should be    ${arguments}       3
    length should be    ${arguments[0]}    3
    length should be    ${arguments[1]}    3

Login with List Of Credentials
    [Arguments]  ${LoginScenarios}
    FOR  ${LoginScenario}  IN  ${LoginScenarios}
        run keyword and continue on failure  Navigate To Login Page
        run keyword and continue on failure  Attempt Login With UserName Only    ${LoginScenario[0]}
        run keyword and continue on failure  Verify Login Page Error Message  ${LoginScenario[2]}
    END