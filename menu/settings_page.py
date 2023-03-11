from menu import multi_checkbox, textLogo
import os
from settings.save import grab_settings_json, change_settings_key

exit_settings = False

def logs_callback():
    json_object = grab_settings_json()
    change_settings_key("logs", not json_object["logs"])

def save_keys_callback():
    json_object = grab_settings_json()
    change_settings_key("save_keys", not json_object["save_keys"])

def exit_callback():
    global exit_settings
    exit_settings = True

def settings_options():
    json_object = grab_settings_json()

    global exit_settings
    exit_settings = False

    os.system('cls' if os.name == 'nt' else 'clear')
    print(textLogo)
    multi_checkbox(
        [
            {
                "name": "Logs",
                "target_value": json_object["logs"],
                "required_value": True,
                "callback": logs_callback,
            },
            {
                "name": "Save Keys",
                "target_value": json_object["save_keys"],
                "required_value": True,
                "callback": save_keys_callback,
            },
            {
                "name": "Exit",
                "target_value": exit_settings,
                "required_value": True,
                "callback": exit_callback,
            },
        ]
    )

    return exit_settings