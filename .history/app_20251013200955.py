import utilities as util
import yara


def main():
    yara_rules_dict = util.get_yara_rules('.\\yararules')
    print(yara_rules_dict)


    compiled_rules = yara.compile(fileaths=yara_rules_dict, error_on_warnin=True)
    rules.save('.//yara

if __name__ == "__main__":
    main()
