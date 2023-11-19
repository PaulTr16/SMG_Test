*** Settings ***

# Resource     ../action/WikiAPI.robot
Library    ../../API/libraries/WikiAPILib.py

Library     XML
Library     DataDriver    file=../data/invalid_offset.csv     
...    dialect=unix 
...    delimiter=','


Test Template     Verify Response Invalid Offset Value
*** Keywords ***
Verify Response Invalid Offset Value
    [Arguments]     ${srsearch}     ${sroffset}
    ${response}    WikiAPILib.Test Wikipedia Search Api     ${srsearch}     ${sroffset}
    
    WikiAPILib.Verify Status Code    ${response.status_code}    200
    WikiAPILib.Verify Invalid Offset Value    ${sroffset}     ${response.content}

*** Test Cases ***

Testing     
   