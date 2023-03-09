from encryption.base import EncryptionMethod, alphabet


class KeywordEncryption(EncryptionMethod):
    def __init__(self):
        super().__init__()

    def __keyword_shift_char(self, char: str, new_alphabet: list[str]) -> str:
        # if the character is not in the alphabet, we don't need to unshift
        if char not in list(alphabet):
            return char
        
        return new_alphabet[alphabet.index(char)]
    
    def __keyword_unshift_char(self, char: str, new_alphabet: list[str]) -> list[str]:
        # if the character is not in the alphabet, we don't need to unshift
        if char not in list(alphabet):
            return char
        
        return alphabet[new_alphabet.index(char)] 

    def __grab_alphabet(self, keyword: str) -> list[str]:
        new_alphabet = []
        for char in list(keyword):
            if char in new_alphabet:
                continue

            new_alphabet.append(char)

        for char in alphabet:
            if char in new_alphabet:
                continue
            
            new_alphabet.append(char)

        return new_alphabet


    def encrypt(self, message: str, keyword: str) -> str:
        new_alphabet = self.__grab_alphabet(keyword.lower())
        shifted_message = [self.__keyword_shift_char(char, new_alphabet) for char in list(message.lower())]
        encrypted_result = ''.join(str(char) for char in shifted_message)

        return encrypted_result
        

    def decrypt(self, cipher: str, keyword: str):
        new_alphabet = self.__grab_alphabet(keyword.lower())
        unshifted_message = [self.__keyword_unshift_char(char, new_alphabet) for char in list(cipher.lower())]
        decrypted_result = ''.join(str(char) for char in unshifted_message)

        return decrypted_result