import json
import os

from colorama import Fore


def export(file_dictionary: dict, export_directory: str):
    for notebook in file_dictionary["notebooks"]:
        print(f":: Exporting: {Fore.BLUE}{notebook['name']}{Fore.RESET}")

    for notes in file_dictionary["notes"]:
        if "content" in notes:
            print(f":: Exporting: {Fore.YELLOW}{notes['title']}{Fore.RESET}")
            note_file_path: str = f"{notes['title'].upper().replace(' ', '_')}.md"

            for notebook in file_dictionary["notebooks"]:
                notebook_identities = {notebook["id"]: notebook["name"]}
                for notebook_id, notebook_name in notebook_identities.items():
                    notebook_directory: str = f"{export_directory}/{notebook_name}"

                    if not os.path.exists(notebook_directory):
                        os.makedirs(notebook_directory)

                    export_path: str = f"{notebook_directory}/{note_file_path}"
                    print(f":: Saving to {export_path}")
                    if int(notes["notebookId"]) == notebook_id:
                        print(f"{notebook_id} - {notebook_name} - {notes['title']}")
                        with open(export_path, "w") as note_file:
                            note_file.write(notes["content"])
