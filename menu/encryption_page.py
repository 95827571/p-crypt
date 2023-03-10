from encryption import EncryptionMethod
from menu import ask_user_with_callback, SEPARATOR_LENGTH, TerminalColors, caeser_callback, textLogo
import os


def encrypt_input(encryption_method: EncryptionMethod, settings: dict[str,str]):
    user_input = input("What message would you like to encrypt?\n")
    encrypted_message = ""
    match settings["method"]:
        case "Caesar":
            shift_input = ask_user_with_callback("How much would you like to shift to the left(- for right shift)?", caeser_callback)

            encrypted_message = encryption_method.encrypt(user_input, int(shift_input))
        case "Keyword":
            keyword_input = input("What keyword would you like to use?\n")

            encrypted_message = encryption_method.encrypt(user_input, keyword_input)
        case "Vigenere":
            keyword_input = input("What keyword would you like to use?\n")

            encrypted_message = encryption_method.encrypt(user_input, keyword_input)
        case _:
            encrypted_message = encryption_method.encrypt(user_input)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print(textLogo)
    print("-"*SEPARATOR_LENGTH)
    print(f"Encrypted Message: {TerminalColors.BRIGHT_CYAN}{encrypted_message}{TerminalColors.ENDC} \
| {TerminalColors.BRIGHT_RED}Method: {settings['method']}{TerminalColors.ENDC}")
    print("-"*SEPARATOR_LENGTH)