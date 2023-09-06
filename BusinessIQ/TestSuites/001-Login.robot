*** Settings ***
#Test Tags         001-Login
Suite Setup       FrameworkKeywords.Suite Setup    ${SUITE NAME}   
Test Setup        FrameworkKeywords.Test Setup    ${TEST_NAME}
Test Teardown     FrameworkKeywords.End Test    ${TEST_NAME}    ${TestCaseDescription}

Library    String
Library    ListenerLibrary
Library    Collections
Resource   ../Resource/Common.robot
Library    ../Resource/FrameworkKeywords.py
Library    ../Resource/CommonBIQKeywords.py
Library    ../Resource/Utility.py
Library    ../Resource/MySettings_v2.py
Library    ../Resource/LoginPage.py 
Library    ../Resource/Login.py
*** Variables ***
${TestCaseDescription}    EMPTY
${testDataSet}    EMPTY
${ExecutionFlag}    EMPTY
${UserName}    EMPTY
${Subcode}    EMPTY
${BIQV2Default}    EMPTY
${Portfolio}    EMPTY
${ScoringModel}    EMPTY

*** Test Cases ***
    
003_Login_With_User_With_Security_Question
    [Documentation]    Login with a user hat has security question enabled
    Log To Console    \n${TEST_NAME}    \n${UserName}

004_Login_With_User_Locked_Account 
    [Documentation]    Login with a user with locked account
    Log To Console    \n${TEST_NAME}    \n${UserName}


