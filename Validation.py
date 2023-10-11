def checkvaliduserid(userid):
    uppercase = 0
    lowercase = 0
    digit = 0
    length = 0
    for i in userid:
        if (i.isupper()):
            uppercase = 1
        if (i.islower()):
            lowercase = 1
        if (i.isdigit()):
            digit = 1
        if len(userid) > 6:
            length = 1
    # check for the special character
    special = 0
    special_list = ["@", "$", "%", "*","."]
    for i in userid:
        for j in special_list:
            if i == j:
                special = 1
    if (uppercase==1 and lowercase==1 and digit==1 and length==1 and special==1):
        return True
    return False


def checkname(name):
    if name.isalpha():
        return True
    return False

def checkcontactno(contact):
    if len(contact)==10 and contact.isdigit():
        return True
    return False

#validation on password
''' password 1st letter must me upper case
password len must be between 6 to 10 
it must contain digit
last letter of the must be lower case'''

def checkpassword(password):
    uppercase = 0
    lowercase = 0
    digit = 0
    length = 0
    if (password[0].isupper()):
        uppercase=1
    if (password[-1].islower()):
        lowercase=1
    if len(password)>=6 and len(password)<=10:
        length=1
    for i in password:

        if (i.isdigit()):
            digit = 1

    if (uppercase == 1 and lowercase == 1 and digit == 1 and length == 1):
        return True
    return False

def checkage(age):
 if (int(age) >=18 and int(age)<=85):
     return True
 return False

def checkgender(gender):
    genderflag=0
    gender_list = ["Male","Female","Others"]
    for i in gender_list:
        if (i==gender):
                genderflag=1
    if (genderflag==1):
        return True
    return False

def checkmaratialstatus(maratial):
    maratialflag=0
    maratialist = ["Married","Single","Divorced"]
    for i in maratialist:
        if (i==maratial):
            maratialflag=1

    if (maratialflag==1):
        return True
    return False














