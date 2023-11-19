*** Settings ***

Library    ../../libraries/wiki/WikiBasePage.py
Library     SeleniumLibrary

*** Keywords ***

Open Testing Browser
    WikiBasePage.Open Web Browser

Close Browser
    WikiBasePage.Close Browser

Close All Browsers
    WikiBasePage.Close All Browsers