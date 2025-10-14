import os

def get_yara_rules(yara_directory):
    """
    Load YARA rules from the 'yara_rules' directory.

    Returns:
        list: A list of YARA rule file paths.
   """
    yara_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                yara_files.append(os.path.join(root, file))

