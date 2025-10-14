import os

def get_yara_rules(yara_directory):
    """
    Load YARA rules from the 'yara_rules' directory.

    Returns:
        list: A list of YARA rule file paths.
   """
    yara_files = {}
    i = 1
    for root, _, files in os.walk(yara_directory):
        for file in files:
            if file.endswith(".yar"):
                yara_files["yara_rule" + str(i)] = (os.path.join(root, file))
                i += 1
    return yara_files


def get_all_files(drive_root):
    """
    Load YARA rules from the 'yara_rules' directory.

    Returns:
        list: A list of YARA rule file paths.
   """
    yara_files = []
    for root, _, files in os.walk(drive_root):
        for file in files:
            if file.endswith(".yar"):
                yara_files["yara_rule" + str(i)] = (os.path.join(root, file))
                i += 1
    return yara_files