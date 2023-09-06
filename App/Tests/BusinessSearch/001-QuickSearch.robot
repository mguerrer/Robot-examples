***Settings***
Library           DataDriver    dialect=excel    file=../../Data/001-QuickSearch.csv
Resource          ${EXECDIR}/App/Resource/Features/BusinessSearch.robot
Resource          ${EXECDIR}/App/Resource/Features/UserManagement.robot
Test Template     Quick Search
Test Setup        Common.Begin Web Test
Test Teardown     Common.End Web Test

*** Test Case ***
Quick Search with Name City State ZIP and BIN

*** Keywords ***
Quick Search
    [Arguments]    ${Name}    ${City}    ${State}    ${ZIP}    ${BIN}
    # Arrange
    Navigate To Login Page
    Attempt Login With UserName Only     auto_user
    Verify Page Loaded
    # Act
    Set Business Name    ${Name}
    Set City    ${City}  
    Set State    ${State} 
    Set Zip Code    ${ZIP} 
    Set Bin    ${BIN}
    ${nrecords}=    Count Results
    Log    Count Results= ${nrecords}
    # Assert