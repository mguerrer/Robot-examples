*** Settings ***
Library    Collections
Library    c:/Github/Robot-examples/App/Api/mars-photo-api.py    WITH NAME    MarsPhotoAPI

*** Test Cases ***
Obtener Fotos Por Sol
    ${result}=    MarsPhotoAPI.Get Photos By Sol    curiosity    1000
    Dictionary Should Contain Key    ${result}    photos

Obtener Fotos Por Fecha Terrestre
    ${result}=    MarsPhotoAPI.Get Photos By Earth Date    curiosity    2015-06-03
    Dictionary Should Contain Key    ${result}    photos

Obtener Fotos Más Recientes
    ${result}=    MarsPhotoAPI.Get Latest Photos    curiosity
    Dictionary Should Contain Key    ${result}    latest_photos

Obtener Manifiesto De Misión
    ${result}=    MarsPhotoAPI.Get Manifest    curiosity
    Dictionary Should Contain Key    ${result}    photo_manifest