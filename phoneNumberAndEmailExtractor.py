import re,pyperclip


def phoneNumberFinder(in_string):
    phoneRegex=re.compile(r'''(
    (\d{3}|\((\d{3})\))?               #area code
    (\s|-|\.)?                 #seperator
    (\d{3})               # first 3 digits
    (\s|-|\.)                 # separator
    (\d{4})               # last 4 digits
    )''',re.VERBOSE)
    phonNumbers=phoneRegex.findall(in_string)
    return phonNumbers

def emailAddrFinder(in_string):
    emailRegex=re.compile(r'''(
    [a-zA-Z0-9-.+%_]+   #user name
    @
    [a-zA-Z0-9.-]+      #domain name
    (\.[a-zA-Z]{2,4})   #dot-something
    )''',re.VERBOSE)
    emailAddres=emailRegex.findall(in_string)
    return emailAddres

#def phoneAndEmailFinder(in_string):
def phoneAndEmailFinder():
    in_string=str(pyperclip.paste())
    phoneNumbers=phoneNumberFinder(in_string)
    emilAddres=emailAddrFinder(in_string)
    matches=[]
    for num in phoneNumbers:
        if num[2] == '':
            matches.append("-".join([num[1],num[4],num[6]]))
        else:
            matches.append('-'.join([num[2],num[4],num[6]]))

    for email in emilAddres:
        matches.append(email[0])
    if len(matches) > 0 :
        print("coopied to clipboard")
        print("\n".join(matches))
    else:
        print("There is no matches")

    return matches