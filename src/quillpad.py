import json
import os

from colorama import Fore

bad_char_list = "/\\?%*:|\"<>.;="

def export(file_dictionary: dict, export_directory: str):
    notebook_dirs: dict = {}

    default_dir = f"{export_directory}/default"
    if not os.path.exists(default_dir):
        os.makedirs(default_dir)
    
    for notebook in file_dictionary["notebooks"]:
        
        print(f":: Exporting: {Fore.BLUE}{notebook['name']}{Fore.RESET}")
        notebook_directory: str = f"{export_directory}/{notebook['name']}"
        
        if not os.path.exists(notebook_directory):
            os.makedirs(notebook_directory)
        notebook_dirs[notebook["id"]] = notebook_directory

    for notes in file_dictionary["notes"]:
        try:
            export_dir = notebook_dirs[int(notes["notebookId"])]
        except:
            export_dir = default_dir

        if "content" in notes:
            title = notes.get("title", str(notes.get("creationDate","no title")))
 
            for bad_char in bad_char_list:
                title.replace(bad_char, "")
            
            export_path: str = f"{export_dir}/{title}.md"
            
            print(f":: Saving {Fore.YELLOW}{title}{Fore.RESET} to {export_path}")
            with open(export_path, "w") as note_file:
                note_file.write(notes["content"])

if __name__ == "__main__":
    for char in bad_char_list:
        print(char)