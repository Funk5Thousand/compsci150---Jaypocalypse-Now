import utilities as util
import yara
import os

def main():


    if os.path.exists('.//yararules//yara_compiled_rules'):
        compiled_rules = yara.load('.//yararules//yara_compiled_rules')
    

    else:    
        yara_rules_dict = util.get_yara_rules('.\\yararules')
        compiled_rules = yara.compile(filepaths=yara_rules_dict)
        compiled_rules.save('.//yararules//yara_compiled_rules')

    files_to_scan = util.get_all_files("C:\\")
    for file in files_to_scan:
        try:
            matches = compiled_rules.match(file)
            print("Blank_stuff")
        except as e(e):
if __name__ == "__main__":
    main()
