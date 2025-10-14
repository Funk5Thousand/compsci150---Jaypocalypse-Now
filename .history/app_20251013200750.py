import utilities as util

def main():
    yara_rules_dict = util.get_yara_rules('.\\yararules')
    print(yara_rules_dict)


    compiled_rules = yara.compile

if __name__ == "__main__":
    main()
