from converter import ConversionMethod
from converter.hexadecimal import HexadecimalConverter
from menu import ask_user, ask_user_with_callback, textLogo, SEPARATOR_LENGTH, TerminalColors
from logs import append_custom_log
import re
import os
from datetime import datetime

def decimal_check_callback(number: str):
    try:
        number = int(number)
    except:
        print("Please input a number")
        return False
    
    if number < 0:
        print("Pick a number that is not negative")
        return False
    
    return True

def hex_check_callback(hexadecimal: str):
    if not re.search("^[0-9a-fA-F]+$", hexadecimal):
        print("Please input a valid hexadecimal value")
        return
    
    return True

def create_log(input: str, output:str, conversion_method: str):
    now = datetime.now()
    append_custom_log(f"Input: {input}\n\
Output: {output}\n\
Conversion: {conversion_method}\n\
Time: {now.strftime('%d/%m/%Y %H:%M:%S')}")

def manage_hexadecimal(convertion_method: HexadecimalConverter, settings: dict[str,str]):
    user_input = ask_user("", "Decimal > Hex", "Hex > Decimal")
    match user_input:
        case "Decimal > Hex":
            before_input = ask_user_with_callback("Decimal: ", decimal_check_callback)
            output = convertion_method.convert_to(int(before_input))
        case "Hex > Decimal":
            before_input = ask_user_with_callback("Hex: ", hex_check_callback)
            output = convertion_method.convert_from(before_input)

    # Clears the terminal and shows us our result
    os.system('cls' if os.name == 'nt' else 'clear')
    print(textLogo)

    # Our output
    print("-"*SEPARATOR_LENGTH)
    print(f"Before Conversion: {TerminalColors.BRIGHT_CYAN}{before_input}{TerminalColors.ENDC} \
| After Conversion: {TerminalColors.BRIGHT_CYAN}{output}{TerminalColors.ENDC} \
| {TerminalColors.BRIGHT_RED}Conversion: {user_input}{TerminalColors.ENDC}")
    print("-"*SEPARATOR_LENGTH)

    create_log(before_input, output, user_input)

def conversion_input(convertion_method: ConversionMethod, settings: dict[str,str]):
    match settings["method"]:
        case "Hexadecimal":
            manage_hexadecimal(convertion_method, settings)