import utilities as util
import yara
import os
from tqdm import tqdm
import psutil
from halo import Halo
import sys
import atexit
import keyboard
from io import StringIO
def main():
    
    
    global saved_state_flag
    global high_water_mark_file
    high_water_mark_file = " " 
    saved_state_flag = False
    atexit.register(save_progress_on_exit)
    message1 ='''
        Welcome, What would you like to do? Enter the number for your choice.
                          
        1) Scan the file system.
        2) Scan the active running processes.
        3) Scan the entire system.

'''
    message2 = '''

         Welcome, What would you like to do? Enter the number for your choice.
                          
        1) Scan the file system.
        2) Scan the active running processes.
        3) Scan the entire system.
        4) Continue with an in progress scan                 
                          
                           
                             '''
    if os.path.exists('scan_saved_progress_file'):
        with open("scan_saved_progress_file", "r") as f:
            high_water_mark_file = f.readline()
        greet_user(message2)
    else:
         greet_user(message1)
    
    
def greet_user(message):    
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("Welcome to CompSci 150 Malware Scanner")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    
    user_response = input(message)
     
                    
    if user_response == '1':
            scan_file_system()
    elif user_response == '2':
            scan_processes()
    elif user_response == '3':
            scan_file_system()
            scan_processes()
    elif user_response == '4':
           saved_state_flag = True
           scan_file_system()
    else:
            print("That selection does not exist")


def scan_file_system():
    global saved_state_flag
         
    with Halo(text="Gathering file system file data. Once scanning begins, press escape to exit.", spinner='dots', text_color = 'magenta', animation = 'bounce'):
        compiled_rules = util.get_compiled_rules()
        files_to_scan = util.get_all_files()
        if saved_state_flag == True:
             if high_water_mark_file in files_to_scan:
                  high_water_mark_index = files_to_scan.index(high_water_mark_file)
                  temporary_file_list = files_to_scan[high_water_mark_index:]
                  files_to_scan = temporary_file_list
                  saved_state_flag = False
        files_to_scan = tqdm(files_to_scan)
    matches = []
    for file in files_to_scan:
        high_water_mark_file = file
        if keyboard.is_pressed('esc'):
             sys.exit()
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

def save_progress_on_exit():

    line_to_write = high_water_mark_file
    with open("scan_saved_progress_file", "w") as f:
         f.write(line_to_write)


def error_handler(message):
     if "An error occurred: could not open file" in message:
          return 
     else:
          print(message)

if __name__ == "__main__":
    main()
