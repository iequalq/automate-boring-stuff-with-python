# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

#Regular Expressions prefunctions
    message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
    message1='Batmobile lost a wheel'
    nameString='First Name : alis  Last Name : brithon'
    dotAllString='First Name : alis \n Last Name : brithon'
    subString='Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'

    phoneNumberFinder(message)
    allPhoneNumberFinder(message)
    batFinder(message1)
    RegularExpressions.nameFinder(nameString)
    RegularExpressions.dotAllMatch(dotAllString)
    RegularExpressions.nameSub(subString)
