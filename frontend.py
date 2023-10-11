#frontend application can be developed in 3 steps
#step1- import the package
from tkinter import *
import requests
import constant
from tkinter import messagebox
import urllib.request
import ast
import frontendconstant
import random

def validatesecurity():
    sanswer=abcd_entry.get()
    url="http://127.0.0.1:5000/validatesecurity/"+userid+"/"+question+"/"+sanswer
    print(url)
    response = requests.get(url)
    data = response.text
    print(data)
    if(data==constant.SUCCESSFULL):
        messagebox.showinfo('Validation successfull',constant.SUCCESSFULL)
        confirm_account['state']=NORMAL
        execute_default_api()
    elif (data==constant.FAILED):
        messagebox.showwarning('Please try again later', constant.FAILED)
    else:
        messagebox.showerror('Error', 'this error is unknown to user')


def submitsecurityquestion():
    question1=frontendconstant.SECURITYQUESTIONS[0]
    question2=frontendconstant.SECURITYQUESTIONS[1]
    question3=frontendconstant.SECURITYQUESTIONS[2]
    answer1=answer1_entry.get()
    answer2=answer2_entry.get()
    answer3=answer3_entry.get()
    userid=userid_security.get()
    url="http://127.0.0.1:5000/securityquestions/"+question1+"/"+question2+"/"+question3+"/"+answer1+"/"+answer2+"/"+answer3+"/"+userid
    print(url)
    response=requests.get(url)
    data=response.text
    print(data)
    if (data==constant.SUCCESSFULL):
        messagebox.showinfo('Validation successfull', constant.SUCCESSFULL)
        securitycomponent.place_forget()
        lcomponent.place(x=80, y=60, height=400, width=1000)
    elif (data==constant.FAILED):
        messagebox.showwarning('Please try again later', constant.FAILED)
    else:
        messagebox.showerror('Error', 'this error is unknown to user')

def updatedetails():
    updatename=namerd_entry.get()
    updatecontact=contactrd_entry.get()
    updateage=agerd_entry.get()
    updatemartial=martialrd_entry.get()
    url="http://127.0.0.1:5000/updatepersonaldetails/"+userid+"/"+updatename+"/"+updateage+"/"+updatecontact+"/"+updatemartial
    print(url)
    response=requests.get(url)
    data=response.text
    print(data)
    if (data == constant.APISUCCESS):
        messagebox.showinfo('Validation successfull', constant.APISUCCESS)
        updatecomponent.place_forget()
        execute_default_api()
    elif (data == constant.APIFAILED):
        messagebox.showwarning('Please try again later', constant.APIFAILED)
    else:
        messagebox.showerror('Error', 'this error is unknown to user')

def openupdatecontainer():
    updatebutton.place(x=200, y=420, height=frontendconstant.BUTTON_HEIGHT, width=frontendconstant.BUTTON_WIDTH)

def execute_default_api():
    url="http://127.0.0.1:5000/fetchpd/"+userid
    response=urllib.request.urlopen(url)
    response=response.read()
    data=response.decode("UTF:8")
    mydata=ast.literal_eval(data)
    name_ld.configure(text="NAME:" + mydata["name"])
    contact_ld.configure(text="CONTACT:" + mydata["contact"])
    age_ld.configure(text="AGE:" + mydata["age"])
    gender_ld.configure(text="GENDER:" + mydata["gender"])
    martial_ld.configure(text="MARTIAL STATUS:" + mydata["martialstatus"])
    #dissable pd button and enable the update button
    pdbutton['state']=DISABLED
    updatebutton['state']=NORMAL
    #insert the details in entry field which is inside the update container
    namerd_entry.insert(0,mydata["name"])
    #contactrd_entry.insert(0,"+91")
    contactrd_entry.insert(0,mydata["contact"])
    agerd_entry.insert(0,mydata["age"])
    martialrd_entry.insert(0,mydata["martialstatus"])

    '''
    response=requests.get(url)
    response=response.text
    a = response.split(",")
    result = []
    for i in range(0, 5):
        data = a[i]
        data = data.split(":")[1]
        result.append(data)

    data = a[5].split(":")[1][0:-3]
    result.append(data)
    print(result)
    #set the each data in lable
    name_ld.configure(text="NAME:"+result[4])
    contact_ld.configure(text="CONTACT:"+result[1])
    age_ld.configure(text="AGE:"+result[0])
    gender_ld.configure(text="GENDER:"+result[2])
    martial_ld.configure(text="MARTIAL STATUS:"+result[3])
    
    '''

