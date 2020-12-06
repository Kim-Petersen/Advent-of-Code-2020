import re

with open('./passport data.txt') as f:
    passport_data = f.read()

passport_data = passport_data.split('\n\n')
passport_data = [x.replace('\n', ' ') for x in passport_data]

passport_dicts = [dict(s.split(':', 1) for s in passport.split(' ') if ':' in s) for passport in passport_data]


def passport_has_required_keys(d):
    required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for i in required_keys:
        if i in d:
            pass
        else:
            return False
    return True


passports_req_keys = list(filter(passport_has_required_keys, passport_dicts))

print(len(passports_req_keys))


def has_valid_byr(d):
    byr = int(d['byr'])
    return byr >= 1920 and byr <= 2002


def has_valid_iyr(d):
    iyr = int(d['iyr'])
    return iyr >= 2010 and iyr <= 2020


def has_valid_eyr(d):
    eyr = int(d['eyr'])
    return eyr >= 2020 and eyr <= 2030


def has_valid_hgt(d):
    hgt_s = d['hgt']
    try:
        hgt, unit = re.search('([0-9]+)(cm|in)', hgt_s).groups()
        hgt = int(hgt)
    except AttributeError:
        return False
    if unit == 'cm' and hgt >= 150 and hgt <= 193:
        return True
    elif unit == 'in' and hgt >= 59 and hgt <= 76:
        return True
    else:
        return False


def has_valid_hcl(d):
    hcl = d['hcl']
    if re.search('#[0-9a-f]{6}', hcl):
        return True
    else:
        return False


def has_valid_ecl(d):
    ecl = d['ecl']
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def has_valid_pid(d):
    pid = d['pid']
    if re.search('[0-9]{9}', pid):
        return True
    else:
        return False


def passport_has_valid_values(d):
    validity_checks = [has_valid_byr,
                       has_valid_iyr,
                       has_valid_eyr,
                       has_valid_hgt,
                       has_valid_hcl,
                       has_valid_ecl,
                       has_valid_pid]

    return all([f(d) for f in validity_checks])


print(len(list(filter(passport_has_valid_values, passports_req_keys))))