*** Settings ***
Documentation    This is my 1st robot script
Library    RPA.Browser.Selenium    auto_close=${FALSE}
Library    SeleniumLibrary
Library    DateTime
Library    SeleniumLibrary
Variables    ../PageObjects/Google.py
*** Variables ***
${chrome}   chrome
${options1}    options=add_experimental_option("detach", True)
${options2}    options=add_experimental_option("excludeSwitches", ["enable-automation"])
*** Keywords ***
I open the Browser with URL
#    [Arguments]    ${URL}    ${chrome}
    open browser    ${URL}    ${chrome}    options=add_experimental_option("excludeSwitches", ["enable-automation"])
    maximize browser window
    set selenium implicit wait    5

Click on the I am lucky button
     click button    ${FeelingLucky}

Click on the About menu
     click element   ${About}

Click on the burining word
     click element   ${burrning}
