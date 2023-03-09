from base import EncryptionMethod, alphabet

class AffineEncryption(EncryptionMethod):
    def __init__(self):
        super().__init__()

    # convers the character to an integer
    def __convert_char(self, char: str) -> int:
        # if the character is not in the alphabet, we don't need to unshift
        if char not in list(alphabet):
            return char

        return list(alphabet).index(char)+1
    
    # converts the integer back to its normal state
    def __unconvert_char(self, int_as_char: str) -> str:
        try:
            return alphabet[int(int_as_char)-1]
        except:
            return int_as_char
    
    # encrypts the message
    def encrypt(self, message: str) -> str:
        message_split = list(message.lower())
        converted_chars = [self.__convert_char(char) for char in message_split]
        encrypted_result = ''.join(f"{str(char)}-" for char in converted_chars)

        return encrypted_result

    #decrypts the message :)
    def decrypt(self, encrypted_message: str) -> str:
        message_split = encrypted_message.split("-")
        normal_chars = [self.__unconvert_char(char) for char in message_split]
        decrypted_result = ''.join(str(char) for char in normal_chars)

        return decrypted_result