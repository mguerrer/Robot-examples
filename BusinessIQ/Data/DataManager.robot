*** Settings ***
Documentation  Use this layer to get data from external files
Library    ../CustomLibs/Csv.py
Library  ../CustomLibs/UserDetails.py

*** Keywords ***
Get CSV Data
    [Arguments]  ${FilePath}
    ${Data} =  read csv file  ${FilePath}
    [Return]  ${Data}

Get User Password
    [Arguments]    ${username}
    ${password}    UserDetails.Get Password    ${username}
    [Return]    ${password}