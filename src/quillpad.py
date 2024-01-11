import json

from colorama import Fore


def export(file_dictionary):
    for notebook in file_dictionary["notebooks"]:
        print(f":: Exporting: {Fore.BLUE}{notebook['name']}{Fore.RESET}")
