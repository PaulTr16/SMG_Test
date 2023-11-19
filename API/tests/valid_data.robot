*** Settings ***

# Resource     ../action/WikiAPI.robot
Library    ../../API/libraries/WikiAPILib.py

Library     XML
Library     DataDriver    file=../data/valid.csv     
...    dialect=unix 
...    delimiter=','


Test Template     Verify Response valid Value
*** Keywords ***
Verify Response valid Value
    [Arguments]     ${srsearch}     ${sroffset}
    ${response}    WikiAPILib.Test Wikipedia Search Api     ${srsearch}     ${sroffset}
    
    WikiAPILib.Verify Status Code    ${response.status_code}    200
    WikiAPILib.Verify Search Successfully    ${sroffset}   ${srsearch}   ${response.content}

*** Test Cases ***

Testing 