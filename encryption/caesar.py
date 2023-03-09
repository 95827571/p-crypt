from base import EncryptionMethod, alphabet

class CeaserEncryption(EncryptionMethod):
    def __init__(self):
        super().__init__()


    # shifts a singular char by x amount to the left
    def __shift_char(self, char: str, shift: int) -> str:
        # if the character is not in the alphabet, then just don't shift it
        if char not in list(alphabet):
            return char
        
        # the value after shifting the character
        index_after_shift = list(alphabet).index(char) - shift

        # if the index after shift is longer than length, then loop around
        if index_after_shift >= len(alphabet):
            return alphabet[abs(index_after_shift - len(alphabet))]
        
        return alphabet[index_after_shift]
    
    # unshifts a singular char by x amount
    def __unshift_char(self, char: str, shift: int) -> str:
        # if the character is not in the alphabet, we don't need to unshift
        if char not in list(alphabet):
            return char

        # gets the index
        index_after_shift = list(alphabet).index(char) + shift

        # if the index after shift is longer than length, then loop around
        if index_after_shift >= len(alphabet):
            return alphabet[abs(index_after_shift - len(alphabet))]

        return alphabet[index_after_shift]
    
    # encrypts
    def encrypt(self, message: str, shift: int) -> str:
        message_split = list(message.lower())
        shifted_chars = [self.__shift_char(char, shift) for char in message_split]
        encrypted_result = ''.join(str(char) for char in shifted_chars)

        return encrypted_result

    # decrypts
    def decrypt(self, encrypted_message: str, shift: int) -> str:
        message_split = list(encrypted_message.lower())
        unshifted_chars = [self.__unshift_char(char, shift) for char in message_split]
        decrypted_result = ''.join(str(char) for char in unshifted_chars)

        return decrypted_result