from encryption import base, caesar, atbash, keyword_c, affine, vigenere
import menu


def caeser_callback(response):
    try:
        response = int(response)
    except:
        print("not a valid input")
        return False
    
    if response < -25 or response > 25:
        print("Pick a number between -25 and 25")
        return False
    
    return True

def encrypt_input(encryption_method: base.EncryptionMethod, settings: dict[str,str]):
    user_input = input("What message would you like to encrypt?\n")
    encrypted_message = ""
    match settings["method"]:
        case "Caesar":
            shift_input = menu.ask_user_with_callback("How much would you like to shift to the left(- for right shift)?", caeser_callback)

            encrypted_message = encryption_method.encrypt(user_input, int(shift_input))
        case "Keyword":
            keyword_input = input("What keyword would you like to use?\n")

            encrypted_message = encryption_method.encrypt(user_input, keyword_input)
        case "Vigenere":
            keyword_input = input("What keyword would you like to use?\n")

            encrypted_message = encryption_method.encrypt(user_input, keyword_input)
        case _:
            encrypted_message = encryption_method.encrypt(user_input)
    
    print("-"*menu.SEPARATOR_LENGTH)
    print(f"Encrypted Message: {menu.TerminalColors.BRIGHT_CYAN}{encrypted_message}{menu.TerminalColors.ENDC} \
| {menu.TerminalColors.BRIGHT_RED}Method: {settings['method']}{menu.TerminalColors.ENDC}")
    print("-"*menu.SEPARATOR_LENGTH)

def decrypt_input(encryption_method: base.EncryptionMethod, settings: dict[str,str]):
    user_input = input("What cipher would you like to decrypt?\n")
    decrypted_cipher = ""
    match settings["method"]:
        case "Caesar":
            shift_input = menu.ask_user_with_callback("How much would you like to shift to the left(- for right shift)?", caeser_callback)

            decrypted_cipher = encryption_method.decrypt(user_input, int(shift_input))
        case "Keyword":
            keyword_input = input("What keyword would you like to use?\n")

            decrypted_cipher = encryption_method.decrypt(user_input, keyword_input)
        case "Vigenere":
            keyword_input = input("What keyword would you like to use?\n")

            decrypted_cipher = encryption_method.decrypt(user_input, keyword_input)
        case _:
            decrypted_cipher = encryption_method.decrypt(user_input)
    
    print("-"*menu.SEPARATOR_LENGTH)
    print(f"Decryption Result: {menu.TerminalColors.BRIGHT_CYAN}{decrypted_cipher}{menu.TerminalColors.ENDC} \
| {menu.TerminalColors.BRIGHT_RED}Method: {settings['method']}{menu.TerminalColors.ENDC}")
    print("-"*menu.SEPARATOR_LENGTH)

def manage_inputs(settings: dict[str,str]):
    encryption_method = None
    match settings["method"]:
        case "Caesar":
            encryption_method = caesar.CeaserEncryption()
        case "Atbash":
            encryption_method = atbash.AtbashEncryption()
        case "Affine":
            encryption_method = affine.AffineEncryption()
        case "Keyword":
            encryption_method = keyword_c.KeywordEncryption()
        case "Vigenere":
            encryption_method = vigenere.VigenereEncryption()

    match settings["doing"]:
        case "Encrypt":
            encrypt_input(encryption_method, settings)
        case "Decrypt":
            decrypt_input(encryption_method, settings)

def main():
    settings = {
        "doing": "Encrypt",
        "method": "Caesar",
    }

    print(menu.textLogo)

    while True:
        settings["doing"] = menu.ask_user("What would you like to do?", "Encrypt", "Decrypt", "Exit")

        # Exits the loop exiting the program
        if settings["doing"] == "Exit":
            return

        settings["method"] = menu.ask_user("What type of encryption?", "Caesar", "Atbash", "Affine", "Keyword", "Vigenere")
        manage_inputs(settings)


if __name__ == '__main__':
    main()