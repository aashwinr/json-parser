class IncorrectCharacterError(Exception):
    def __init__(self, expected_character: str, received_character: str, *args: object) -> None:
        self.message = f'Incorrect Character: Expected {expected_character}, got {received_character}'
        super().__init__(*args, self.message)
