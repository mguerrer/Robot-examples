# Suite init settings
*** Setting ***
Documentation     Setting metadata for test suite directory
Suite Setup       Init Suite    
Suite Teardown    Teardown Suite
#Test Tags         BIQ_Suite

*** Variables ***
${BIQ_PAGES_DIR}

*** Keywords ***
Init Suite
    Log To Console    Starting suite
    Set Suite Variable    ${BIQ_PAGES_DIR}    ${EXECDIR}/BusinessIQ/Resource/Pages

Teardown Suite
    Log To Console    Teardown suite
    