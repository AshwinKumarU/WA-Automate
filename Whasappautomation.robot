*** Settings ***
Library    SeleniumLibrary
Library    ExcelUtils.py
Library    Collections

*** Variables ***
${EXCEL_FILE}    ./testWA.xlsx
${WHATSAPP_URL}  https://web.whatsapp.com/
${TIMEOUT}       160s
${ChatTitle}    /html/body/div[1]/div/div/div[2]/div[3]/header/header/div/div[1]/h1

*** Test Cases ***
Send WhatsApp Messages
    [Documentation]    Automate sending WhatsApp messages using data from Excel.
    Open Browser And Maximize Window
    Wait Until QR Code Scanned
    Send Messages From Excel

*** Keywords ***
Open Browser And Maximize Window
    Open Browser    ${WHATSAPP_URL}    Chrome
    Maximize Browser Window
    Set Selenium Timeout    ${TIMEOUT}

Wait Until QR Code Scanned
    [Documentation]    Wait until WhatsApp Web is fully loaded.
    Wait Until Page Contains Element    ${ChatTitle}    ${TIMEOUT}

Send Messages From Excel
    ${contacts} =    Read Contacts    ${EXCEL_FILE}
    FOR    ${contact}    IN    @{contacts}
        Log    Processing contact: ${contact['Phone']}
        Search And Send Message    ${contact['Phone']}    ${contact['Message']}
    END

Search And Send Message
    [Arguments]    ${phone}    ${message}
    Click Element    //*[@title='New chat']
    Wait Until Page Contains Element    //*[@contenteditable='true']    ${TIMEOUT}
    Input Text    //*[@contenteditable='true']    ${phone}
    Sleep    3s    # Allow some time for search to complete

    ${exists} =    Run Keyword And Return Status    Element Should Be Visible    (//span[contains(text(), '${phone}')])[1]    ${TIMEOUT}
    IF    ${exists}
        Log    Contact found: ${phone}
        Click Element    (//span[contains(text(), '${phone}')])[1]
        Wait Until Page Contains Element    //*[@contenteditable='true']    ${TIMEOUT}
        Input Text    //*[@contenteditable='true']    ${message}
        Press Keys    //*[@contenteditable='true']    ENTER
    ELSE
        Log    ${phone} does not exist
        Click Element    //*[@aria-label='Back']
    END
    Sleep    5s    # Ensure message is sent properly
