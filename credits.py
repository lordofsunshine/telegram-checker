import colorama
from colorama import Fore, Style

colorama.init()

def print_header():
    header = f"""
{Fore.BLUE}
 ▄▄▄·▄▄▌   ▄▄▄·  ▐ ▄ ▄▄▄ .▄▄▄▄▄▄• ▄▌.▄▄ · 
▐█ ▄███•  ▐█ ▀█ •█▌▐█▀▄.▀·•██  █▪██▌▐█ ▀. 
 ██▀·██▪  ▄█▀▀█ ▐█▐▐▌▐▀▀▪▄ ▐█.▪█▌▐█▌▄▀▀▀█▄
▐█▪·•▐█▌▐▌▐█ ▪▐▌██▐█▌▐█▄▄▌ ▐█▌·▐█▄█▌▐█▄▪▐█
.▀   .▀▀▀  ▀  ▀ ▀▀ █▪ ▀▀▀  ▀▀▀  ▀▀▀  ▀▀▀▀ 
{Style.RESET_ALL}
"""
    print(header)
    print(f"{Fore.GREEN}Участвуем в розыгрыше LolzTeam :D{Style.RESET_ALL}")
    print("\n")

if __name__ == "__main__":
    print_header()
