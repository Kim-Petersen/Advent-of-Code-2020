import re
import logging

logging.basicConfig(level=logging.INFO)

with open('./passport data.txt') as f:
    passport_data = f.read()

passport_data = passport_data.split('\n\n')

for index, passport in enumerate(passport_data):
    passport_data[index] = passport.replace('\n', ' ')


def validate_passport(passport, f=1):
    logging.debug(passport)

    has_byr = 'byr' in passport
    has_iyr = 'iyr' in passport
    has_eyr = 'eyr' in passport
    has_hgt = 'hgt' in passport
    has_hcl = 'hcl' in passport
    has_ecl = 'ecl' in passport
    has_pid = 'pid' in passport
    has_cid = 'cid' in passport

    if has_byr and has_iyr and has_eyr and has_hgt and has_hcl and has_ecl and has_pid:
        if f == 1:
            return True
        elif f == 2:
            byr_valid = is_byr_valid(passport)
            logging.debug(f'byr valid - {byr_valid}')
            iyr_valid = is_iyr_valid(passport)
            logging.debug(f'iyr valid - {iyr_valid}')
            eyr_valid = is_eyr_valid(passport)
            logging.debug(f'eyr valid - {eyr_valid}')
            hgt_valid = is_hgt_valid(passport)
            logging.debug(f'hgt valid - {hgt_valid}')
            hcl_valid = is_hcl_valid(passport)
            logging.debug(f'hcl valid - {hcl_valid}')
            ecl_valid = is_ecl_valid(passport)
            logging.debug(f'ecl valid - {ecl_valid}')
            pid_valid = is_pid_valid(passport)
            logging.debug(f'pid valid - {pid_valid}')
            if byr_valid and iyr_valid and eyr_valid and hgt_valid and hcl_valid and ecl_valid and pid_valid:
                logging.debug('Passport valid')
                return True
            else:
                logging.debug('Passport invalid')
                return False
    else:
        return False


def is_byr_valid(passport):
    try:
        byr = int(re.search('(byr):(\d{4})', passport).group(2))
    except:
        byr = None
    logging.debug(f'byr - {byr}')
    if byr == None:
        return False
    elif byr >= 1920 and byr <= 2002:
        return True
    else:
        return False


def is_iyr_valid(passport):
    try:
        iyr = int(re.search('(iyr):(\d{4})', passport).group(2))
    except:
        iyr = None
    logging.debug(f'iyr - {iyr}')
    if iyr == None:
        return False
    elif iyr >= 2010 and iyr <= 2020:
        return True
    else:
        return False


def is_eyr_valid(passport):
    try:
        eyr = int(re.search('(eyr):(\d{4})', passport).group(2))
    except:
        eyr = None
    logging.debug(f'eyr - {eyr}')
    if eyr == None:
        return False
    elif eyr >= 2020 and eyr <= 2030:
        return True
    else:
        return False


def is_hgt_valid(passport):
    try:
        hgt = re.search('(hgt):(\d{3}|\d{2})(cm|in)?', passport).groups()[1:]
    except:
        hgt = None
    logging.debug(f'hgt - {hgt}')
    if hgt == None:
        return False
    elif int(hgt[0]) >= 150 and int(hgt[0]) <= 193 and hgt[1] == 'cm':
        return True
    elif int(hgt[0]) >= 59 and int(hgt[0]) <= 76 and hgt[1] == 'in':
        return True
    else:
        return False


def is_hcl_valid(passport):
    try:
        hcl = re.search('(hcl):(#[0-9a-f]{6})', passport).group(2)
    except:
        hcl = None
    logging.debug(f'hcl - {hcl}')
    if hcl:
        return True
    else:
        return False


def is_ecl_valid(passport):
    try:
        ecl = re.search('(ecl):(amb|blu|brn|gry|grn|hzl|oth)', passport).group(2)
    except:
        ecl = None
    logging.debug(f'ecl - {ecl}')
    if ecl:
        return True
    else:
        return False

def is_pid_valid(passport):
    try:
        pid = re.search('(pid):(\d{9})', passport).group(2)
    except:
        pid = None
    logging.debug(f'pid - {pid}')
    if pid:
        return True
    else:
        return False

valid_passports = 0

for passport in passport_data:
    if validate_passport(passport, f=2):
        valid_passports += 1
print(valid_passports)