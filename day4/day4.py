import re

input = open("day4_input.txt").read().split("\n\n")
input = [sub.replace("\n", " ") for sub in input]

def checkPassports(passports):
    valid_passports = []
    for passport in passports:
        passport_invalid = False
        required_fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
        for field in required_fields:
            if field not in passport:
                passport_invalid = True
        if passport_invalid == False:
            valid_passports.append(passport)
    return valid_passports

valid_passports = checkPassports(input)

def convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct

def preprocessor(passports):
    processed_passports = []
    for el in passports:
        el = el.replace(" ", ":")
        el = el.split(":")
        el = convert(el)
        processed_passports.append(el)
    return processed_passports

formatted_passports = preprocessor(valid_passports)

def doubleCheckPassports(passports):
    valid_passports = []
    hcl_pattern = r"^\#[\da-f]{6}$"
    ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    pid_pattern = r"^\d{9}$"
    for passport in passports:
        passport_invalid = False
        if (2002 < int(passport["byr"])) or (int(passport["byr"]) < 1920):
            passport_invalid = True
        if (2020 < int(passport["iyr"])) or (int(passport["iyr"]) < 2010):
            passport_invalid = True
        if (2030 < int(passport["eyr"])) or (int(passport["eyr"]) < 2020):
            passport_invalid = True
        if "cm" in passport["hgt"]:
            if (193 < int(passport["hgt"].rstrip("cm"))) or (int(passport["hgt"].rstrip("cm")) < 150):
                passport_invalid = True
        elif "in" in passport["hgt"]:
            if (76 < int(passport["hgt"].rstrip("in"))) or (int(passport["hgt"].rstrip("in")) < 59):
                passport_invalid = True
        else:
            passport_invalid = True    
        if not (re.search(hcl_pattern, passport["hcl"])):
            passport_invalid = True
        if passport["ecl"] not in ecl:
            passport_invalid = True
        if not (re.search(pid_pattern, passport["pid"])):
            passport_invalid = True
        if passport_invalid == False:
            valid_passports.append(passport)
    return len(valid_passports)

print(doubleCheckPassports(formatted_passports))