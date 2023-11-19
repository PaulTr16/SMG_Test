*** Settings ***

Library     ../../libraries/wiki/WikiSearchPage.py
Library     SeleniumLibrary

*** Keywords ***

Search Page Contain Text
    [Arguments]     ${text}
    WikiSearchPage.Go To Search Page
    WikiSearchPage.Search Page Input Search Value     ${text}
    WikiSearchPage.Search Page Click Search Bnt        

Verify No Result Search
    [Arguments]    ${text}
    WikiSearchPage.Verify No Result    ${text}

Verify Search Page UI Contain All Tab
    WikiSearchPage.Go To Search Page
    WikiSearchPage.UI Search Page

Verify Search Result
    ${value}=    Run Keyword And Return Status       WikiSearchPage.Page Contain Result Container  
    Log To Console     ${value}
    [return]     ${value}   
    


