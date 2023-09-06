*** Settings ***
Documentation     Tests UI for Select Report page.
Suite Setup       Alerts Suite Setup
Test Setup        Alerts Test Setup
Test Teardown     Alerts Test Teardown
Suite Teardown    Login.Close Browser
Library    ../Resource/Login.py
Library    ../Resource/Utility.py
Library    ../Resource/DashboardV2.py
Library    ../Resource/CommonBIQKeywords.py
Library    ../Resource/Portfolio_v2.py
Library    ../Resource/Alerts_V2.py
*** Test Cases ***      
Can unset monitoring alerts from Account Details
    [Tags]    Medium    DECISIONIQ-406
    [Documentation]    Can change subscriber to a known value
    Navigate to account details by bin    798304266
    Click on alert me button on account details
    Uncheck all alerts
    Click on SAVE alert on account details
    Validate Alert Me button state is not    Monitored

Can Cancel edit monitoring alerts from Account Details
    [Tags]    Medium    
    [Documentation]    Can change subscriber to a known value
    Navigate to account details by bin    798304266
    Click on alert me button on account details
    Click on CANCEL alert on account details
    Validate alert dialog is closed

*** Keywords ***
Alerts Suite Setup
    Login.Suite Setup    ${SUITE_NAME}    
    Login To Biq    qa_admin

Alerts Test Setup
    Login.Test Setup    ${TEST_NAME}    export=${False}
    Open Portfolio Tab
    Login.Set Zoom Level Of Current Page To    70
Alerts Test Teardown
    Login.End Test    ${TEST_NAME}    ${TEST DOCUMENTATION}    close_session=${False}
