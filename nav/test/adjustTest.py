import unittest
import nav.adjust as nav
from urllib import urlencode
import httplib
import json
from cmath import sqrt

class adjustTest(unittest.TestCase):


    def setUp(self):
        self.inputDictionary = {}
        self.errorKey = "error"
        self.solutionKey = "probability"
        self.BX_PATH = '/nav?'
        self.BX_PORT = 5000
        self.BX_URL = 'localhost'
#         self.BX_PORT = 5000
#         self.BX_URL = 'www.ibmcloud.com'

    def tearDown(self):
        self.inputDictionary = {}

    def setParm(self, key, value):
        self.inputDictionary[key] = value
        
    def microservice(self):
        try:
            theParm = urlencode(self.inputDictionary)
            theConnection = httplib.HTTPConnection(self.BX_URL, self.BX_PORT)
            theConnection.request("GET", self.BX_PATH + theParm)
            theStringResponse = theConnection.getresponse().read()
            return theStringResponse
        except Exception as e:
            return "error encountered during transaction"
        
    def string2dict(self, httpResponse):
        '''Convert JSON string to dictionary'''
        result = {}
        try:
            jsonString = httpResponse.replace("'", "\"")
            unicodeDictionary = json.loads(jsonString)
            for element in unicodeDictionary:
                if(isinstance(unicodeDictionary[element],unicode)):
                    result[str(element)] = str(unicodeDictionary[element])
                else:
                    result[str(element)] = unicodeDictionary[element]
        except Exception as e:
            result['diagnostic'] = str(e)
        return result





# 500 adjust
#    Analysis
#        inputs
#            observation -> string, mandatory, validated
#            height -> string, not mandatory, validated
#            temperature -> string, not mandatory, validated
#            pressure -> string, not mandatory, validated
#            horizon -> string, not mandatory, validated
#        outputs
#            altitude -> string, mandatory, validated
#            observation -> string, mandatory, validated
#            height -> string, not mandatory, validated
#            temperature -> string, not mandatory, validated
#            pressure -> string, not mandatory, validated
#            horizon -> string, not mandatory, validated
#    Happy path analysis
#        strategy: exercise code from simple to hard
#        1) return a constant
#        2) return a dictionary
#        3) 






#     def test500_010ShouldVerifyCallToAdjust(self):
#         expectedResult = 1.0
#         actualResult = nav.adjust()
#         self.assertEquals(expectedResult, actualResult)
        
#     def test500_020ShouldReturnDictionary(self):
#         values = self.setParm('op','adjust')
#         expectedResult = values
#         actualResult = nav.adjust(values)
#         self.assertEquals(expectedResult, actualResult)

    def test500_030CalculateDip(self):
#        values = self.setParm('op','adjust')
        self.setParm('height','33')
        height = int(self['height'])
        expectedResult = -0.97 * sqrt(height) / 60
        actualResult = 1
        self.assertEquals(expectedResult, actualResult)       
    
    
    
    
    
    
    
    
