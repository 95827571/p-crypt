from encryption import caesar, atbash, keyword_c, affine, vigenere
from menu.encryption_page import EncryptionMethod
from menu import decryption_page, encryption_page, settings_page
import menu
import os


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
            encryption_page.encrypt_input(encryption_method, settings)
        case "Decrypt":
            decryption_page.decrypt_input(encryption_method, settings)
        case "Settings":
            while True:
                if settings_page.settings_options():
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(menu.textLogo)
                    break


def main():
    settings = {
        "doing": "Encrypt",
        "method": "Caesar",
    }
    os.system('cls' if os.name == 'nt' else 'clear')
    print(menu.textLogo)

    while True:
        # settings_page()
        settings["doing"] = menu.ask_user("", "Encrypt", "Decrypt", "Settings", "Exit")

        # Exits the loop exiting the program
        if settings["doing"] == "Exit":
            return

        # Goes to settings
        if settings["doing"] != "Settings": 
            settings["method"] = menu.ask_user("Method?", "Caesar", "Atbash", "Affine", "Keyword", "Vigenere")
        
        manage_inputs(settings)


if __name__ == '__main__':
    main()