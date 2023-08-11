import random, string
import passwordStrength


def generatePassword(length=14):
    characters = string.digits + string.ascii_letters + r'?$#@%&!/'
    while True:
        password = ""
        for i in range(length):
            password += random.choice(characters)

        if passwordStrength.passwordStrength(password) is True:
            print(password)
            break
        else:

            continue


generatePassword(15)
