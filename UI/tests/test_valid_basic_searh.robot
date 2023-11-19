*** Settings ***

Resource     ../resources/actions/Wiki.BasePage.robot
Resource    ../resources/actions/Wiki.MainPage.robot
Resource     ../resources/actions/Wiki.SearchPage.robot



Suite Setup      Wiki.BasePage.Open Testing Browser



# Suite Teardown     Wiki.BasePage.Close All Browsers


*** Test Cases ***

Verify UI 
    Wiki.MainPage.Click Search Button To Go To Search Page
    Wiki.SearchPage.Verify Search Page UI Contain All Tab

Verify Can Access Search For Page Containing Text from MainPage
    Wiki.MainPage.Main Page Input Search Text     Software Testing
    ${value}     Wiki.SearchPage.Verify Search Result    
    Should Be Equal    ${value}     ${True}
