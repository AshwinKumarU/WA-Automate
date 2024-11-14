*** Settings ***
Documentation     A resource file with reusable keywords and variables.
...
...               The system specific keywords created here form our own
...               domain specific language. They utilize keywords provided
...               by the imported SeleniumLibrary.
Library           SeleniumLibrary
Library          WAnumberCheck.py

*** Variables ***
${SERVER}
${BROWSER}    chrome
${DELAY}    3
${VALID USER}    /html/body/div[1]/div/div/div[2]/div[2]/div[1]/span/div/span/div/div[2]/div[2]
${password}    1234
${LOGIN URL}    https://web.whatsapp.com     
# ${LOGIN URL 2}    https://web.whatsapp.com/send/?phone=918778000401&text=I%27m+interested+in+your+car+for+sale&type=phone_number&app_absent=0      
# https://wa.me/918778000401?text=Hello!%20I'm%20reaching%20out%20regarding%20your%20recent%20inquiry.%20For%20more%20information,%20please%20visit%20https%3A%2F%2Famura.ai%2F
# ${WELCOME URL}    https://dbx92nph6l84n.cloudfront.net/home
${ERROR URL}      http://${SERVER}/error.html
${ValidationText}    /html/body/div[1]/div/div/div[2]/div[3]/div[1]/div/div/div[2]/div[2]/canvas
${OTP}    /html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div[3]/div/div/h4[2]/a/span
${My_List}    /html/body/div[1]/div/div/div[2]/div[3]/div[1]/div/div/div[2]/div[2]/canvas
${ChatTitle}    /html/body/div[1]/div/div/div[2]/div[3]/header/header/div/div[1]/h1
${EXCEL_FILE_PATH}    ./testWA.xlsx
${SearchUser}    /html/body/div[1]/div/div/div[2]/div[2]/div[1]/span/div/span/div/div[1]/div[2]/div[2]/div
${SearchPlusIcon}    /html/body/div[1]/div/div/div[2]/div[3]/header/header/div/span/div/span/div[1]/div/span
${RESULT_CARD}    /html/body/div[1]/div/div/div[2]/div[2]/div[1]/span/div/span/div/div[2]/div/div/div/div[2]
${NO_RESULT_TEXT}    /html/body/div[1]/div/div/div[2]/div[2]/div[1]/span/div/span/div/div[2]/div/div
${TextInputBox}    /html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p

*** Keywords ***

Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}
    # Login Page Should Be Open

# Login Page Should Be Open
#     Title Should Be    Amura PMS

# Go To Login Page
#     Go To    ${LOGIN URL}
#     Login Page Should Be Open

# Input Username
#     [Arguments]    ${username}
#     Input Text    id:${Mobile number}    ${username}

# Input Password
#     [Arguments]    ${password}
#     Input Text    id:${OTP}    ${password}

# Submit Credentials
#     Click Button    Verify

# Welcome Page Should Be Open
#     Location Should Be    ${WELCOME URL}
#     Title Should Be    Amura PMS


# Login
    # Open Browser To Login Page
    # Set Browser Implicit Wait    100
    # Wait Until Element Is Visible    Xpath:${ValidationText}
    # Set Browser Implicit Wait    200
    # Wait Until Element Is Visible    Xpath:${ChatTitle}

# Search And Verify Mobile Number
#     [Arguments]    ${mobile_number}
#     Click Element    XPath:${SEARCH_USER}
#     Press Keys    None    ${mobile_number}
#     Click Element    ${RESULT_CARD}  # Trigger search, if required

#     Wait Until Element Is Visible    ${CHAT_TITLE}    timeout=10s  # Wait for the result to appear

#     ${card_present}=    Run Keyword And Return Status    Page Should Contain Element    ${RESULT_CARD}
#     ${no_result_present}=    Run Keyword And Return Status    Page Should Contain Element    ${NO_RESULT_TEXT}

#     Run Keyword If    ${card_present}    Perform Actions For Mobile Number    ${mobile_number}
#     ...    ELSE IF    ${no_result_present}    Mark No WhatsApp For Number    ${mobile_number}
#     ...    ELSE    Log    Unexpected result for ${mobile_number}

# Perform Actions For Mobile Number
#     [Arguments]    ${mobile_number}
#     Log    Performed actions for mobile number: ${mobile_number}
#     # Add any further actions, such as sending messages or interacting with elements here.

# Mark No WhatsApp For Number
#     [Arguments]    ${mobile_number}
#     Log No Whatsapp    ${mobile_number}    ${EXCEL_FILE_PATH}
#     Log    Marked ${mobile_number} as "No WhatsApp"

Send Message 
    


