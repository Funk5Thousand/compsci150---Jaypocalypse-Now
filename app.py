import utilities as util
import yara
import os
from tqdm import tqdm
import psutil
from halo import Halo
def main():


    print("Welcome to CompSci 150 Malware Scanner")
    print(" ")

    user_response = input('''
          Welcome, What would you like to do? Enter the number for your choice.
                          
        1) Scan the file system.
        2) Scan the active running processes.
        3) Scan the entire system.
                          
                        ''')
    if user_response == '1':
            scan_file_system()
    elif user_response == '2':
            scan_processes()
    elif user_response == '3':
            scan_file_system()
            scan_processes()
    else:
            print("That selection does not exist")


def scan_file_system():
    with Halo(text="Gathering file system file data", spinner='dots', text_color = 'magenta', animation = 'bounce'):
        compiled_rules = util.get_compiled_rules()
        files_to_scan = tqdm(util.get_all_files())
    matches = []
    for file in files_to_scan:
        base_file = os.path.basename(file)
        message = "Scanning file: " + str(base_file[:15]).ljust(20)
        files_to_scan.set_description(message)
        try:
            matches = compiled_rules.match(file, console_callback=error_handler)

        except Exception as e:
            print(f"An error occurred: {e}")
            pass
    for match in matches:
        for item in match:
            print(str(item))


def scan_processes():
    compiled_rules = util.get_compiled_rules()
    pids = util.get_process_pids()
    for id in tqdm(pids):
            matches = compiled_rules.match(pid=id)


def error_handler(message):
     if "An error occurred: could not open file" in message:
          return 
     else:
          print(message)

if __name__ == "__main__":
    main()
