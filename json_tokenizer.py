from tokenizer import Tokenizer
from incorrect_character import IncorrectCharacterError

class JSON_Tokenizer(Tokenizer):
    def __init__(self, contents):
        super().__init__(contents)
    
    def tokenize_whitespace(self):
        self.consume_whitespace()

    def tokenize_string(self):
        string_begin_character = self.consume()
        def is_valid_string_char(char:str):
            return ((char.isascii()) and (char != '"'))
        if string_begin_character != '"':
            raise IncorrectCharacterError(expected_character='"', received_character=string_begin_character)
        string_contents = self.consume_while(is_valid_string_char)
        string_terminating_character = self.consume()
        if string_begin_character != '"':
            raise IncorrectCharacterError(expected_character='"', received_character=string_terminating_character)
        return JSString(string_contents)

    def tokenize_number(self):
        raise NotImplementedError()
    def tokenize_value(self):
        raise NotImplementedError()
    def tokenize_object(self):
        raise NotImplementedError()
    def tokenize_array(self):
        raise NotImplementedError()

###
# The JSON Spec can be found at https://json.org/json-en.html
###