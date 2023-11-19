*** Settings ***

Library    ../../libraries/wiki/WikiMainPage.py
Library    SeleniumLibrary

*** Keywords ***


   
Main Page Input Search Text
    [Arguments]     ${text}
    WikiMainPage.Go To Main Page
    WikiMainPage.Main Page Input Search Value And Go To Search Page   ${text} 
    Sleep    2 
#    WikiMainPage.Testing Click Xpath

Click Search Button To Go To Search Page
    WikiMainPage.Go To Main Page
    WikiMainPage.Main Page Click Search Bnt
    



