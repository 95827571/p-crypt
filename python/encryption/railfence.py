from encryption import EncryptionMethod, alphabet, check_index_to_alphabet
import math

def railfence_callback(response):
    try:
        response = int(response)
    except:
        print("not a valid input")
        return False
    
    return True

class RailfenceEncryption(EncryptionMethod):
    def __init__(self):
        super().__init__()

    def __rail_from_cipher(self, message: str, key: int) -> list[list[str]]:
        rail = [""] * key
        row = 0
        for character in message:
            rail[row] += character
            if row == key-1:
                row = 0
                continue
            
            row += 1

        return rail

    # encrypts the cipher into rows and then puts it into a string
    def encrypt(self, message: str, key: int) -> str:
        rail = self.__rail_from_cipher(message, key)

        return "".join(rail)
    
    # Takes a cipher and makes into its original encrypted rail
    def __reverse_cipher_into_rail(self, cipher: str, key: int) -> list[list[str]]:
        # Creates the max amount of spots possible in each row from the cipher
        max_rail_length = math.ceil(len(cipher) / key)
        rail = [[""] * max_rail_length for i in range(key)]

        # Puts each character into its related row as if it was being encrypted
        current_row = 0
        current_char = 0
        for char in cipher:
            rail[current_row][current_char] = char

            # Loop through every row
            # we start from the beginning because its possible once row is less than the others
            if current_char == max_rail_length-1:
                current_row += 1
                current_char = 0
                continue

            current_char += 1

        return rail
    
    # Creates plaintext from reverse rail
    def __plaintext_from_reverse_rail(self, cipher: str, key: int, rail: list[list[str]]) -> str:
        plaintext = ""
        current_row = 0
        current_char = 0
        while len(plaintext) != len(cipher):
            plaintext += rail[current_row][current_char]

            if current_row == key-1:
                current_char += 1
                current_row = 0
                continue

            current_row += 1
        return plaintext

    def decrypt(self, cipher: str, key: int) -> str:
        rail = self.__reverse_cipher_into_rail(cipher, key)
        return self.__plaintext_from_reverse_rail(cipher, key, rail).strip()
                  