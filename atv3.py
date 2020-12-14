def perfectN(n):
    array = []
    resp=0
    for x in range(n):
        if(x!=0):
            if(n/x == n//x):
                array.append(x)
    for y in array:
        resp=resp+y
    if(resp==n):
        return True
    else:
        return False


def getPerfectN():
    array = []
    for x in range(1, 10000):
        if(perfectN(x)):
            array.append(x)

    print(array)
getPerfectN()