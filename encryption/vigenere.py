from encryption import EncryptionMethod, alphabet, check_index_to_alphabet

class VigenereEncryption(EncryptionMethod):
    def __init__(self):
        super().__init__()

    # shifts the character by the index of the keyword character to the alphabet
    def __shift_char_by_key_char(self, char: str, kw_char:str) -> str:
        if char not in alphabet or kw_char not in alphabet:
            return char
        
        index_after_shift = list(alphabet).index(char) + list(alphabet).index(kw_char)
        
        return alphabet[check_index_to_alphabet(index_after_shift)]
    
    # unshifts ^
    def __unshift_char_by_key_char(self, char: str, kw_char:str) -> str:
        if char not in alphabet or kw_char not in alphabet:
            return char
        
        index_after_shift = list(alphabet).index(char) - list(alphabet).index(kw_char)
        
        return alphabet[check_index_to_alphabet(index_after_shift)]

    # shifts each character in a word by key char
    def encrypt(self, message: str, keyword: str) -> str:
        # splits the message and key word
        message_split = list(message.lower())
        keyword_index = 0
        shifted_chars = []
        for char in message_split:
            # makes sure the index is never longer than the keyword
            if keyword_index == len(keyword):
                keyword_index = 0
            
            shifted_chars.append(self.__shift_char_by_key_char(char, keyword[keyword_index]))
            keyword_index += 1

        # joins characters together
        encrypted_result = ''.join(char for char in shifted_chars)
        return encrypted_result

    # unshifts each character in a word by key char
    def decrypt(self, cipher: str, keyword: str):
        message_split = list(cipher.lower())
        keyword_index = 0
        unshifted_chars = []
        for char in message_split:
            # makes sure the index is never longer than the keyword
            if keyword_index == len(keyword):
                keyword_index = 0
            
            unshifted_chars.append(self.__unshift_char_by_key_char(char, keyword[keyword_index]))
            keyword_index += 1

        decrypted_result = ''.join(char for char in unshifted_chars)
        return decrypted_result