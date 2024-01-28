import json
import os

from colorama import Fore

def export(file_dictionary: dict, export_directory: str):
    notebook_dirs: dict = {}

    # make directory for default notes
    default_dir = f"{export_directory}/default"
    if not os.path.exists(default_dir):
        os.makedirs(default_dir)
    
    # make directory for each notebook
    for notebook in file_dictionary["notebooks"]:
        
        print(f":: Exporting: {Fore.BLUE}{notebook['name']}{Fore.RESET}")
        notebook_directory: str = f"{export_directory}/{notebook['name']}"
        
        if not os.path.exists(notebook_directory):
            os.makedirs(notebook_directory)
        notebook_dirs[notebook["id"]] = notebook_directory

    #iterate over each note file and save it
    for notes in file_dictionary["notes"]:
        try:
            export_dir = notebook_dirs[int(notes["notebookId"])]
        except:
            export_dir = default_dir

        title = notes.get("title", str(notes.get("creationDate","no title")))

        # Remove characters not allowed in file names
        bad_char_list = "/\\?%*:|\"<>.;="
        for bad_char in bad_char_list:
            title = title.replace(str(bad_char), "")
        
        export_path: str = f"{export_dir}/{title}.md"
        
        note_text: str = ""
        if "content" in notes:    
            note_text = notes["content"]
        
        elif "taskList" in notes:
            for item in notes["taskList"]:
                if item["isDone"]:
                    note_text += f"- [x] {item.get('content', '')}\n"
                else:
                    note_text += f"- [ ] {item.get('content', '')}\n"
            
        print(f":: Saving {Fore.YELLOW}{title}{Fore.RESET} to {export_path}")
        with open(export_path, "w") as note_file:
            note_file.write(note_text)