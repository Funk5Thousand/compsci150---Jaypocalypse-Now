import os
import psutil
import yara
from halo import Halo
import vt

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


def get_all_files():
    
    partitions = psutil.disk_partitions()
    all_files_list = []
    for p in partitions:
        for root, _, files in os.walk(p.device):
            for file in files:
                all_files_list.append(os.path.join(root, file))
    return all_files_list


def get_process_pids():
    return psutil.pids()

def get_compiled_rules():
    spinner = Halo(text='Compiling Yara Rules', spinner='dots')
    spinner.text_color = 'blue'
    spinner.start()
    

    if os.path.exists('.//yararules//yara_compiled_rules'):
        compiled_rules = yara.load('.//yararules//yara_compiled_rules')
    

    else:    
        yara_rules_dict = get_yara_rules_paths('.\\yararules')
        compiled_rules = yara.compile(filepaths=yara_rules_dict)
        compiled_rules.save('.//yararules//yara_compiled_rules')
    spinner.stop()
    return compiled_rules

def calculate_file_hash(file_path):
    sha256_hasher = hashlib.sha256()
    with open(file_path, "rb") as file:
              for chunk in iter(lambda: file.read(4096, b"")):
                sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

def confirm_yara_positive(sha256_hash):
    client = vt.Client("b4d2415ad3800d703b579ed15ae38108f51354156d918b46f2ebda36142285df")
    file_string = "/files/" + sha256_hash
    file = client.get_object(file_string)
    if file.last_analysis_stats["malicious"] > 3:
        return True
    else:
        return False