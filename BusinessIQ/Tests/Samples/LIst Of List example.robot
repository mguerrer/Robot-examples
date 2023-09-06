*** Variables ***
@{numbers}    1    2    3
@{letters}    a    b    c    d
@{listoflists}    ${numbers}    ${letters}

*** Keywords ***
Accept list of lists as single arg
    [Arguments]         ${arguments}
    length should be    ${arguments}       2
    length should be    ${arguments[0]}    3
    length should be    ${arguments[1]}    4

Accept multiple args
    [Arguments]         @{arguments}
    length should be    ${arguments}       2
    length should be    ${arguments[0]}    3
    length should be    ${arguments[1]}    4


*** Test cases ***
Pass list of lists as single argument
    Accept list of lists as single arg       ${listoflists}

Pass list of lists as multiple arguments
    Accept multiple args    @{listoflists}
    Accept multiple args    ${numbers}    ${letters}