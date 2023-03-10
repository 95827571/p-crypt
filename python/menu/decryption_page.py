from encryption import EncryptionMethod
from menu import ask_user_with_callback, SEPARATOR_LENGTH, TerminalColors, caeser_callback, textLogo
from encryption.railfence import railfence_callback
import os
import logs

def decrypt_input(encryption_method: EncryptionMethod, settings: dict[str,str]):
    user_input = input("What cipher would you like to decrypt?\n")
    decrypted_cipher = ""

    # finds which method we are doing
    match settings["method"]:
        case "Caesar":
            shift_input = ask_user_with_callback("How much would you like to shift to the left(- for right shift)?", caeser_callback)

            decrypted_cipher = encryption_method.decrypt(user_input, int(shift_input))
        case "Keyword":
            keyword_input = input("What keyword would you like to use?\n")

            decrypted_cipher = encryption_method.decrypt(user_input, keyword_input)
        case "Vigenere":
            keyword_input = input("What keyword would you like to use?\n")

            decrypted_cipher = encryption_method.decrypt(user_input, keyword_input)
        case "Railfence":
            shift_input = ask_user_with_callback("How many rows?", railfence_callback)

            decrypted_cipher = encryption_method.decrypt(user_input, int(shift_input))
        case _:
            decrypted_cipher = encryption_method.decrypt(user_input)

    os.system('cls' if os.name == 'nt' else 'clear')
    print(textLogo)

    # outputs
    print("-"*SEPARATOR_LENGTH)
    print(f"Decryption Result: {TerminalColors.BRIGHT_CYAN}{decrypted_cipher}{TerminalColors.ENDC} \
| {TerminalColors.BRIGHT_RED}Method: {settings['method']}{TerminalColors.ENDC}")
    print("-"*SEPARATOR_LENGTH)

    logs.append_log(settings["doing"], settings["method"], decrypted_cipher)