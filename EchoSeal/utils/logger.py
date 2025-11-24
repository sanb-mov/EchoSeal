from .colors import Colors
import datetime

def log(message, level="INFO"):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    if level == "INFO":
        print(f"[{timestamp}] {Colors.OK}[+] {message}{Colors.RESET}")
    elif level == "WARN":
        print(f"[{timestamp}] {Colors.WARN}[!] {message}{Colors.RESET}")
    elif level == "ALERT":
        print(f"[{timestamp}] {Colors.FAIL}[XXX] {message}{Colors.RESET}")
    elif level == "HEADER":
        print(f"\n{Colors.HEADER}=== {message} ==={Colors.RESET}")