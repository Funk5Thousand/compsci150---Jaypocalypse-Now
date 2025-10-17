import utilities as util
import yara
import os
import psutil

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
    files_to_scan = util.get_all_files("C:\\")
    for file in files_to_scan:
        try:
            matches = compiled_rules.match(file)

        except Exception as e:
            print(f"An error occurred: {e}")
            pass
    for match in matches:
        for item in match:
            print(str(item))
def scan_processes():
    compiled_rules = util.get_compiled_rules()
    pids = util.get_process_pids()
    for id in pids:
        matches = compiled_rules.match(pid=id)


if __name__ == "__main__":
    main()
