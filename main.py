from encryption import caesar, atbash, keyword_c, affine, vigenere
from menu import decryption_page, encryption_page, settings_page
import menu
import os
import json


def manage_encryption(task_settings: dict[str,str]):
    task_method = None
    match task_settings["method"]:
        case "Caesar":
            task_method = caesar.CeaserEncryption()
        case "Atbash":
            task_method = atbash.AtbashEncryption()
        case "Affine":
            task_method = affine.AffineEncryption()
        case "Keyword":
            task_method = keyword_c.KeywordEncryption()
        case "Vigenere":
            task_method = vigenere.VigenereEncryption()

    match task_settings["doing"]:
        case "Encrypt":
            encryption_page.encrypt_input(task_method, task_settings)
        case "Decrypt":
            decryption_page.decrypt_input(task_method, task_settings)


def manage_settings():
    while True:
        if settings_page.settings_options():
            os.system('cls' if os.name == 'nt' else 'clear')
            print(menu.textLogo)
            break

# Creates the settings config
def create_settings():
    if not os.path.exists("config.json"):
        settings = {
            "logs": True,
            "save_keys": False
        }
        json_object = json.dumps(settings, indent=4)
        file = open("config.json", "w")
        file.write(json_object)
        file.close()

def main():
    # Clears the screen and prints p crypt
    os.system('cls' if os.name == 'nt' else 'clear')
    print(menu.textLogo)
    create_settings()

    # Our current task settings
    task_settings = {
        "doing": "Encrypt",
        "method": "Caesar",
    }

    while True:
        # settings_page()
        task_settings["doing"] = menu.ask_user("", "Encrypt", "Decrypt", "Convert", "Settings", "Exit")

        # Exits the loop exiting the program
        if task_settings["doing"] == "Exit":
            return

        # Encryption page
        if task_settings["doing"] == "Encrypt" or task_settings["doing"] == "Decrypt": 
            task_settings["method"] = menu.ask_user("Method?", "Caesar", "Atbash", "Affine", "Keyword", "Vigenere")
            manage_encryption(task_settings)
        # Conversion page
        elif task_settings["doing"] == "Convert":
            task_settings["method"] = menu.ask_user("Conversion?", "Hexadecimal")
        # Settings page
        elif task_settings["doing"] == "Settings":
            manage_settings()


if __name__ == '__main__':
    main()