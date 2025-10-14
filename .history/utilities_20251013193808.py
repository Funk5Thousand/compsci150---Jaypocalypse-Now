import os

def get_yara_rules(yara_directory):
    """
    Load YARA rules from the 'yara_rules' directory.

    Returns:
        list: A list of YARA rule file paths.
   """
    yara_files = {}
    i = 1
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".yar"):
                yara_files["yara_rule" + str(i)]
                