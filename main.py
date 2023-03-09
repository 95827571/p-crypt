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
    match settings["method"]:
        case "Caesar":
            shift_input = menu.ask_user_with_callback("How much would you like to shift to the left(- for right shift)?", caeser_callback)

            print(encryption_method.encrypt(user_input, int(shift_input)))
            return
        case "Keyword":
            keyword_input = input("What keyword would you like to use?")

            print(encryption_method.encrypt(user_input, keyword_input))
            return
        case "Vigenere":
            keyword_input = input("What keyword would you like to use?")

            print(encryption_method.encrypt(user_input, keyword_input))
            return
        
    print(encryption_method.encrypt(user_input))

def decrypt_input(encryption_method: base.EncryptionMethod, settings: dict[str,str]):
    user_input = input("What cipher would you like to decrypt?")
    match settings["method"]:
        case "Caesar":
            shift_input = menu.ask_user_with_callback("How much would you like to shift to the left(- for right shift)?", caeser_callback)

            print(encryption_method.decrypt(user_input, int(shift_input)))
            return
        case "Keyword":
            keyword_input = input("What keyword would you like to use?\n")

            print(encryption_method.decrypt(user_input, keyword_input))
            return
        case "Vigenere":
            keyword_input = input("What keyword would you like to use?\n")

            print(encryption_method.decrypt(user_input, keyword_input))
            return
    
        
    print(encryption_method.decrypt(user_input))

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