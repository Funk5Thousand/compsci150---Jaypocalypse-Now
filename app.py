import utilities as util
import yara
import os
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
    compiled_rules = util.get_compiled_rules()
    matches = []
    partitions = psutil.disk_partitions()
    for p in partitions:
        files_to_scan = util.get_all_files(p.device)
        for file in files_to_scan:
            spinner_message = 'Scanning file system. File: ' + str(file)
            with Halo(text=spinner_message, spinner='dots', text_color = 'magenta', animation = 'bounce'):
            
                try:
                    matches = compiled_rules.match(file)

                except Exception as e:
                    print(f"An error occurred: {e}")
                    pass
    for match in matches:
        for item in match:
            print(str(item))
    

def scan_processes():
    with Halo(text='Scanning system processes...', spinner='dots', text_color = 'magenta', animation = 'bounce'):
        compiled_rules = util.get_compiled_rules()
        pids = util.get_process_pids()
        for id in pids:
            spinner_message = 'Scanning systen processes. Process #: ' + str(id)
            with Halo(text=spinner_message, spinner='dots', text_color = 'magenta', animation = 'bounce'):
                matches = compiled_rules.match(pid=id)
    

if __name__ == "__main__":
    main()
