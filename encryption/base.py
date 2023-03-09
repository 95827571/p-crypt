alphabet = 'abcdefghijklmnopqrstuvwxyz'

class EncryptionMethod():
    def __init__(self):
        pass

    def encrypt():
        pass

    def decrypt():
        pass

# Makes sure the index is never out of range of the alphabet, and if it does, loop round.
def check_index_to_alphabet(index: int):
    # if the index after shift is longer than length, then loop around
    if index >= len(alphabet):
        return abs(index - len(alphabet))
        
    # makes sure the index is never below 0, if it is then loop back to start
    if index < 0:
        return len(alphabet) - (abs(index - len(alphabet)))
    
    return index
