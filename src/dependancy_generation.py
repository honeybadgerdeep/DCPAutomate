import sys
import shutil

# This code is responsible for generating and populating necessary source and test dependancies for projects.

"""
Overall application flow:
- begins with an init phase: prompt user asking whichever languages are being called and populate with boilerplate files

1. Read a JSON file
2. Based on the JSON file, populate the files with features
3. 
"""

def build_file_name(base_name, language):
    file_name = base_name

    # The following languages require capitalization support
    capitalization = {
        "java": True
    }

    if (language in capitalization):
        file_name = file_name.capitalize()

    # Some languages do not have the same extension as the language name in lowercase
    extension = {
        "python": "py"
    }

    file_name += "." + extension.get(language, language)

    return file_name


def copy_file(from_path, dest_path, file_name=""):
    try:
        shutil.copy(from_path + file_name, dest_path + file_name)
    except:
        print("Error copying file.")
    else:
        print("SUCCESS: Processed dependancy request with copy")

# Initialize files according to the programming language content parameters.
def init(language_params):
    language = language_params[0]
    dest_dir = language_params[1] + "/"
    from_dir = "boilerplates/" + language + "/"
    file_name = build_file_name("solution", language)

    copy_file(from_dir, dest_dir, file_name)

if __name__ == "__main__":
    args = sys.argv
    if [sys.argv[1] == "init"]:
        init(sys.argv[2:])