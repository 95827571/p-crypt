from encryption.base import EncryptionMethod, alphabet

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
        reversed_chars = [self.__reverse_char(char) for char in list(message.lower())]
        encrypted_result = ''.join(str(char) for char in reversed_chars)

        return encrypted_result

    # decrypting literally just takes the encrypted message and re-reverses it LOL
    def decrypt(self, cipher: str) -> str:
        return self.encrypt(cipher)