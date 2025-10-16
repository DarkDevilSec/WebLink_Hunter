#!/usr/bin/env python3

import os
import sys
import time
from core import crawler, extractor, storage
from colorama import Fore, Style, init
from colorama import Fore, Style

init(autoreset=True)
DARK_RED = "\033[38;5;124m"
DARK_YELLOW = "\033[38;5;178m"

BANNER = f"""
{DARK_RED}
██╗    ██╗███████╗██████╗ ██╗     ██╗███╗   ██╗██╗  ██╗    ██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ 
██║    ██║██╔════╝██╔══██╗██║     ██║████╗  ██║██║ ██╔╝    ██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
██║ █╗ ██║█████╗  ██████╔╝██║     ██║██╔██╗ ██║█████╔╝     ███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
██║███╗██║██╔══╝  ██╔══██╗██║     ██║██║╚██╗██║██╔═██╗     ██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
╚███╔███╔╝███████╗██████╔╝███████╗██║██║ ╚████║██║  ██╗    ██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
{DARK_YELLOW}
🚀WebLink Hunter           |  Version: 1.0
🕵️ Author: Ashish Prajapati |  GitHub: https://github.com/DarkDevilSec/
🖥️ Fully CLI-Based          |  HTML Reports

{Fore.CYAN}🎯 Project Purpose:
{Fore.GREEN}WebLink Hunter is a CLI-based Web VAPT Link Harvester that helps penetration testers 
and security researchers identify, extract, and analyze all URLs (href, src, and form actions) 
from target web applications. The goal is to simplify web reconnaissance and automate 
link discovery for vulnerability assessments and reporting.
{Style.RESET_ALL}
"""
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input(f"\n{Fore.YELLOW}[>] Press Enter to continue...")

def main_menu():
    clear_screen()
    print(BANNER)
    print(f"{Fore.CYAN}[1]{Style.RESET_ALL} Extract all href links")
    print(f"{Fore.CYAN}[2]{Style.RESET_ALL} Extract all src links")
    print(f"{Fore.CYAN}[3]{Style.RESET_ALL} Extract all form actions")
    print(f"{Fore.CYAN}[4]{Style.RESET_ALL} Crawl target and get all (href/src/action)")
    print(f"{Fore.CYAN}[0]{Style.RESET_ALL} Exit\n")
    choice = input(f"{Fore.YELLOW}[?] Choose an option: {Style.RESET_ALL}")
    return choice.strip()

def get_target():
    target = input(f"{Fore.YELLOW}[?] Enter target URL: {Style.RESET_ALL}").strip()
    if not target.startswith("http"):
        target = "http://" + target
    return target

def main():
    while True:
        choice = main_menu()
        if choice == "0":
            print(f"\n{Fore.GREEN}[+] Exiting... Goodbye, White Devil!")
            sys.exit(0)

        target = get_target()
        print(f"\n{Fore.GREEN}[+] Starting scan for: {target}\n")
        time.sleep(1)

        try:
            links_dict = {"href": [], "src": [], "action": []}

            if choice == "1":
                links_dict["href"] = extractor.extract_links(target, "href")
            elif choice == "2":
                links_dict["src"] = extractor.extract_links(target, "src")
            elif choice == "3":
                links_dict["action"] = extractor.extract_links(target, "action")
            elif choice == "4":
                links_dict = crawler.crawl(target, max_depth=2)
            else:
                print(f"{Fore.RED}[!] Invalid choice. Try again.")
                pause()
                continue

            # Display results
            total_links = sum(len(v) for v in links_dict.values())
            print(f"\n{Fore.CYAN}[+] Total links found: {total_links}\n{'='*40}")
            for link_type, urls in links_dict.items():
                for link in urls:
                    print(f"{Fore.GREEN}[{link_type}] {link}")

            # Save HTML report
            storage.save(target, links_dict)

        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}")

        pause()

if __name__ == "__main__":
    main()
