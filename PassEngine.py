import os
import random
import string

align = os.get_terminal_size().columns

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[2J\033[H", end="", flush=True)

bg_red = "\033[41m\033[97m" 
red = "\033[91m"            
green = "\033[92m"          
reset = "\033[0m"

bord = ' /// PassEngine /// '
close = ' /// TERMINATED /// '
history_bord = ' /// HISTORY /// '

# History ki memory list
history = []

# File Handling: Purane passwords file se memory mein load karna
if os.path.exists('passEngineHistory.txt'):
    with open('passEngineHistory.txt', 'r') as file:
        history = [line.strip() for line in file.readlines()]

while True:
    clear_screen()
    print(f'{bg_red}{bord:^{align}}{reset}')
    print(f'\n  {green}Generate Strong, Hack-Proof Passwords{reset}')

    try:
        # Smart Menu: Length daalo, ya h/q dabao
        user_input = input(f'\n  {bg_red}[h]{reset} History | {bg_red}[q]{reset} Exit\n  {reset}Enter length (e.g. 8, 12) : ').strip().lower()

        # Exit Logic
        if user_input == 'q':
            clear_screen()
            print(f'{bg_red}{close:^{align}}{reset}')
            break
            
        # Blank Enter Logic
        if not user_input:
            continue
            
        # History Logic (MathEngine wale strict menu jaisa)
        if user_input == 'h':
            while True:
                clear_screen()
                print(f'{bg_red}{history_bord:^{align}}{reset}\n')
                
                if not history:
                    print(f'  {red}History is empty!\n  No passwords saved yet.{reset}\n')
                else:
                    for i, pwd in enumerate(history, 1):
                        # Number ke sath password dikhayega (e.g., 1. A#b79kL)
                        print(f'  {green}{i}. {pwd}{reset}')
                        
                choice = input(f'\n  [Enter] Go Back\n  {bg_red}[c]{reset} Clear History | ').strip().lower()
                
                if choice == 'c':
                    history.clear()
                    with open('passEngineHistory.txt', 'w') as file:
                        pass # File khali kar di
                    print(f'  {green}History Cleared!{reset}')
                    input(f'\n  {bg_red} [Enter] Continue {reset}')
                    break
                elif choice == '':
                    break
                else:
                    print(f'  {red}Use [c] or [Enter]{reset}')
                    input(f'\n  {bg_red}[Enter] Try Again{reset}')
            continue

        # Agar input 'q' ya 'h' nahi tha, toh iska matlab user ne number daala hai
        length = int(user_input)
        
        # Security checks
        if length < 4:
            print(f'  {red}At least 4 characters long!{reset}')
            input(f'\n  {bg_red} [Enter] Try Again {reset}')
            continue
        elif length > 1000:
            print(f'  {red}Too long! Maximum length is 1000.{reset}')
            input(f'\n  {bg_red} [Enter] Try Again {reset}')
            continue

    except ValueError:
        print(f'  {red}Enter a number, "h", or "q".{reset}')
        input(f'\n  {bg_red} [Enter] Try Again {reset}') 
        continue

    # --- PASSWORD GENERATION LOGIC ---
    letters = string.ascii_letters 
    numbers = string.digits        
    symbols = "!@#$%^&*()-_=+"     
    all_chars = letters + numbers + symbols

    password = ""
    for _ in range(length):
        password += random.choice(all_chars)

    # --- SAVE TO HISTORY ---
    history.append(password)
    with open('passEngineHistory.txt', 'a') as file:
        file.write(password + '\n')

    # --- RESULT PRINTING ---
    print(f'  ___________________________')
    print(f'\n  {green}Password genrated: {bg_red} {password} {reset}')
    input(f'\n  {red}Press [Enter] To Generate Another {reset}')
