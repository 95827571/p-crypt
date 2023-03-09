textLogo = '''
██████╗░░░░░░░░█████╗░██████╗░██╗░░░██╗██████╗░████████╗
██╔══██╗░░░░░░██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝
██████╔╝█████╗██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░
██╔═══╝░╚════╝██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░
██║░░░░░░░░░░░╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░
╚═╝░░░░░░░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░
'''

class TerminalColors:
    RED = '\u001b[31m'
    BLUE = '\033[36;49m'
    ENDC = '\033[0m'

def ask_user(question: str, *answers: str):
    print(question)
    answers = [answer for answer in answers]
    formatted_answers = ''.join(f"{TerminalColors.BLUE}{index+1}) {answer}{TerminalColors.ENDC}\n" for index, answer in enumerate(answers))
    print(formatted_answers)

    while True:
        user_input = input()
        
        try:
            user_input = int(user_input)-1
        except:
            print(f"{TerminalColors.RED}Can't parse this response, try a valid number.{TerminalColors.ENDC}")
            continue

        if user_input < 0 or user_input >= len(answers):
            print(f"{TerminalColors.RED}Not a valid input, please try one in the range{TerminalColors.ENDC}")
            continue

        return answers[user_input]
    

def ask_user_with_callback(question: str, callback):
    user_input = None
    while True:
        print(f"{question}\n")
        user_input = input()
        if callback(user_input):
            break
        
    
    return user_input