def fillpd():
    name=name_entry.get()
    contact=contact_entry.get()
    age=age_entry.get()
    g=gender.get()
    ms=martial.get()
    # prepare the url to call the api
    url="http://127.0.0.1:5000/personalinfo/"+name+"/"+age+"/"+g+"/"+ms+"/"+contact+"/"+userid
    print(url)
    #call the api
    response=requests.get(url)
    data=response.text
    print(data)
    if(data==constant.SUCCESSFULL):
        messagebox.showinfo('Validation successfull',constant.SUCCESSFULL)
        pdcomponent.place_forget()
        dcomponent.place(x=50, y=60, height=700, width=1400)
        execute_default_api()
    elif(data==constant.UNSUCCESSFULL):
        messagebox.showwarning('Enter valid detail',constant.UNSUCCESSFULL)
    elif(data==constant.FAILED):
        messagebox.showwarning('Please try again later',constant.FAILED)
    else:
        messagebox.showerror('Error', 'this error is unknown to user')

def openupdate():
    updatecomponent.place(x=10, y=20, height=500, width=600)

def openpd():
    pdcomponent.place(x=10, y=20, height=550, width=700)

def gotoscomponent():
    lcomponent.place_forget()
    scomponent.place(x=80, y=60, height=400, width=1000)

def createaccount():
    #fetch the data from interface
    userid=signup_userid_entry.get()
    password=signup_password_entry.get()
    name=signup_name_entry.get()
    contact=signup_contact_entry.get()
    # create the URL to call the API
    url="http://127.0.0.1:5000/createaccount/"+userid+"/"+password+"/"+name+"/"+contact
    #call the API
    response=requests.get(url)
    data=response.text
    print(data)
    #give notification to the user
    if (data==constant.APIFAILED):
        messagebox.showwarning('Warning',constant.APIFAILED)
    elif(data==constant.POLICYVOILATED):
        messagebox.showerror('Error',constant.POLICYVOILATED)
    elif(data==constant.APISUCCESS):
        messagebox.showinfo('Info',constant.APISUCCESS)
        #move the container to login container
        scomponent.place_forget()
        userid_security.insert(0, userid)
        securitycomponent.place(x=80, y=60, height=700, width=1200)
    else:
        messagebox.showerror('Error','this error is unknown to user')

def login():
    #make the userid global
    global userid
    userid=userid_entry.get()
    password=password_entry.get()
    url="http://127.0.0.1:5000/login/"+userid+"/"+password
    response=requests.get(url)
    data=response.text
    print(data)
    if(data==constant.APIFAILED):
        messagebox.showwarning('Warning',constant.APIFAILED)
    elif(data==constant.POLICYVOILATED):
        messagebox.showerror('Error',constant.POLICYVOILATED)
    elif(data==constant.APISUCCESS):
        messagebox.showinfo('Info',constant.APISUCCESS)
        lcomponent.place_forget()
        dcomponent.place(x=50, y=60, height=700, width=1400)
        #call all the necessary api of our application
        execute_default_api()

    else:
        messagebox.showerror('Error','this error is unknown to user')

########################################################################################################################

# * is called meta character which means 0 to all
#ster2- create application
fapp=Tk()
#configure the window
fapp.geometry('800x900')
fapp.state('zoomed')
fapp.configure(background='white')
#create signup component
scomponent=Frame(fapp,bg=frontendconstant.APPLICATION_COLOUR)
scomponent.place(x=80,y=60,height=400,width=1000)

signup_userid=Label(scomponent, text="ENTER USER-ID", font=(frontendconstant.FONTFAMILY, frontendconstant.FONTSIZE),bg=frontendconstant.APPLICATION_COLOUR,fg=frontendconstant.FOURGROUND_COLOUR)
signup_userid.place(x=100,y=60)
signup_userid_entry=Entry(scomponent)
signup_userid_entry.place(x=400,y=60,height=frontendconstant.ENTRY_HEIGHT, width=frontendconstant.ENTRY_WIDTH)

