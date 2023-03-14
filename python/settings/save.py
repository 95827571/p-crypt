import json
import os

def grab_settings_json():
    f = open("config.json", "r")
    json_object = json.load(f)
    f.close()

    return json_object

def grab_settings_key(key):
    json_object = grab_settings_json()
    
    return json_object[key]

def change_settings_key(key, value):
    json_object = grab_settings_json()
    json_object[key] = value

    new_json_object = json.dumps(json_object, indent=4)
    file = open("config.json", "w")
    file.write(new_json_object)
    file.close()

    return json_object

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