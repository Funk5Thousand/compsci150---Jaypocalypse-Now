import os
import psutil
import yara
def get_yara_rules_paths(yara_directory):
    """
    Load YARA rules from the 'yara_rules' directory.

    Returns:
        list: A dictionary of YARA rule file paths.
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
        list: A list of all the files on a computer
   """
    all_files_list = []
    for root, _, files in os.walk(drive_root):
        for file in files:
            all_files_list.append(os.path.join(root, file))
    return all_files_list


def get_process_pids():
    return psutil.pids()

def get_compiled_rules():
    if os.path.exists('.//yararules//yara_compiled_rules'):
        compiled_rules = yara.load('.//yararules//yara_compiled_rules')
    

    else:    
        yara_rules_dict = get_yara_rules_paths('.\\yararules')
        compiled_rules = yara.compile(filepaths=yara_rules_dict)
        compiled_rules.save('.//yararules//yara_compiled_rules')
    return compiled_rules