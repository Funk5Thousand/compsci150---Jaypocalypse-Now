import utilities as util
import yara
import os

def main():
    yara_rules_dict = util.get_yara_rules('.\\yararules')


    if os.path.exists('.//yararules//yara_compiled_rules'):
        rules = yara.load('.//yararules//yara_compiled_rules')

    else:    
        compiled_rules = yara.compile(filepaths=yara_rules_dict)
        compiled_rules.save('.//yararules//yara_compiled_rules')

if __name__ == "__main__":
    main()
