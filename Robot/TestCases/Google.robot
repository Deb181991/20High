*** Settings ***
Documentation    This is my 1st robot script
Library    SeleniumLibrary
Library    DateTime
Resource    ../Resources/GoogleResource.robot

*** Test Cases ***

My first Robot TestCases Execution
     [Tags]    Smoke
     Given I open the Browser with URL
     Then Click on the I am lucky button
     Then Click on the About menu
     Then Click on the burining word
