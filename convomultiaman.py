AMAN-10292DS10292
AMAN-ca8dc066-1ee9-4024-8e07-cf2676798c8d
AMAN-c7d0323f-47d5-4384-b8c1-62ae7727f922
AMAN-fd86365d-c882-49b2-9c04-edf3d005938
AMAN-10292DS10292
AMAN-10361DS10361
import requests
import time
import random
import os
import sys
from colorama import init, Fore

init(autoreset=True)

def approval():
    os.system('git pull')  # Update tool
    time.sleep(1)
    uuid = str(os.geteuid()) + 'DS' + str(os.geteuid())
    id = 'AMAN-' + ''.join(uuid)
    os.system('clear')

    logo = r'''
     ##     ##   ##    ##     ##  ##  
   ####    ### ###   ####    ### ##  
  ##  ##   #######  ##  ##   ######  
  ######   ## # ##  ######   ######  
  ##  ##   ##   ##  ##  ##   ## ###  
  ##  ##   ##   ##  ##  ##   ##  ##  
  ##  ##   ##   ##  ##  ##   ##  ##  
                                    
  $$$$$$\                  $$$$$$$$\ $$\                     
 $$  __$$\                 $$  _____|\__|                    
 $$ /  $$ |$$$$$$$\        $$ |      $$\  $$$$$$\   $$$$$$\  
 $$ |  $$ |$$  __$$\       $$$$$\    $$ |$$  __$$\ $$  __$$\ 
 $$ |  $$ |$$ |  $$ |      $$  __|   $$ |$$ |  \__|$$$$$$$$ |
 $$ |  $$ |$$ |  $$ |      $$ |      $$ |$$ |      $$   ____|
  $$$$$$  |$$ |  $$ |      $$ |      $$ |$$ |      \$$$$$$$\ 
  \______/ \__|  \__|      \__|      \__|\__|       \_______|
    '''

    print(logo)
    print(Fore.WHITE + ' [\x1b[36m•\x1b[1;37m] You Need Approval To Use This Tool')
    print(Fore.WHITE + ' [\x1b[36m•\x1b[1;37m] Your Key :\x1b[36m ' + id)
    time.sleep(0.1)
    print('----------------------------------------------')
    try:
        httpCaht = requests.get('https://github.com/SANDHU880/amanpost1/blob/main/aman.txt').text
        if id in httpCaht:
            print(Fore.GREEN + ' >> Your Key Has Been Approved !!!')
            time.sleep(1)
        else:
            print(Fore.RED + ' >> Sorry Your Key Has Not Been Approved ')
            time.sleep(0.1)
            input('IF YOU WANT TO BUY THEN PRESS ENTER ')
            tks = 'Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20' + id
            os.system('am start https://wa.me/+918700850020?text=' + tks)
            time.sleep(1)
            sys.exit(0)  # Exit gracefully after user interaction
    except requests.exceptions.RequestException as e:
        print(Fore.RED + str(e))
        print(Fore.RED + ' >> Unable To Fetch Data From Server ')
        time.sleep(2)
        sys.exit(1)  # Exit with error code

def send_messages(tokens_file, target_id, messages_file, haters_name, speed):
    with open(messages_file, "r") as file:
        messages = file.readlines()
    with open(tokens_file, "r") as file:
        tokens = file.readlines()

    headers = {
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": ("Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36"),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,fr;q=0.8",
        "Referer": "www.google.com",
    }

    while True:
        for message_index, message in enumerate(messages):
            token_index = message_index % len(tokens)
            access_token = tokens[token_index].strip()
            full_message = f"{haters_name} {message.strip()}"

            url = f"https://graph.facebook.com/v17.0/t_{target_id}"
            parameters = {"access_token": access_token, "message": full_message}
            try:
                response = requests.post(url, json=parameters, headers=headers)
                response.raise_for_status()
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                current_logo = random.choice(logos)
                print(Fore.GREEN + current_logo)
                print(Fore.YELLOW + f"[+] XM9RTY AM9N K1NG {message_index + 1} S3NT TO C0NV0 {target_id} W1TH TOK3N {token_index + 1}: {full_message} at {current_time}")
            except requests.exceptions.RequestException as e:
                print(Fore.RED + f"[x] F91L3D TO S3ND M3SS3G3  {message_index + 1} T0 C0NV0 {target_id} W1TH TOK3N {token_index + 1}: {full_message} - Error: {e}")

            time.sleep(speed)
        print(Fore.CYAN + "\n[+] All messages sent. Restarting the process...\n")

def main():
    approval()

    print(Fore.MAGENTA + " XM9RTY AM9N K1NG TOOL ")
    print(Fore.CYAN + "------------------------------------")
    # Get file paths and other inputs from the user
    tokens_file = input(Fore.YELLOW + "Enter the path to the tokens file: ").strip()
    target_id = input(Fore.YELLOW + "Enter the target_id: ").strip()
    messages_file = input(Fore.YELLOW + "Enter the path to the messages file: ").strip()
    haters_name = input(Fore.YELLOW + "Enter the hater's name: ").strip()
    speed = float(input(Fore.YELLOW + "Enter the speed (in seconds) between messages: ").strip())

    # Start sending messages
    send_messages(tokens_file, target_id, messages_file, haters_name, speed)

if __name__ == "__main__":
    main()
