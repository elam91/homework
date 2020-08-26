
def digitsonly(badphone: str):  # only returns digits with no spaces.
    goodphone = ''
    checkdigits = "0123456789"
    for digit in badphone:
        check = digit in checkdigits
        if check == True:
            goodphone = goodphone+digit
    return goodphone


# adds seventh digit to old phones before the change to 7 digits
def seventhdigit(oldphonenum: str):
    if oldphonenum[0] != "0":
        oldphonenum = "0"+oldphonenum
    oldphonenum = digitsonly(oldphonenum)
    if len(oldphonenum) == 10:
        newphonenum = oldphonenum  # this means this is a new number
    elif len(oldphonenum) < 9:
        newphonenum = "Error: Phone number too short"
    elif len(oldphonenum) == 9:
        if oldphonenum[1:3] == "52" or oldphonenum[1:3] == "53" or oldphonenum[1:3] == "58" or oldphonenum[1:3] == "64" or oldphonenum[1:3] == "65":
            newphonenum = "052" + oldphonenum[2] + oldphonenum[3:]
        elif oldphonenum[1:3] == "54" or oldphonenum[1:3] == "55" or oldphonenum[1:3] == "66" or oldphonenum[1:3] == "67":
            newphonenum = "054" + oldphonenum[2] + oldphonenum[3:]
        elif oldphonenum[1:3] == "50" or oldphonenum[1:3] == "51" or oldphonenum[1:3] == "56" or oldphonenum[1:3] == "68":
            newphonenum = "050" + oldphonenum[2] + oldphonenum[3:]
        elif oldphonenum[1:3] == "57":
            newphonenum = "057" + oldphonenum[2] + oldphonenum[3:]
        elif oldphonenum[1:3] == "59":
            newphonenum = "059" + oldphonenum[2] + oldphonenum[3:]
        else:
            newphonenum = "Error: Invalid number"
    return newphonenum


# use the other functions to create a normal cellphone number with one dash in the right place
def normalizephone(freakynum: str):
    normalphone = seventhdigit(freakynum)
    errorchecker = "Error" in normalphone
    if errorchecker == False:
        exceltypephone = normalphone[:3] + "-" + normalphone[3:]
        return exceltypephone
    else:
        return normalphone


bphone1 = "054-3223  411 "
oldphone3 = "066-234567"
notaphone = "334"
myphone = "0-54-974-7361- "
nozerophone = "549737362"
homenumber = "04-6392298"

print(normalizephone(bphone1))
print(normalizephone(oldphone3))
print(normalizephone(notaphone))
print(normalizephone(myphone))
print(normalizephone(nozerophone))
print(normalizephone(homenumber))
