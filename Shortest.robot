*** Settings ***
Library           pywhatkit
Library           OpenPyxlLibrary
Resource    resource.robot

*** Variables ***
${EXCEL_FILE}     contacts.xlsx

*** Test Cases ***
Send WhatsApp Messages
    ${data}=    Read Excel Data    ${EXCEL_FILE}
    FOR    ${row}    IN    @{data}
        ${mobile_number}=    Set Variable    ${row[0]}
        ${message}=    Set Variable    ${row[1]}
        Send WhatsApp Message    ${mobile_number}    ${message}
    END

*** Keywords ***
Read Excel Data
    [Arguments]    ${file_path}
    Open Workbook    ${file_path}
    ${sheet}=    Get Worksheet    Sheet1
    ${data}=    Get Worksheet Data    ${sheet}    start=2
    Close Workbook
    [Return]    ${data}

Send WhatsApp Message
    [Arguments]    ${mobile_number}    ${message}
    Sendwhatmsg Instantly    ${mobile_number}    ${message}    10
