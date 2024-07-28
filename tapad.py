import requests
import time
from colorama import Fore, Style, init
import json
import os
import random
import sys
init(autoreset=True)

def print_welcome_message():
    print(r"""
 __  __      __                   __                         
/\ \/\ \    /\ \                 /\ \                        
\ \ `\\ \   \_\ \     __     _ __\ \ \____     __     __     
 \ \ , ` \  /'_` \  /'__`\  /\`'__\ \ '__`\  /'__`\ /'_ `\   
  \ \ \`\ \/\ \L\ \/\ \L\.\_\ \ \/ \ \ \L\ \/\  __//\ \L\ \  
   \ \_\ \_\ \___,_\ \__/.\_\\ \_\  \ \_,__/\ \____\ \____ \
    \/\/_/\/__,_ /\/__/\/_/ \/\/   \/___/  \/____/\/___L\ \
                                                      /\_____/
                                                      \/__/ .bot
          """)

    print(f"{Fore.GREEN}TapAdventure{Fore.RESET}\n\n")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_credentials():
    try:
        with open('data.txt', 'r') as file:
            credentials_list = file.readlines()
        credentials = [cred.strip() for cred in credentials_list]
        return credentials
    except FileNotFoundError:
        print("File 'data.txt' tidak ditemukan. Pastikan file tersebut ada di direktori yang sama dengan script.")
        return []

def user_data(authorization):
    url = 'https://tapadventure.pixelheroes.io/api/init'
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'initdata': authorization,
        'origin': 'https://d2y873tmoumjr5.cloudfront.net',
        'priority': 'u=1, i',
        'referer': 'https://d2y873tmoumjr5.cloudfront.net/',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    data = {'platform': 'ios', 'locale': 'en', 'is_premium': False}
    try:
        response = requests.get(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error:", e)

def touch(authorization, token, touch):
    response = user_data(authorization)
    token = response['body']['authorization']
    url = 'https://tapadventure.pixelheroes.io/api/tapTouch'
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'Authorization': f'Bearer {token}',
        'initdata': authorization,
        'origin': 'https://d2y873tmoumjr5.cloudfront.net',
        'priority': 'u=1, i',
        'referer': 'https://d2y873tmoumjr5.cloudfront.net/',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    payload = {'touchCount': touch}
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Check if the request was successful
    except requests.exceptions.RequestException as e:
        print("Error: Unable to send touch request. Error message: ", e)

def main():
    clear_console()
    print_welcome_message()
    credentials = load_credentials()

    while True:
        for index, authorization in enumerate(credentials):
            info = user_data(authorization)
            print(f"{Fore.CYAN+Style.BRIGHT}============== [ Akun {index+1} ] ==============")
            if info:
                username = info.get('body').get('userName', '')
                usercoin = info.get('body').get('coin', '')
                lvl = info.get('body').get('level', '')
                energy = info.get('body').get('attackEnergy', '')
                print(Fore.GREEN + Style.BRIGHT + f"User Name: {username}")
                print(Fore.GREEN + Style.BRIGHT + f"User Coin: {usercoin}")
                print(Fore.GREEN + Style.BRIGHT + f"Level: {lvl}")
                print(Fore.GREEN + Style.BRIGHT + f"Attack Energy: {energy}")
                response = user_data(authorization)
                token = response['body']['authorization']
                while True:
                    time.sleep(2)
                    tap = random.randint(100, 250)
                    touch(authorization, token, tap)
                    print(Fore.RED + Style.BRIGHT + f"Sisa Energy: {energy}")
                    energy -= tap
                    if energy <= 100:
                        print(Fore.RED + Style.BRIGHT + f"Energy Kurang Dari 100!!")
                        break
            else :
                print("\r{Fore.RED+Style.BRIGHT}Token akses tidak valid, lanjut ke akun berikutnya.") 
        time.sleep

        print(f"{Fore.CYAN+Style.BRIGHT}==============Semua akun telah diproses=================")
        for i in range(300, 0, -1):
            sys.stdout.write(f"\rMemproses ulang semua akun dalam {i} detik...")
            sys.stdout.flush()
            time.sleep(1)
        print("Mari Kita Mulai Lagi")

        clear_console()
if __name__ == "__main__":
    main()