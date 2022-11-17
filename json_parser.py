from parser import Parser
from json_types import *
# Mapping of JSON Data to python objects

'''
    Objects: JSONObjects have the following structure:
    JSONObject({
        JSONObjectKey(key_name): <any_json_element>,
        ...
    })
    This will be mapped to python dicts with the keys being JSONObjectKey and the value being the value inside the any_json_element value.

    Arrays: JSONArrays have the following structure:
    JSONArray([<any_json_element>, ...])
    This will be mapped to python lists.

    Every other element will be mapped to it's corresponding named equivalent in python, will null being mapped to None.
'''

class JSONParser(Parser):
    def __init__(self, token) -> None:
        self.root_token = token
        super().__init__()
    
    def parse_object(self, token) -> dict:
        return_object = {}
        if token.content is None:
            return {}
        print(token)
        for key, value in token.content.items():
            return_object[key.content] = self.parse_element(value)
        return return_object
    
    def parse_array(self, token) -> list:
        return_array = []
        if token.content is None:
            return []
        for item in token.content:
            return_array.append(self.parse_element(item))
        return return_array
        
    def parse_false(self) -> bool:
        return False
    
    def parse_true(self) -> bool:
        return True
    
    def parse_null(self) -> None:
        return None
        
    def parse_number(self, token) -> float:
        return float(token.content)

    def parse_string(self, token) -> str:
        return token.content

    def parse_value(self, token):
        return self.parse_element(token.content)
    
    def parse_element(self, token):
        if type(token).__name__ == 'JSONObject':
            return self.parse_object(token)
        elif type(token).__name__ == 'JSONObjectKey':
            return self.parse_string(token)
        elif type(token).__name__ == 'JSONArray':
            return self.parse_array(token)
        elif type(token).__name__ == 'JSONValue':
            return self.parse_value(token)
        elif type(token).__name__ == 'JSONString':
            return self.parse_string(token)
        elif type(token).__name__ == 'JSONNumber':
            return self.parse_number(token)
        elif type(token).__name__ == 'JSONNull':
            return self.parse_null()
        elif type(token).__name__ == 'JSONTrue':
            return self.parse_true()
        elif type(token).__name__ == 'JSONFalse':
            return self.parse_false()
        else:
            raise Exception('Tokenizer/Parser Error: Unknown token encountered')

    def parse(self):
        return self.parse_element(self.root_token)