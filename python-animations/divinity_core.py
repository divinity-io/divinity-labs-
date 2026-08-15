import time
import random
import os
import sys

# Colors
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
PURPLE = "\033[1;35m"
YELLOW = "\033[1;33m"
RED = "\033[1;31m"
RESET = "\033[0m"
BOLD = "\033[1m"

os.system("clear")

logo = f"""
{CYAN}{BOLD}
██████╗ ██╗██╗   ██╗██╗███╗   ██╗██╗████████╗██╗   ██╗
██╔══██╗██║██║   ██║██║████╗  ██║██║╚══██╔══╝╚██╗ ██╔╝
██║  ██║██║██║   ██║██║██╔██╗ ██║██║   ██║    ╚████╔╝ 
██║  ██║██║╚██╗ ██╔╝██║██║╚██╗██║██║   ██║     ╚██╔╝  
██████╔╝██║ ╚████╔╝ ██║██║ ╚████║██║   ██║      ██║   
╚═════╝ ╚═╝  ╚═══╝  ╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝      ╚═╝   
{RESET}
"""

print(logo)

print(f"{PURPLE}CODE FIRST • SECURITY ALWAYS • IMPACT FOREVER{RESET}\n")

time.sleep(1)

systems = [
    "Initializing Divinity Core...",
    "Loading developer environment...",
    "Scanning security layers...",
    "Connecting GitHub modules...",
    "Optimizing performance...",
    "System ready."
]

for item in systems:
    print(f"{GREEN}▶ {item}{RESET}")
    time.sleep(0.7)

print()

chars = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(25):
    line = "".join(random.choice(chars) for _ in range(55))
    print(f"{CYAN}{line}{RESET}")
    time.sleep(0.08)

print()

for i in range(4):
    print(f"{YELLOW}⚡ CYBER PULSE {'█' * (i+1)}{RESET}")
    time.sleep(0.4)

print()

print(f"""
{GREEN}
╔════════════════════════════════════╗
║        DIVINITY CORE ONLINE        ║
║                                    ║
║  Developer: divinity-io             ║
║  Mode: Mobile Development          ║
║  Security: Enabled                 ║
║  Impact: Forever                   ║
╚════════════════════════════════════╝
{RESET}
""")
