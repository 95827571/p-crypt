from converter import ConvertionMethod

hex_table = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

class HexadecimalConverter(ConvertionMethod):
    def __init__(self):
        super().__init__()

    def __convert_char(self, char: list[str], multiplier: int):
        return hex_table[char] * multiplier


    def convert_from(self, hexadecimal: str):
        converted_chars = [self.__convert_char(char, 16 ** position if position > 0 else 1) for position, char in enumerate(reversed(list(hexadecimal.upper())))]
        return sum(converted_chars)
