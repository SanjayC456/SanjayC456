# create the backend application in python - flask
#step-1 -  import the package
from flask import Flask
import Validation
import constant
import pyrebase

#step-2 - create the backend application
app=Flask(__name__)
#create first feature of an application
#create dummy api
@app.route("//hello")
def hello():
    return ("My name is Sanjay")

@app.route("//add/<a>/<b>")
def add(a,b):
    try:
        c = int(a) + int(b)
        return str(c)
    except:
        return("ERROR")

#create the signup api to insert the data in the data base
@app.route(constant.CREATEACCOUNTAPI)
def createaccount(userid,password,name,contact):
    # step1- perform the validation operation
    useridvalidity=Validation.checkvaliduserid(userid)
    namevalidity=Validation.checkname(name)
    contactvalidity=Validation.checkcontactno(contact)
    passwordvalidity=Validation.checkpassword(password)
    if useridvalidity==True and namevalidity==True and contactvalidity==True and passwordvalidity==True:
       try:
           # store the data in the database
           # step1- connect to database
           # step2- authonticate and insert the data in database
           firebaseConfig=constant.FIREBASECONNECTION
           # start the server
           firebase = pyrebase.initialize_app(firebaseConfig)
           # create account
           auth = firebase.auth()
           auth.create_user_with_email_and_password(userid, password)
           return constant.APISUCCESS
       except:
           return constant.APIFAILED


    return constant.POLICYVOILATED
#######################################################################################################################
@app.route("/login/<userid>/<password>")
def login(userid,password):
    useridstatus=Validation.checkvaliduserid(userid)
    passwordstatus=Validation.checkpassword(password)
    try:
        if useridstatus == True and passwordstatus == True:
            # connect with data base to check userid and password is valid
            firebaseConfig = constant.FIREBASECONNECTION
            firebase = pyrebase.initialize_app(firebaseConfig)
            # login to application
            auth = firebase.auth()
            auth.sign_in_with_email_and_password(userid, password)
            return constant.APISUCCESS
    except:
        return constant.APIFAILED
    return constant.POLICYVOILATED

########################################################################################################################
@app.route("/personalinfo/<name>/<age>/<gender>/<martialstatus>/<contact>/<userid>")
def personaldetails(name,age,gender,martialstatus,contact,userid):
    namevalidation=Validation.checkname(name)
    agevalidation=Validation.checkage(age)
    gendervalidation=Validation.checkgender(gender)
    martialvalidation=Validation.checkmaratialstatus(martialstatus)
    try:
        if namevalidation == True and agevalidation==True and gendervalidation==True and martialvalidation==True:
            #push the data in database server and then return successfull message
            #step1- connect to server
            from firebase import firebase
            firebase=firebase.FirebaseApplication("https://firstapplication-84e79-default-rtdb.firebaseio.com/")
            #prepare the data to be inserted
            data={
                'name':name,
                'age':age,
                'gender':gender,
                'martialstatus':martialstatus,
                'contact':contact,
                'userid':userid,
            }
            #commit the data in a database
            firebase.post('personaldata',data)
            return constant.SUCCESSFULL
        else:
            return constant.UNSUCCESSFULL

    except:

        return constant.FAILED

######################################################################################################################
#create an API to fetch the data fro the database

@app.route("/fetchpd/<userid>")
def fetchpd(userid):
    useridstatus=Validation.checkvaliduserid(userid)
    if useridstatus==True:
        #check that userid is there in data base or not
        #step1- connect to data base
        firebaseConfig = constant.FIREBASECONNECTION
        firebase = pyrebase.initialize_app(firebaseConfig)
        #create data base object
        database=firebase.database()
        #step3- fetch the data from data base
        data=database.child("personaldata").get()
        dict={}
        for eachdata in data:
            #fetch userid from each data
            uid=eachdata.val()['userid']
            if uid==userid:
                dict["age"]=eachdata.val()["age"]
                dict["contact"] = eachdata.val()["contact"]
                dict["gender"] = eachdata.val()["gender"]
                dict["martialstatus"] = eachdata.val()["martialstatus"]
                dict["name"] = eachdata.val()["name"]
                dict["userid"] = eachdata.val()["userid"]
                return dict

    else:
        return "Invalid UserID"

#######################################################################################################################

@app.route("/updatepersonaldetails/<userid>/<name>/<age>/<contact>/<martialstatus>")
def updatepersonaldetails(userid,name,age,contact,martialstatus):
    namevalidation = Validation.checkname(name)
    agevalidation = Validation.checkage(age)
    contactvalidation = Validation.checkcontactno(contact)
    martialvalidation = Validation.checkmaratialstatus(martialstatus)
    if namevalidation==True and agevalidation==True and contactvalidation==True and martialvalidation==True:
        #step1 connect to data base
        firebaseConfig = constant.FIREBASECONNECTION
        firebase = pyrebase.initialize_app(firebaseConfig)
        #step2 create the database object
        database = firebase.database()
        #step3 fetch all the data from data base
        data = database.child("personaldata").get()
        for eachdata in data:
            databaseuserid=eachdata.val()['userid']
            if databaseuserid==userid:
                #update the data of the userid
                database.child("personaldata").child(eachdata.key()).update({"name":name})
                database.child("personaldata").child(eachdata.key()).update({"age": age})
                database.child("personaldata").child(eachdata.key()).update({"contact": contact})
                database.child("personaldata").child(eachdata.key()).update({"martialstatus": martialstatus})
                return constant.APISUCCESS

    return constant.FAILED

#########################################################################################################################

@app.route("/securityquestions/<question1>/<question2>/<question3>/<answer1>/<answer2>/<answer3>/<userid>")
def securityquestions(question1,question2,question3,answer1,answer2,answer3,userid):
    useridvalidity=Validation.checkvaliduserid(userid)
    if useridvalidity==True:
        from firebase import firebase
        firebase = firebase.FirebaseApplication("https://firstapplication-84e79-default-rtdb.firebaseio.com/")
        security_data = {
            "question1":question1,
            "question2":question2,
            "question3":question3,
            "answer1":answer1,
            "answer2":answer2,
            "answer3":answer3,
            "userid":userid,
        }
        firebase.post('securityquestions', security_data)
        return constant.SUCCESSFULL
    else:
        return constant.FAILED

@app.route("/validatesecurity/<userid>/<squestion>/<sanswer>")
def validatesecurity(userid,squestion,sanswer):
    firebaseConfig = constant.FIREBASECONNECTION
    firebase = pyrebase.initialize_app(firebaseConfig)
    database = firebase.database()
    data = database.child("securityquestions").get()
    Q=[]
    A=[]
    for eachdata in data:
        # fetch userid from each data
        uid = eachdata.val()['userid']
        if uid == userid:
            q1=eachdata.val()['question1']
            q2=eachdata.val()['question2']
            q3=eachdata.val()['question3']
            a1=eachdata.val()['answer1']
            a2=eachdata.val()['answer2']
            a3=eachdata.val()['answer3']
            Q.append(q1)
            Q.append(q2)
            Q.append(q3)
            A.append(a1)
            A.append(a2)
            A.append(a3)
            print(Q)
            print(A)
    for i in range(len(Q)):
        if Q[i]==squestion and A[i]==sanswer:
            return constant.SUCCESSFULL
    return constant.FAILED



#step-3 - run the application
if __name__=="__main__":
    app.run(debug=True)






