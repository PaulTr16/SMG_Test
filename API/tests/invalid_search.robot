*** Settings ***

# Resource     ../action/WikiAPI.robot
Library    ../../API/libraries/WikiAPILib.py

Library     XML
Library     DataDriver    file=../data/invalid_search.csv     
...    dialect=unix 
...    delimiter=','

Test Template     Verify Response Invalid Search Value
*** Keywords ***
Verify Response Invalid Search Value
    [Arguments]     ${srsearch}     ${sroffset}
    ${response}    WikiAPILib.Test Wikipedia Search Api     ${srsearch}     ${sroffset}
    
    WikiAPILib.Verify Status Code    ${response.status_code}    200
    WikiAPILib.Verify Invalid Search Value     ${srsearch}     ${response.content}    
*** Test Cases ***

Testing   