signup_password=Label(scomponent, text="ENTER PASSWORD", font=(frontendconstant.FONTFAMILY, frontendconstant.FONTSIZE),bg=frontendconstant.APPLICATION_COLOUR,fg=frontendconstant.FOURGROUND_COLOUR)
signup_password.place(x=100,y=100)
signup_password_entry=Entry(scomponent)
signup_password_entry.place(x=400,y=100,height=frontendconstant.ENTRY_HEIGHT, width=frontendconstant.ENTRY_WIDTH)

signup_name=Label(scomponent, text="ENTER NAME", font=(frontendconstant.FONTFAMILY, frontendconstant.FONTSIZE),bg=frontendconstant.APPLICATION_COLOUR,fg=frontendconstant.FOURGROUND_COLOUR)
signup_name.place(x=100,y=140)
signup_name_entry=Entry(scomponent)
signup_name_entry.place(x=400,y=140,height=frontendconstant.ENTRY_HEIGHT, width=frontendconstant.ENTRY_WIDTH)

signup_contact=Label(scomponent, text="ENTER CONTACT NO", font=(frontendconstant.FONTFAMILY, frontendconstant.FONTSIZE),bg=frontendconstant.APPLICATION_COLOUR,fg=frontendconstant.FOURGROUND_COLOUR)
signup_contact.place(x=100,y=180)
signup_contact_entry=Entry(scomponent)
signup_contact_entry.place(x=400,y=180,height=frontendconstant.ENTRY_HEIGHT, width=frontendconstant.ENTRY_WIDTH)

scomponent.place_forget()
#create login component
lcomponent=Frame(fapp,bg=frontendconstant.APPLICATION_COLOUR)
lcomponent.place(x=80,y=60,height=400,width=1000)
l_heading=Label(lcomponent,text="Login",font=(frontendconstant.FONTFAMILY, frontendconstant.FONTSIZE),bg=frontendconstant.APPLICATION_COLOUR,fg=frontendconstant.FOURGROUND_COLOUR)
l_heading.place(x=100,y=20,height=frontendconstant.ENTRY_HEIGHT, width=frontendconstant.ENTRY_WIDTH)

userid_lable=Label(lcomponent,text="ENTER USERID",font=(frontendconstant.FONTFAMILY, frontendconstant.FONTSIZE),bg=frontendconstant.APPLICATION_COLOUR,fg=frontendconstant.FOURGROUND_COLOUR)
userid_lable.place(x=100,y=60)
userid_entry=Entry(lcomponent)
userid_entry.place(x=350,y=60,height=frontendconstant.ENTRY_HEIGHT, width=frontendconstant.ENTRY_WIDTH)

password_lable=Label(lcomponent, text ="ENTER PASSWORD",font=(frontendconstant.FONTFAMILY, frontendconstant.FONTSIZE),bg=frontendconstant.APPLICATION_COLOUR,fg=frontendconstant.FOURGROUND_COLOUR)
password_lable.place(x=100,y=100)
password_entry=Entry(lcomponent,show="*")
password_entry.place(x=350,y=100,height=frontendconstant.ENTRY_HEIGHT, width=frontendconstant.ENTRY_WIDTH)

dcomponent=Frame(fapp,bg=frontendconstant.APPLICATION_COLOUR)
dcomponent.place(x=50,y=60,height=700,width=1400)
dcomponent.place_forget()

ldcomponent=Frame(dcomponent,bg=frontendconstant.APPLICATION_COLOUR)
ldcomponent.place(x=10,y=20,height=500,width=500)
personaldetails=Label(ldcomponent, text="PERSONAL INFO", font=(frontendconstant.FONTFAMILY, frontendconstant.FONTSIZE),bg=frontendconstant.APPLICATION_COLOUR,fg=frontendconstant.FOURGROUND_COLOUR)
personaldetails.place(x=50,y=20,height=frontendconstant.ENTRY_HEIGHT, width=frontendconstant.ENTRY_WIDTH)

pdbutton=Button(ldcomponent,text="Complete PD",command=openpd)
pdbutton.place(x=200,y=380,height=frontendconstant.BUTTON_HEIGHT, width=frontendconstant.BUTTON_WIDTH)

updatebutton=Button(ldcomponent,text="Update PD",command=openupdate)
updatebutton.place(x=200,y=420,height=frontendconstant.BUTTON_HEIGHT, width=frontendconstant.BUTTON_WIDTH)

