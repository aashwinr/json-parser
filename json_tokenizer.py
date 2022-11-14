from tokenizer import Tokenizer
from incorrect_character import IncorrectCharacterError, IncorrectIdentifierError
from json_types import *

class TokenizerHelpers:
    def isdigit(digit):
        return digit in ['0','1','2','3','4','5','6','7','8','9']

class JSON_Tokenizer(Tokenizer):
    def __init__(self, contents):
        super().__init__(contents)
    
    def tokenize_element(self) -> JSONValue:
        self.consume_whitespace()
        return_value = self.tokenize_value()
        self.consume_whitespace()
        return return_value
    
    def tokenize_value(self) -> JSONValue:
        next_element = self.next()
        if next_element == '{':
            return_json_value = self.tokenize_object()
        elif next_element == '[':
            return_json_value = self.tokenize_array()
        elif next_element == '"':
            return_json_value = self.tokenize_string()
        elif next_element in ['0','1','2','3','4','5','6','7','8','9', '-']:
            return_json_value = self.tokenize_number()
        elif next_element == 't':
            if self.next_n(4) == 'true':
                return_json_value = self.tokenize_true()
            else:
                raise IncorrectIdentifierError()
        elif next_element == 'f':
            if self.next_n(5) == 'false':
                return_json_value = self.tokenize_false()
            else:
                raise IncorrectIdentifierError()
        elif next_element == 'n':
            if self.next_n(4) == 'null':
                return_json_value = self.tokenize_null()
            else:
                raise IncorrectIdentifierError()
        else:
            raise IncorrectIdentifierError()
        self.consume_whitespace()
        return return_json_value
    
    def tokenize_object(self) -> JSONObject:
        self.consume()
        self.consume_whitespace()
        if self.next() == '}':
            self.consume()
            return JSONObject({})
        else:
            members = self.tokenize_members()
            # consuming the '}'
            self.consume()
            return JSONObject(members)
    
    def tokenize_members(self) -> dict:
        first_member = self.tokenize_member()
        members = {}
        members[first_member[0]] = first_member[1]
        while self.next() == ',':
            # for consuming the ','
            self.consume()
            member = self.tokenize_member()
            members[member[0]] = member[1]
        return members
    
    def tokenize_member(self) -> tuple((JSONString, JSONValue)):
        self.consume_whitespace()
        key = self.tokenize_string()
        self.consume_whitespace()
        # for consuming the ':' in key:value
        self.consume()
        value = self.tokenize_element()
        return (key, value)
    
    def tokenize_array(self) -> JSONArray:
        # for consuming the '['
        self.consume()
        self.consume_whitespace()
        if self.next() == ']':
            self.consume()
            return JSONArray([])
        values = self.tokenize_elements()
        return_array = JSONArray(values)
        # for consuming ']'
        self.consume()
        return return_array
    
    def tokenize_elements(self): #-> list(JSONValue):
        element = self.tokenize_element()
        if self.next() == ',':
            self.consume()
            return [element, self.tokenize_elements()]
        return element
    
    def tokenize_string(self) -> JSONString:
        # for consuming the '"'
        self.consume()
        characters = self.tokenize_characters()
        # for consuming the '"'
        self.consume()
        return JSONString(characters)

    def tokenize_characters(self) -> str:
        character = self.tokenize_character()
        if self.next() == '"':
            return character
        return character + self.tokenize_characters()
    
    def tokenize_character(self) -> str:
        if self.next() == '"':
            return ''
        elif self.next() == '\\':
            return '\\' + self.tokenize_escape()
        else:
            return self.consume()
    
    def tokenize_escape(self) -> str:
        if self.next() in ['"', '\\', '/', 'b', 'f', 'n', 'r', 't']:
            return self.consume()
        elif self.next() == 'u':
            output = self.consume()
            for i in range(4):
                output += self.tokenize_hex()
            return output
        else:
            raise IncorrectIdentifierError()

    def tokenize_hex(self) -> str:
        if self.next() in ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','A','B','C','D','E','F']:
            return self.consume()
        else:
            raise IncorrectIdentifierError()
    
    def tokenize_number(self) -> JSONNumber:
        integer = self.tokenize_integer()
        fraction = self.tokenize_fraction()
        exponent = self.tokenize_exponent()
        return JSONNumber(f'{integer}{fraction}{exponent}')
    
    def tokenize_integer(self) -> str:
        optional_minus_sign = ''
        if self.next() == '-':
            optional_minus_sign = self.consume()
        if TokenizerHelpers.isdigit(self.next()):
            if self.next() == '0':
                if TokenizerHelpers.isdigit(self.next_n(2)[-1]):
                    raise IncorrectIdentifierError()
                else:
                    return optional_minus_sign + self.tokenize_digit()
            elif TokenizerHelpers.isdigit(self.next()):
                return optional_minus_sign + self.tokenize_digits()

    
    def tokenize_digit(self) -> str:
        return self.consume()
    
    def tokenize_digits(self) -> str:
        digit = self.tokenize_digit()
        if TokenizerHelpers.isdigit(self.next()):
            return digit + self.tokenize_digits()
        else:
            return digit

    def tokenize_fraction(self) -> str:
        if self.next() != '.':
            return ''
        else:
            # consume the decimal
            decimal = self.consume()
            # TODO: include check for whether the next is a number
            digits = self.tokenize_digits()
            return decimal + digits
    
    def tokenize_exponent(self) -> str:
        if self.next() not in ['e', 'E']:
            return ''
        else:
            return self.tokenize_signs() + self.tokenize_digits()
    
    def tokenize_signs(self) -> str:
        if self.next() in ['+', '-']:
            return self.consume()
        else:
            return ''

    def tokenize(self):
        return self.tokenize_element()

        
        
    
    

        


###
# The JSON Spec can be found at https://json.org/json-en.html
###