import re


def checkMatchWithDictionary(chosen_pass):
    file = open("words.txt", "r")

    for line in file:
        word = line.strip('\n')
        if word.isdigit() or word.isalpha():
            continue

        if word.lower() in chosen_pass.lower():
            file.close()
            return True,word
    return False, None


def checkCommonPass(chosen_pass):
    file = open('passlist.txt', 'r')
    for line in file:
        word = line.strip('\n')
        if chosen_pass == word:
            file.close()
            return True
    return False


def checkBasicRequirements(chosen_pass):
    requirements = [
        r"(?=.*[A-Z])",  # At least one uppercase letter
        r"(?=.*[a-z])",  # At least one lowercase letter
        r"(?=.*\d)",  # At least one digit
        r"(?=.*[@#$%^&*()!])",  # At least one special character
        r"[A-Za-z\d@#$%^&*()!]{8,}",  # No whitespace or spaces
    ]

    failed_requirements = []
    outputs = ['At least one uppercase letter required', 'At least one lowercase letter required',
               'At least one digit required', 'At least one special character required', 'No whitespaces or spaces']
    for i in range(len(requirements)):
        passRegex = re.compile(requirements[i])
        if not passRegex.search(chosen_pass):
            failed_requirements.append(outputs[i])
    return failed_requirements


def passwordStrength(chosen_pass):
    # check minimum length
    if len(chosen_pass) < 8:
        print("Password too short to be secure")
        return False

    # check for maximum length?

    simplePass = checkMatchWithDictionary(chosen_pass)
    if simplePass[0] is True:
        print(f'Password has {simplePass[1]} available in a dictionary')
        return False

    commonPass = checkCommonPass(chosen_pass)
    if commonPass is True:
        print(f'{chosen_pass} as Password is very commonly used')
        return False

    # check basic requirements
    failed_requirements = checkBasicRequirements(chosen_pass)
    if len(failed_requirements) != 0:
        for text in failed_requirements:
            print(text)
        return False

    print("Password is strong")
    return True


# passwordStrength('hello123')
