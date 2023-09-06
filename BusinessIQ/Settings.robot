# App configuration
*** Settings ***
Resource    ${EXECDIR}/Settings.robot

*** Variables ***

&{BASE_URL}  dev=https://stg-gateway.secure.experian.com/  uat=https://stg-gateway.secure.experian.com/  prod=https://stg-gateway.secure.experian.com/
${LOGIN_URL} =  BusinessIQ/login.html
${PATH_CSV} =  C:/Github/Robot/BusinessIQ/Data/Users.csv