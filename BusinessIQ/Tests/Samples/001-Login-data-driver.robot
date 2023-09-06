***Settings***
Library           DataDriver    dialect=excel    file=../../Data/001-Login-data-driver.csv
Test Template     Login

*** Test Case ***
Login with user username and priority and subcode portfolio and scoringModel

***** *Keywords* *****
login
    [Arguments]    ${username}    ${priority}	${subcode}	${portfolio}	${scoringModel}
    Log To Console    \nUser=${username}
    Log To Console    Priority=${priority}
    Log To Console    Model=${scoringModel}