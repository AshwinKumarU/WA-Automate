*** Settings ***
Documentation     Verify the default card view of user cards
# Suite Setup    Login
Library    ExcelLibrary.py
Library          WAnumberCheck.py
Library           Collections
Resource    resource.robot
Library           pywhatkit
Library           OpenPyxlLibrary
# Resource     MyListCard.robot
# Resource    ../utils.robot
*** Test Cases ***
# Click on the Alert open URL
#     Handle Alert    action=ACCEPT    
    # Get Selenium Implicit Wait(1000)
    
    
Login
    Open Browser To Login Page
    Set Browser Implicit Wait    10
    # Wait Until Element Is Visible    Xpath:${ValidationText}
    Set Browser Implicit Wait    2
    # Wait Until Element Is Visible    Xpath:${ChatTitle}

Wait until title is Visible and input text
    # Load Excel    ${EXCEL_FILE_PATH}
    # ${mobile_numbers}=    Get Mobile Numbers    ${EXCEL_FILE_PATH}
    # FOR    ${mobile_number}    IN    @{mobile_numbers}
    Click Element    Xpath:${SearchPlusIcon}
    Click Element    XPath:${SEARCH_USER}
    Press Keys    None    8790425929
    ${is_present}=    Run Keyword And Return Status    Element Should Be Visible    xpath=/html/body/div[1]/div/div/div[2]/div[2]/div[1]/span/div/span/div/div[2]/div[2]
    Run Keyword If    ${is_present}    Click Element    Xpath:${VALID USER}
    ...    ELSE    Handle Element Not Found
    Click Element    Xpath:${VALID USER}
    # Click Element    XPath:${TextInputBox}
    Input Text    ${TextInputBox}    Some random test 2
    Click Element    Xpath:/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span/div/div[2]/div[2]/button
        
    # END

    #     Search And Verify Mobile Number    ${mobile_number}
    # END
    # [Teardown]    Close Browser

*** Keywords ***
# Get Mobile Numbers From Excel
#     [Arguments]    ${EXCEL_FILE_PATH}
#     ${mobile_numbers}=    Get Mobile Numbers    ${EXCEL_FILE_PATH}
#     [Return]    ${mobile_numbers}