updatebutton['state']=DISABLED

####################################################################################

rdcomponent=Frame(dcomponent,bg=frontendconstant.APPLICATION_COLOUR)
rdcomponent.place(x=600,y=20,height=650,width=700)

######################################################################################

pdcomponent=Frame(rdcomponent,bg=frontendconstant.APPLICATION_COLOUR)
pdcomponent.place(x=10,y=20,height=550,width=700)
pdcomponent.place_forget()
personal_heading=Label(pdcomponent, text="Personal Details", font=(frontendconstant.FONTFAMILY, frontendconstant.FONTSIZE),bg=frontendconstant.APPLICATION_COLOUR,fg=frontendconstant.FOURGROUND_COLOUR)
personal_heading.place(x=100,y=20)

#create the userid field
#concept of accessing the variable in an out of function is called variable global access

name_lable=Label(pdcomponent,text="Name",font=(frontendconstant.FONTFAMILY, frontendconstant.FONTSIZE),bg=frontendconstant.APPLICATION_COLOUR,fg=frontendconstant.FOURGROUND_COLOUR)
name_lable.place(x=100,y=60)
name_entry=Entry(pdcomponent)
name_entry.place(x=250,y=60,height=frontendconstant.ENTRY_HEIGHT, width=frontendconstant.ENTRY_WIDTH)

contact_lable=Label(pdcomponent,text="Contact",font=(frontendconstant.FONTFAMILY, frontendconstant.FONTSIZE),bg=frontendconstant.APPLICATION_COLOUR,fg=frontendconstant.FOURGROUND_COLOUR)
contact_lable.place(x=100,y=100)
contact_entry=Spinbox(pdcomponent)
contact_entry.place(x=250,y=100,height=frontendconstant.ENTRY_HEIGHT, width=frontendconstant.ENTRY_WIDTH)

gender_lable=Label(pdcomponent,text="Gender",font=(frontendconstant.FONTFAMILY, frontendconstant.FONTSIZE),bg=frontendconstant.APPLICATION_COLOUR,fg=frontendconstant.FOURGROUND_COLOUR)
gender_lable.place(x=100,y=140)
gender=StringVar()
gender.set(False)
radio1=Radiobutton(pdcomponent,text="Male",variable=gender,value="Male")
radio1.place(x=250,y=140)
radio2=Radiobutton(pdcomponent,text="Female",variable=gender,value="Female")
radio2.place(x=320,y=140)
radio3=Radiobutton(pdcomponent,text="Others",variable=gender,value="Others")
radio3.place(x=400,y=140)

maratial_lable=Label(pdcomponent,text="Maratial Status",font=(frontendconstant.FONTFAMILY, frontendconstant.FONTSIZE),bg=frontendconstant.APPLICATION_COLOUR,fg=frontendconstant.FOURGROUND_COLOUR)
maratial_lable.place(x=100,y=180)
martial=StringVar()
martial.set(False)
radio4=Radiobutton(pdcomponent,text="Married",variable=martial,value="Married")
radio4.place(x=250,y=180)
radio5=Radiobutton(pdcomponent,text="Single",variable=martial,value="Single")
radio5.place(x=320,y=180)
radio6=Radiobutton(pdcomponent,text="Divorced",variable=martial,value="Divorced")
radio6.place(x=400,y=180)

age_lable=Label(pdcomponent,text="Age",font=(frontendconstant.FONTFAMILY, frontendconstant.FONTSIZE),bg=frontendconstant.APPLICATION_COLOUR,fg=frontendconstant.FOURGROUND_COLOUR)
age_lable.place(x=100,y=220)
age_entry=Spinbox(pdcomponent,from_=1,to_=99)
age_entry.place(x=250,y=220,height=frontendconstant.ENTRY_HEIGHT, width=frontendconstant.ENTRY_WIDTH)

submitbutton=Button(pdcomponent,text="SUBMIT",command=fillpd)
submitbutton.place(x=200,y=420,height=frontendconstant.BUTTON_HEIGHT, width=frontendconstant.BUTTON_WIDTH)

########################################################################################################################

