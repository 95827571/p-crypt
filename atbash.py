from encryption import EncryptionMethod

alphabet = 'abcdefghijklmnopqrstuvwxyz'

class AtbashEncryption(EncryptionMethod):
    def __init__(self):
        super().__init__()

    # reverses the char
    def __reverse_char(self, char: str) -> str:
        if char not in list(alphabet):
            return char
        
        return alphabet[abs((len(alphabet)-1) - list(alphabet).index(char))]
        
    # encrypts with atbash
    def encrypt(self, message: str) -> str:
        message_split = list(message)
        reversed_chars = [self.__reverse_char(char) for char in message_split]
        encrypted_result = ''.join(str(char) for char in reversed_chars)

        return encrypted_result

    # decrypting literally just takes the encrypted message and re-reverses it LOL
    def decrypt(self, encrypted_message: str) -> str:
        return self.encrypt(encrypted_message)