
def addzero(phone_num: str):  # add zero in the beginning of phone number if its missing
    if phone_num[0] != "0":
        phone_num = "0"+phone_num
    return phone_num


def digitsonly(bad_phone: str):  # only returns digits with no spaces.
    bad_phone = addzero(bad_phone)
    good_phone = ''
    for digit in bad_phone:
        check = digit.isdigit()
        if check == True:
            good_phone = good_phone+digit
    return good_phone


def ishomephone(tel_num: str):  # check if its a home phone number
    tel_num = digitsonly(tel_num)
    cellphone_codes = ("05", "06")
    if len(tel_num) == 10 and tel_num[:2] in cellphone_codes:
        return True
    else:
        return False


# changes the area code for old hot mobile phones that changed from 053 to 057
def mirsishot(mirs_num: str):
    hot_num = digitsonly(mirs_num)
    if (hot_num[:3] in "057"):
        if (len(hot_num) == 10):
            hot_num = "053" + hot_num[3:]
            return hot_num
    else:
        return mirs_num


# adds seventh digit to old phones before the change to 7 digits
def seventhdigit(old_phone_num: str):
    old_phone_num = digitsonly(old_phone_num)
    # this means its either a new cellphone number or a home phone
    if len(old_phone_num) == 10 or ishomephone(old_phone_num) == True:
        return old_phone_num
    elif len(old_phone_num) == 9 and ishomephone(old_phone_num) == False:
        old_area_code = old_phone_num[1:3]
        newdigit = old_phone_num[2]
        old_phone_num_end = old_phone_num[3:]
        cellcom_area_codes = ("52", "53", "58", "64" "65")
        partner_area_codes = ("54", "55", "66", "67")
        pelephone_area_codes = ("50", "51", "56", "68")
        mirs_area_code = "57"
        javal_area_code = "59"
        if old_area_code in cellcom_area_codes:
            new_phone_num = "052" + newdigit + old_phone_num_end
        elif old_area_code in partner_area_codes:
            new_phone_num = "054" + newdigit + old_phone_num_end
        elif old_area_code in pelephone_area_codes:
            new_phone_num = "050" + newdigit + old_phone_num_end
        elif old_area_code in mirs_area_codes:  # mirs turned to hot in 2015
            new_phone_num = "053" + newdigit + old_phone_num_end
        elif old_area_code in javal_area_codes:
            new_phone_num = "059" + newdigit + old_phone_num_end
        else:
            raise ValueError("Not a valid phone number")
    return new_phone_num


# use the other functions to create a normal cellphone number with one dash in the right place, if its not a phone number it is exterminated (erased)
def normalizephone(freaky_num: str):
    normal_phone = addzero(freaky_num)
    normal_phone = digitsonly(normal_phone)
    normal_phone = mirsishot(normal_phone)
    try:
        if len(normal_phone) < 9:
            raise ValueError("Number too short")
    except:
        return ""
    else:
        try:
            normal_phone = seventhdigit(normal_phone)
        except:
            return ""
        else:
            if len(normal_phone) == 10:
                excel_type_phone = normal_phone[:3] + "-" + normal_phone[3:]
            elif len(normal_phone) == 9:
                excel_type_phone = normal_phone[:2] + "-" + normal_phone[2:]
            return excel_type_phone


bphone1 = "-54-3223  411 "
oldphone3 = "068-234567"
notaphone = "334"
myphone = "0-54-974-7361- "
nozerophone = "529737362"
homenumber = "04-6392298"
newweirdhomenumber = "077-907-2799"
extremnumber = "5-33-3 847 1    0-"
okayphonenumber = "054-9747361"
oldhotmobile = "0-5-7-8-7-3-2-273"

print(normalizephone(bphone1))
print(normalizephone(oldphone3))
print(normalizephone(notaphone))
print(normalizephone(myphone))
print(normalizephone(nozerophone))
print(normalizephone(homenumber))
print(normalizephone(newweirdhomenumber))
print(normalizephone(extremnumber))
print(normalizephone(okayphonenumber))
print(normalizephone(oldhotmobile))
