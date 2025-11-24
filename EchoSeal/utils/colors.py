from colorama import Fore, Style, init

init(autoreset=True)

class Colors:
    HEADER = Fore.CYAN + Style.BRIGHT
    OK = Fore.GREEN + Style.BRIGHT
    WARN = Fore.YELLOW + Style.BRIGHT
    FAIL = Fore.RED + Style.BRIGHT
    RESET = Style.RESET_ALL