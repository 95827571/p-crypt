from encryption import EncryptionMethod

alphabet = 'abcdefghijklmnopqrstuv'

class AtbashEncryption(EncryptionMethod):
    def __init__(self):
        super().__init__()

    def __reverse_char(self, char: str) -> str:
        if char not in list(alphabet):
            return char
        
        return alphabet[abs((len(alphabet)-1) - list(alphabet).index(char))]
        

    def encrypt(self, message: str) -> str:
        message_split = list(message)
        reversed_chars = [self.__reverse_char(char) for char in message_split]
        encrypted_result = ''.join(str(char) for char in reversed_chars)

        return encrypted_result

    def decrypt(self, message: str) -> str:
        return self.encrypt(message)