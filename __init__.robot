# Suite init settings
*** Settings ***
Documentation     Setting metadata for test suite directory
Library           ListenerLibrary
Suite Setup       Init Suite    
Suite Teardown    Teardown Suite

*** Keywords ***
Init Suite
    Log To Console    Starting suite
    Register Start Test Listener    Init Framework

Teardown Suite
    Log To Console    Teardown suite