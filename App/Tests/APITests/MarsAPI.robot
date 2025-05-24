*** Settings ***
Library    Collections
Library    c:/Github/Robot-examples/App/Api/mars-photo-api.py    WITH NAME    MarsPhotoAPI
Suite Setup    Log    Iniciando pruebas de MarsPhotoAPI

*** Variables ***
${ROVER_VALIDO}        curiosity
${ROVER_INVALIDO}      fake_rover
${SOL_VALIDO}          1000
${SOL_INVALIDO}        -1
${FECHA_VALIDA}        2015-06-03
${FECHA_INVALIDA}      1990-01-01

*** Test Cases ***
Obtener Fotos Por Sol - Escenarios
    [Template]    Obtener Fotos Por Sol Template
    ${ROVER_VALIDO}    ${SOL_VALIDO}      photos         True
    ${ROVER_VALIDO}    ${SOL_INVALIDO}    photos         False
    ${ROVER_INVALIDO}  ${SOL_VALIDO}      photos         False

Obtener Fotos Por Fecha Terrestre - Escenarios
    [Template]    Obtener Fotos Por Fecha Terrestre Template
    ${ROVER_VALIDO}    ${FECHA_VALIDA}      photos         True
    ${ROVER_VALIDO}    ${FECHA_INVALIDA}    photos         False
    ${ROVER_INVALIDO}  ${FECHA_VALIDA}      photos         False

Obtener Fotos Más Recientes - Escenarios
    [Template]    Obtener Fotos Más Recientes Template
    ${ROVER_VALIDO}    latest_photos    True
    ${ROVER_INVALIDO}  latest_photos    False

Obtener Manifiesto De Misión - Escenarios
    [Template]    Obtener Manifiesto De Misión Template
    ${ROVER_VALIDO}    photo_manifest    True
    ${ROVER_INVALIDO}  photo_manifest    False

*** Keywords ***
Obtener Fotos Por Sol Template
    [Arguments]    ${rover}    ${sol}    ${key}    ${espera_exito}
    ${resultado}=    Run Keyword And Ignore Error    MarsPhotoAPI.Get Photos By Sol    ${rover}    ${sol}
    ${status}=    Set Variable    ${resultado}[0]
    ${data}=      Set Variable    ${resultado}[1]
    Run Keyword If    '${espera_exito}'=='True'    Dictionary Should Contain Key    ${data}    ${key}
    ...    ELSE    Dictionary Should Not Contain Key    ${data}    ${key}

Obtener Fotos Por Fecha Terrestre Template
    [Arguments]    ${rover}    ${fecha}    ${key}    ${espera_exito}
    ${resultado}=    Run Keyword And Ignore Error    MarsPhotoAPI.Get Photos By Earth Date    ${rover}    ${fecha}
    ${status}=    Set Variable    ${resultado}[0]
    ${data}=      Set Variable    ${resultado}[1]
    Run Keyword If    '${espera_exito}'=='True'    Dictionary Should Contain Key    ${data}    ${key}
    ...    ELSE    Should Be Equal As Strings    ${status}    FAIL

Obtener Fotos Más Recientes Template
    [Arguments]    ${rover}    ${key}    ${espera_exito}
    ${resultado}=    Run Keyword And Ignore Error    MarsPhotoAPI.Get Latest Photos    ${rover}
    ${status}=    Set Variable    ${resultado}[0]
    ${data}=      Set Variable    ${resultado}[1]
    Run Keyword If    '${espera_exito}'=='True'    Dictionary Should Contain Key    ${data}    ${key}
    ...    ELSE    Should Be Equal As Strings    ${status}    FAIL

Obtener Manifiesto De Misión Template
    [Arguments]    ${rover}    ${key}    ${espera_exito}
    ${resultado}=    Run Keyword And Ignore Error    MarsPhotoAPI.Get Manifest    ${rover}
    ${status}=    Set Variable    ${resultado}[0]
    ${data}=      Set Variable    ${resultado}[1]
    Run Keyword If    '${espera_exito}'=='True'    Dictionary Should Contain Key    ${data}    ${key}
    ...    ELSE    Should Be Equal As Strings    ${status}    FAIL