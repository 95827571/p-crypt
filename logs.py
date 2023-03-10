from os import path
import os
from datetime import datetime

LOGS_FILENAME = "logs.txt"

def format_log(task: str, encryption_method: str, output: str):
    now = datetime.now()
    return f"\nTask: {task}\n\
Encryption Method: {encryption_method}\n\
Output: {output}\n\
Time: {now.strftime('%d/%m/%Y %H:%M:%S')}\n\
{'-'*50}"



def append_log(task: str, encryption_method: str, output: str):
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