import requests
from RequestsLibrary import RequestsLibrary
from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.Collections import Collections
from robot.api import logger
import json




class WikiAPILib(object):
    def __init__(self):
        self.builtIn=BuiltIn()
        self.collection=Collections()

    @property
    def url(self):
        return "https://en.wikipedia.org/w/api.php"

    def test_wikipedia_search_api(self, search_query, offset):
        params = {
            "action": "query",
            "format": "json",
            "list": "search",
            "continue": "-||",
            "formatversion": 2,
            "srsearch": search_query,
            "sroffset": offset,
        }
        response= requests.get(url=self.url,params=params)
        #status_code = response.status_code()
        return response
    

    def verify_status_code(self,status_code,expected):
        print (f"Status_code: {status_code}")
        print (f"Expectation Status_code: {expected}")
        self.builtIn.should_be_equal_as_integers(status_code,expected)


    def verify_invalid_offset_value(self,offset,respone):
        respone=json.loads(respone.decode('utf-8'))
        #print(respone)
        #offset=str(offset)
        print(offset)
        if not offset or not offset.lstrip("-").isdigit():
            code= respone["error"]["code"]
            self.builtIn.should_be_equal_as_strings(code,
                "badinteger"
            )
        else:
            offset=int(offset)
            if offset>=10000:
                code= respone["error"]["code"]
                self.builtIn.should_be_equal_as_strings(code,
                "cirrussearch-offset-too-large"
            )
            elif offset<0:
                warnings= respone["warnings"]["search"]["warnings"]
                self.builtIn.should_be_equal_as_strings(warnings,
                    f"The value \"{offset}\" for parameter \"sroffset\" must be no less than 0.")
                    
    def verify_invalid_search_value(self,search_value,respone):
        respone=json.loads(respone.decode('utf-8'))
        if not search_value:
            code= respone["error"]["code"]
            self.builtIn.should_be_equal_as_strings(
                code,
                "missingparam"
            )
            info=respone["error"]["info"]
            self.builtIn.should_be_equal_as_strings(
                info,
                "The \"srsearch\" parameter must be set."
            )
        else:
            batchcomplete=respone["batchcomplete"]
            totalhits=respone["query"]["searchinfo"]["totalhits"]
            search =respone["query"]["search"]

            self.builtIn.should_be_true(batchcomplete)
            self.builtIn.should_be_equal_as_integers(totalhits,0)
            self.builtIn.should_be_empty(search)   

    
    
    def verify_search_successfully(self,offset,search_value,respone):
        respone=json.loads(respone.decode('utf-8'))
        
        batchcomplete=respone["batchcomplete"]
        totalhits=respone["query"]["searchinfo"]["totalhits"]
        search =respone["query"]["search"]
        
        self.builtIn.should_be_true(batchcomplete)
        self.builtIn.should_not_be_equal_as_integers(totalhits,0)
        self.builtIn.should_not_be_empty(search)
        
        if "continue" in respone:
            conti=respone["continue"]
            sroffset=conti["sroffset"]
            sroffset_value = int(offset)+10
            self.builtIn.should_be_equal_as_integers(sroffset,sroffset_value)


            


                




 


    
    

        

