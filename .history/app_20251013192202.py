import os

def get_yara_rules():
    """
    Load YARA rules from the 'yara_rules' directory.

    Returns:
        list: A list of YARA rule file paths.
   """
    yara_files = []
    