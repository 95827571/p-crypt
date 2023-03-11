from os import path
import os
from datetime import datetime
from settings.save import grab_settings_key

LOGS_FILENAME = "logs.txt"

def format_log(task: str, encryption_method: str, output: str):
    now = datetime.now()
    return f"\nTask: {task}\n\
Encryption Method: {encryption_method}\n\
Output: {output}\n\
Time: {now.strftime('%d/%m/%Y %H:%M:%S')}\n\
{'-'*50}"


def append_log(task: str, encryption_method: str, output: str):
    if not grab_settings_key("logs"):
        return

    if not path.isfile(LOGS_FILENAME):
        file = open(LOGS_FILENAME, "w")
        file.write(f"{'-'*50}" + format_log(task, encryption_method, output))
        file.close()
        return

    with open ("logs.txt", "a") as file:
        if os.path.getsize("logs.txt") <= 0:
            file.write('-'*50)

        file.write(format_log(task, encryption_method, output))
        file.close()    

def append_custom_log(log: str):
    if not grab_settings_key("logs"):
        return

    if not path.isfile(LOGS_FILENAME):
        file = open(LOGS_FILENAME, "w")
        file.write(f"{'-'*50}\n{log}\n{'-'*50}")
        file.close()
        return
    
    with open ("logs.txt", "a") as file:
        if os.path.getsize("logs.txt") <= 0:
            file.write('-'*50)

        file.write(f"\n{log}\n{'-'*50}")
        file.close() 