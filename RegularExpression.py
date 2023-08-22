import re

def phoneNumberFinder(in_string):
    phoneNumberRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
    phoneNumbers = phoneNumberRegex.search(in_string)
    print('Phone number state code found: '+phoneNumbers.group(1))
    print('Phone number city code found: ' + phoneNumbers.group(2))
def allPhoneNumberFinder(in_string):
    phoneNumberRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
    phoneNumbers = phoneNumberRegex.findall(in_string)
    [print(f'Phone number {num}') for num in phoneNumbers]

def batFinder(in_string):
    batRegex=re.compile(r'Bat(man|mobile|copter)')
    bat_string=batRegex.search(in_string)
    print(bat_string.group(1))
    print(bat_string.group())

def nameFinder(in_string):
    firstNameRegex=re.compile(r'First Name : (.*) Last Name : (.*)')
    name=firstNameRegex.search(in_string)
    print('First Name is ' + name.group(1))
    print('Last Name is ' + name.group(2))

def dotAllMatch(in_string):
    dotAllRegex=re.compile(r'.*',re.DOTALL)
    dotAllmatches=dotAllRegex.search(in_string)
    print(dotAllmatches.group())
def ignoreCaseMatch(in_string):
    ignoreCaseRegex=re.compile(r'IGnoreCase', re.IGNORECASE)
    ignoreCaseMatches=ignoreCaseRegex.search(in_string)
    print(ignoreCaseMatches.group())

def nameSub(in_string):
    nameRegex=re.compile(r'Agent (\w)\w*')
    nameMatches=nameRegex.sub(r'\1****',in_string)
    print(nameMatches)

def verbosedRegex(in_string):

    phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # area code
    (\s|-|\.)? # separator
    \d{3} # first 3 digits
    (\s|-|\.) # separator
    \d{4} # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})? # extension
    )''', re.VERBOSE)

    someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)



