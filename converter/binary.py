from converter import ConversionMethod

class BinaryConverter(ConversionMethod):
    def __init__(self):
        super().__init__()
    
    def convert_to(self, decimal: int):
        y = 1
        binary_placements = []
        while y <= decimal * 2:
            binary_placements.append(y)
            y *= 2

        binary_str = ""
        for i in reversed(binary_placements):
            if i <= decimal:
                binary_str += "1"
                decimal -= i
                continue

            binary_str += "0"\

        return binary_str
    
    def convert_from(self, binary: str):
        decimal = 0
        last_placement = 1
        for digit in list(reversed(binary)):
            print(last_placement)
            if digit == "1":
                decimal += last_placement
                
            last_placement *= 2

        return decimal