***Settings***
Library    RequestsLibrary
#Test Tags  Smoke
Test Setup    Get Login Page 
*** Variables ***
${biqUrl}=    https://stg-gateway.secure.experian.com/BusinessIQ/login.html
${legalTermsUrl}=    http://www.experian.com/corporate/legalterms.html
${response}

*** Test Cases ***
Quick Check Login Page
    Request Should Be Successful    ${biqUrl}

Quick Check Login Page Legal Terms 
    Should Contain    ${response.text}    ${legalTermsUrl}
    ${legalTermsPage}=    GET  ${legalTermsUrl} 
    Should Contain    ${legalTermsPage.text}    Please read the following information carefully before using this site.

*** Keywords ***
Get Login Page
    ${resp}=    GET  ${biqUrl} 
    Set Global Variable    ${response}    ${resp}
    