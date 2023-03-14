from converter import ConversionMethod

hex_table = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

class HexadecimalConverter(ConversionMethod):
    def __init__(self):
        super().__init__()
    
    # multiplies a character by its position value
    def __convert_char(self, char: str, multiplier: int):
        return hex_table[char] * multiplier
    
    def __convert_to_hex(self, num: int):
        remainder = (num % 16)
        rest = num // 16
        hex_value = "0"

        for key in hex_table:
            if hex_table[key] == remainder:
                hex_value = key

        if (rest == 0):
            return hex_value
        
        return self.__convert_to_hex(rest) + hex_value


    # converts each character in a hexadecimal string
    def convert_from(self, hexadecimal: str):
        converted_chars = [self.__convert_char(char, 16 ** position if position > 0 else 1) for position, char in enumerate(reversed(list(hexadecimal.upper())))]
        return sum(converted_chars)
    
    def convert_to(self, number: int):
        return self.__convert_to_hex(number)