name_ld=Label(ldcomponent,text="Name:UNKNOWN",font=(frontendconstant.FONTFAMILY, frontendconstant.FONTSIZE),bg=frontendconstant.APPLICATION_COLOUR,fg=frontendconstant.FOURGROUND_COLOUR)
name_ld.place(x=100,y=60)

contact_ld=Label(ldcomponent,text="Contact:UNKNOWN",font=(frontendconstant.FONTFAMILY, frontendconstant.FONTSIZE),bg=frontendconstant.APPLICATION_COLOUR,fg=frontendconstant.FOURGROUND_COLOUR)
contact_ld.place(x=100,y=100)

age_ld=Label(ldcomponent,text="Age:UNKNOWN",font=(frontendconstant.FONTFAMILY, frontendconstant.FONTSIZE),bg=frontendconstant.APPLICATION_COLOUR,fg=frontendconstant.FOURGROUND_COLOUR)
age_ld.place(x=100,y=140)

gender_ld=Label(ldcomponent,text="Gender:UNKNOWN",font=(frontendconstant.FONTFAMILY, frontendconstant.FONTSIZE),bg=frontendconstant.APPLICATION_COLOUR,fg=frontendconstant.FOURGROUND_COLOUR)
gender_ld.place(x=100,y=180)

martial_ld=Label(ldcomponent,text="Martial Status:UNKNOWN",font=(frontendconstant.FONTFAMILY, frontendconstant.FONTSIZE),bg=frontendconstant.APPLICATION_COLOUR,fg=frontendconstant.FOURGROUND_COLOUR)
martial_ld.place(x=100,y=220)

loginbutton=Button(lcomponent,text="LOGIN",command=login)
loginbutton.place(x=400,y=300,height=frontendconstant.BUTTON_HEIGHT, width=frontendconstant.BUTTON_WIDTH)

newuser_button=Button(lcomponent,text="Sign IN", command=gotoscomponent)
newuser_button.place(x=400,y=350,height=frontendconstant.BUTTON_HEIGHT, width=frontendconstant.BUTTON_WIDTH)

creat_account=Button(scomponent,text="CREATE ACCOUNT",command=createaccount)
creat_account.place(x=450,y=350,height=frontendconstant.BUTTON_HEIGHT, width=frontendconstant.BUTTON_WIDTH)

#######################################################################################################################

updatecomponent=Frame(rdcomponent,bg=frontendconstant.APPLICATION_COLOUR)
updatecomponent.place(x=10,y=20,height=500, width=600)
updatecomponent.place_forget()

namerd_lable=Label(updatecomponent,text="Name",font=(frontendconstant.FONTFAMILY, frontendconstant.FONTSIZE),bg=frontendconstant.APPLICATION_COLOUR,fg=frontendconstant.FOURGROUND_COLOUR)
namerd_lable.place(x=100,y=60)
namerd_entry=Entry(updatecomponent)
namerd_entry.place(x=400,y=60,height=frontendconstant.ENTRY_HEIGHT, width=frontendconstant.ENTRY_WIDTH)

contactrd_lable=Label(updatecomponent,text="Contact",font=(frontendconstant.FONTFAMILY, frontendconstant.FONTSIZE),bg=frontendconstant.APPLICATION_COLOUR,fg=frontendconstant.FOURGROUND_COLOUR)
contactrd_lable.place(x=100,y=100)
contactrd_entry=Entry(updatecomponent)
contactrd_entry.place(x=400,y=100,height=frontendconstant.ENTRY_HEIGHT, width=frontendconstant.ENTRY_WIDTH)

agerd_lable=Label(updatecomponent,text="Age",font=(frontendconstant.FONTFAMILY, frontendconstant.FONTSIZE),bg=frontendconstant.APPLICATION_COLOUR,fg=frontendconstant.FOURGROUND_COLOUR)
agerd_lable.place(x=100,y=140)
agerd_entry=Entry(updatecomponent)
agerd_entry.place(x=400,y=140,height=frontendconstant.ENTRY_HEIGHT, width=frontendconstant.ENTRY_WIDTH)

martialrd_lable=Label(updatecomponent,text="Martial status",font=(frontendconstant.FONTFAMILY, frontendconstant.FONTSIZE),bg=frontendconstant.APPLICATION_COLOUR,fg=frontendconstant.FOURGROUND_COLOUR)
martialrd_lable.place(x=100,y=180)
martialrd_entry=Entry(updatecomponent)
martialrd_entry.place(x=400,y=180,height=frontendconstant.ENTRY_HEIGHT, width=frontendconstant.ENTRY_WIDTH)

