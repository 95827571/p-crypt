from menu import multi_checkbox, textLogo
import os
import json

logs = True
save_keys = True
exit_settings = False
def logs_callback():
    global logs
    logs = not logs

def save_keys_callback():
    global save_keys
    save_keys = not save_keys

def exit_callback():
    global exit_settings
    exit_settings = not exit_settings

def settings_options():
    # f = open("config.json")
    # json_object = json.load(f)
    # f.close()
    os.system('cls' if os.name == 'nt' else 'clear')
    print(textLogo)
    multi_checkbox(
        [
            {
                "name": "Logs",
                "target_value": logs,
                "required_value": True,
                "callback": logs_callback,
            },
            {
                "name": "Save Keys",
                "target_value": save_keys,
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


