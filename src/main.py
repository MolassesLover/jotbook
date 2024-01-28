import argparse
import json
import os
import yaml

from colorama import Fore
from dataclasses import dataclass

import quillpad


@dataclass
class file_extension:
    suffix: str


def log_error(error_string: str, print_help: bool = False, argument_parser=None):
    error_message: str = f":: {Fore.RED}Error{Fore.RESET}: {error_string}"
    print(error_message)

    if print_help:
        argument_parser.print_help()
    else:
        raise NotImplementedError(error_string)


def open_file(file: str) -> dict:
    extension: extension_suffix = get_extension(file)

    with open(file, "r") as file_data:
        match str(extension.suffix):
            case ".json":
                file_dictionary: dict = json.load(file_data)
            # case ".yml":
            # case ".yaml":
            case _:
                log_error(f"Extension {extension.suffix} is not supported.")
    return file_dictionary


def get_extension(file: str) -> file_extension:
    extension_suffix: str = os.path.splitext(file)[1]

    extension = file_extension(extension_suffix)
    return extension


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--file", "-f", type=str, required=True)
    argument_parser.add_argument("--type", "-t", type=str, required=True)
    argument_parser.add_argument("--export", "-e", action="store_true")
    argument_parser.add_argument("--export-dir", "-p", type=str)
    arguments = argument_parser.parse_args()

    backup_file: dict = open_file(arguments.file)

    if arguments.export_dir:
        export_dir: str = arguments.export_dir
    else:
        export_dir: str = "export"

    if arguments.export:
        match str(arguments.type).lower():
            case "quillpad":
                quillpad.export(backup_file, export_dir)
            case _:
                log_error(f"Must provide a type when converting.")
