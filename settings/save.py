import json

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