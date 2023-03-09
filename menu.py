textLogo = '''
██████╗░░░░░░░░█████╗░██████╗░██╗░░░██╗██████╗░████████╗
██╔══██╗░░░░░░██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝
██████╔╝█████╗██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░
██╔═══╝░╚════╝██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░
██║░░░░░░░░░░░╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░
╚═╝░░░░░░░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░
'''

def ask_user(question: str, *answers: str):
    print(question)
    answers = [answer for answer in answers]
    formatted_answers = ''.join(f"{index+1}) {answer}\n" for index, answer in enumerate(answers))
    print(formatted_answers)

    while True:
        user_input = input()
        
        try:
            user_input = int(user_input)-1
        except:
            print("Can't parse this response, try a valid number.")
            continue

        if user_input < 0 or user_input >= len(answers):
            print("Not a valid input, please try one in the range")
            continue

        return answers[user_input]
    

def ask_user_with_callback(question: str, callback):
    user_input = None
    while True:
        print(question)
        user_input = input()
        if callback(user_input):
            break
        
    
    return user_input