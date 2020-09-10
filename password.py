# -*- coding:utf-8 -*-
# Password-Generator
# developed by Jiyan Fontaine
# September 2020, Germany

import string
import random
from termcolor import colored
import pyfiglet

ascii_banner = pyfiglet.figlet_format("≠Password≠ \n≠Generator≠")
print(ascii_banner)
print(colored("¢[*] @by Jiyan Fontaine", 'yellow'))

min_lenght = input(
    colored("[*] Enter Minimum Lenght Of The Password : ", 'blue'))
max_lenght = input(
    colored("[*] Enter Maximum Lenght Of The Password : ", 'blue'))


def generate_password():
    try:
        chars = string.ascii_letters + string.digits + string.punctuation
        print("You Generated Password : " + colored(''.join(random.choice(chars)
                                                            for _ in range(int(min_lenght), int(max_lenght))), 'green'))
    except Exception:
        return Exception


generate_password()
