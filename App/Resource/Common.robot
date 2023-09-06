*** Settings ***
Library    SeleniumLibrary
Library           ListenerLibrary
Resource   ${EXECDIR}/BusinessIQ/Settings.robot

*** Variables ***

*** Keywords ***
Begin Web Test
    Open Browser  about:blank  ${BROWSER}
    Maximize Browser Window
    Set Selenium Implicit Wait    10
    Set Selenium Timeout    10
    Set Selenium Speed    0.05 seconds

End Web Test
    Close All Browsers

Init Framework
 	Log  This Framework Start line is always executed, '${TEST NAME}'
