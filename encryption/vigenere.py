from base import EncryptionMethod, alphabet

class VigenereEncryption(EncryptionMethod):
    def __init__(self):
        super().__init__()

    def __shift_char_by_key_char(self, char: str, kw_char:str) -> str:
        if char not in alphabet or kw_char not in alphabet:
            return
        
        index_after_shift = list(alphabet).index(char) - list(alphabet).index(kw_char)

        # if the index after shift is longer than length, then loop around
        if index_after_shift >= len(alphabet):
            return alphabet[abs(index_after_shift - len(alphabet))]
        
        return alphabet[index_after_shift]
    
    def __unshift_char_by_key_char(self, char: str, kw_char:str) -> str:
        if char not in alphabet or kw_char not in alphabet:
            return
        
        index_after_shift = list(alphabet).index(char) + list(alphabet).index(kw_char)

        # if the index after shift is longer than length, then loop around
        if index_after_shift >= len(alphabet):
            return alphabet[abs(index_after_shift - len(alphabet))]
        
        return alphabet[index_after_shift]

    def encrypt(self, message: str, keyword: str) -> str:
        message_split = list(message.lower())
        keyword_index = 0
        shifted_chars = []
        for char in message_split:
            if keyword_index == len(keyword):
                keyword_index = 0
            
            shifted_chars.append(self.__shift_char_by_key_char(char, keyword[keyword_index]))
            keyword_index += 1

        encrypted_result = ''.join(char for char in shifted_chars)
        return encrypted_result

    def decrypt(self, cipher: str, keyword: str):
        message_split = list(cipher.lower())
        keyword_index = 0
        unshifted_chars = []
        for char in message_split:
            if keyword_index == len(keyword):
                keyword_index = 0
            
            unshifted_chars.append(self.__unshift_char_by_key_char(char, keyword[keyword_index]))
            keyword_index += 1

        encrypted_result = ''.join(char for char in unshifted_chars)
        return encrypted_result