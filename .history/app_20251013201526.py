import utilities as util
import yara
import os

def main():
    yara_rules_dict = util.get_yara_rules('.\\yararules')
    print(yara_rules_dict)

    if os.path.exists('.//yararules//yara_compiled_rules'):
        rules = yara.load('.//yararules//yara_compiled_rules')

    else:    
        compiled_rules = yara.compile(fileaths=yara_rules_dict, error_on_warnin=False)
        compiled_rules.save('.//yararules//yara_compiled_rules')

if __name__ == "__main__":
    main()
