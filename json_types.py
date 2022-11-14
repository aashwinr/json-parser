class JSONString:
    def __init__(self, contents) -> None:
        self.content = contents
    def __repr__(self) -> str:
        return f'JSONString({self.content})'

class JSONNumber:
    def __init__(self, number) -> None:
        self.number = number
    def __repr__(self) -> str:
        return f'JSONNumber({self.number})'

class JSONNull:
    def __repr__(self) -> str:
        return 'JSONNull'

class JSONTrue:
    def __repr__(self) -> str:
        return 'JSONTrue'

class JSONFalse:
    def __repr__(self) -> str:
        return 'JSONFalse'

class JSONValue:
    def __init__(self, value) -> None:
        self.value = value
    def __repr__(self) -> str:
        return f'JSONValue({self.value})'

class JSONObject:
    def __init__(self, key_value_pairs) -> None:
        self.key_value_pairs = key_value_pairs
    def __repr__(self) -> str:
        repr_string = '{\n'
        key_value_pair_list = list(self.key_value_pairs.items())
        iter_len = len(key_value_pair_list) - 1
        for i in range(iter_len):
            repr_string += f'{key_value_pair_list[i][0]}:{key_value_pair_list[i][1]},\n'
        repr_string += f'{key_value_pair_list[-1][0]}:{key_value_pair_list[-1][1]}\n}}\n'
        return f'JSONObject({repr_string})'

class JSONArray:
    def __init__(self, values) -> None:
        self.values = values
    def __repr__(self) -> str:
        return f'JSONArray({self.values})'