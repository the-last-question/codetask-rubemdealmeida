import re
def checkPassword(password):
    check= re.compile('[a-z]+[A-Z]+[0-9]+').match(password)
    return check



print(checkPassword('testeA'))