#set random question in below lable
index=random.randint(0,2)
global question
question=frontendconstant.SECURITYQUESTIONS[index]

abcd_lable=Label(updatecomponent,text=question,font=(frontendconstant.FONTFAMILY, frontendconstant.FONTSIZE),bg=frontendconstant.APPLICATION_COLOUR,fg=frontendconstant.FOURGROUND_COLOUR)
abcd_lable.place(x=100,y=220)
abcd_entry=Entry(updatecomponent)
abcd_entry.place(x=400,y=220,height=frontendconstant.ENTRY_HEIGHT, width=frontendconstant.ENTRY_WIDTH)

validation_button=Button(updatecomponent,text="Validate",command=validatesecurity)
validation_button.place(x=280,y=280,height=frontendconstant.BUTTON_HEIGHT, width=frontendconstant.BUTTON_WIDTH)

confirm_account=Button(updatecomponent,text="CONFIRM",command=updatedetails)
confirm_account.place(x=200,y=420,height=frontendconstant.BUTTON_HEIGHT, width=frontendconstant.BUTTON_WIDTH)

confirm_account['state']=DISABLED

########################################################################################################################

securitycomponent=Frame(fapp,bg=frontendconstant.APPLICATION_COLOUR)
securitycomponent.place(x=80,y=60,height=700,width=1200)
securitycomponent.place_forget()

security_component=Label(securitycomponent, text="SECURITY QUESTIONS", font=(frontendconstant.FONTFAMILY, frontendconstant.FONTSIZE),bg=frontendconstant.APPLICATION_COLOUR,fg=frontendconstant.FOURGROUND_COLOUR)
security_component.place(x=300,y=20)

userid_security1=Label(securitycomponent, text="USER ID", font=(frontendconstant.FONTFAMILY, frontendconstant.FONTSIZE),bg=frontendconstant.APPLICATION_COLOUR,fg=frontendconstant.FOURGROUND_COLOUR)
userid_security1.place(x=350,y=100)
userid_security=Entry(securitycomponent)
userid_security.place(x=450,y=100,height=frontendconstant.ENTRY_HEIGHT, width=frontendconstant.ENTRY_WIDTH)

question1=Label(securitycomponent, text= frontendconstant.SECURITYQUESTIONS[0], font=(frontendconstant.FONTFAMILY, frontendconstant.FONTSIZE),bg=frontendconstant.APPLICATION_COLOUR,fg=frontendconstant.FOURGROUND_COLOUR)
question1.place(x=350,y=150)
answer1_entry=Entry(securitycomponent)
answer1_entry.place(x=350,y=200,height=frontendconstant.ENTRY_HEIGHT, width=frontendconstant.ENTRY_WIDTH)

question2=Label(securitycomponent, text=frontendconstant.SECURITYQUESTIONS[1], font=(frontendconstant.FONTFAMILY, frontendconstant.FONTSIZE),bg=frontendconstant.APPLICATION_COLOUR,fg=frontendconstant.FOURGROUND_COLOUR)
question2.place(x=350,y=250)
answer2_entry=Entry(securitycomponent)
answer2_entry.place(x=350,y=300,height=frontendconstant.ENTRY_HEIGHT, width=frontendconstant.ENTRY_WIDTH)

question3=Label(securitycomponent, text=frontendconstant.SECURITYQUESTIONS[2], font=(frontendconstant.FONTFAMILY, frontendconstant.FONTSIZE),bg=frontendconstant.APPLICATION_COLOUR,fg=frontendconstant.FOURGROUND_COLOUR)
question3.place(x=350,y=350)
answer3_entry=Entry(securitycomponent)
answer3_entry.place(x=350,y=400,height=frontendconstant.ENTRY_HEIGHT, width=frontendconstant.ENTRY_WIDTH)

sq_button=Button(securitycomponent,text="SUBMIT", command= submitsecurityquestion)
sq_button.place(x=600,y=520,height=frontendconstant.BUTTON_HEIGHT, width=frontendconstant.BUTTON_WIDTH)



#step3 - run the application
fapp.mainloop()