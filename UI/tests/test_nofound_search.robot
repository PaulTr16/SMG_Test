*** Settings ***

Resource     ../resources/actions/Wiki.BasePage.robot
Resource    ../resources/actions/Wiki.MainPage.robot
Resource     ../resources/actions/Wiki.SearchPage.robot

Library     XML
Library     DataDriver    file=../resources/data/testing_data/UI_testing_data/nofound.csv     
...    dialect=unix 
...    delimiter=','

Suite Setup    Run Keywords    
...    Wiki.BasePage.Open Testing Browser
...    AND    Wiki.MainPage.Click Search Button To Go To Search Page


Suite Teardown     Wiki.BasePage.Close All Browsers


Test Template     Verify Wikipedia Return No Found Successfully

*** Keywords ***
Verify Wikipedia Return No Found Successfully
    [arguments]                          ${text} 
    Wiki.SearchPage.Search Page Contain Text     ${text}
    Wiki.SearchPage.Verify No Result Search     ${text}

*** Test Cases ***

Demo Testing No Found    
   

    
    



