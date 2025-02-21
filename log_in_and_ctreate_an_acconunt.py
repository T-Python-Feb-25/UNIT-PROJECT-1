'''
This file has been created for the account creation process for 
the new user and login for the user who has used the program before

git_users function is to upload and read Json's 
file and check if the user exists or not  

add_users Created to add new user 
information to Json's file 

'''
from colorama import Fore, Back, Style
import json
import emoji
#مكتبة ضمنية في البايثون للتحقق من صحة طريقه متابة الايميل المدخل من المستخدم 
import re 

#دالة لجلب معلومات حسابات المستخدمين من ملف جيسون 
def get_users():
    try :
        with open("users_account_file.json","r") as file:
            return json.load(file)
    except FileNotFoundError :
        return {}
    
#دالة لاضافه مستخدمين جدد الى ملف جيسون 
def add_users(firstName,lastName,email,password):
    users_accounts=get_users()
    if email in users_accounts:
        print (Fore.RED+"The email you entered already exists, please try to log in or try another email ")
        return
    users_accounts[email]={"firstName":firstName, "lastName":lastName, 
    "password":password, "Travel Plans":[]}

#فتح ملف جيسون لكتابة او اضافة معلومات المستخدم الجديد فيه
    with open("users_account_file.json", "w") as file:
        json.dump (users_accounts, file, indent=4)

#دالة لتسجيل الدخول للمستخدمين الذين استخدمو المنصة سابقا 
def users_login(email,password ):

     users_accounts=get_users()

     if email not in users_accounts:
        print(Fore.RED+"This email does not exist. Make sure the email is correct ")
        return False
        while True:
            if users_accounts[email]["password"] ==password:
                print(Fore.MAGENTA+"Welcome back to travelmat {}".format(firstName))
                return True
            else:
                print(Fore.RED+"Incorrect password, please check it")
                password= input(Fore.MAGENTA+"Enter your password again")

 # دالة للتحقق من صحة صيغة الايميبل المدخل من قبل المستخدم 
def email_format_check(email):
    format=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2, }$'
    return re.match(format ,email)



#لا يمكن للمستخدم الدخول الى البرنامج بدون ان يكون له حساب فيه
print(Fore.MAGENTA+"welcome to travelmate :airplane:")
userChoice1=input(Fore.MAGENTA+"do you want to \n1:Create a new account  2:Sign in\n")
# بناء على اختيار المستخدم 1 و الذي يمثل انشاء حساب جديد يتم طلب معلوماته لانشاء حساب جديد
if userChoice1=="1":
    firstName=input(Fore.MAGENTA+"Enter your first name\n")
    lastName=input(Fore.MAGENTA+"Enter your last name\n")
    while True:
        email=input(Fore.MAGENTA+"Enter your email\n")
        if not email_format_check(email):
            print (Fore.RED+"the email format is invalid")

        password=input(Fore.MAGENTA+"Enter your password\n")
# في حال لم تتطابق كلمة المرور مع تأكيدها لا يتم انشاء الحساب حتى يدخل  المستخدم تأكيد كلمة المرور الصحيح
    
        passwordConfirmation=input(Fore.RED+"Confirm your password please \n")

        if password==passwordConfirmation:
            print(Fore.MAGENTA+"Account created successfully!! Welcome to travelmate {}".format(firstName))
            add_users(firstName, lastName, email, password)
            break
        else :
            print(Fore.RED+"The passwords don't match ,try again please")


#بناءا على اختيار المستخدم 2 يتم تسجيل الدخول في البرنامج 
elif userChoice1=="2":
    firstName=input(Fore.MAGENTA+"Enter your first name\n")
    email=input(Fore.MAGENTA+"Enter your email\n")
    while True:
        password=input(Fore.MAGENTA+"Enter your password\n")
        #في حال كانت كلمةالمرور اقل من 8 كاركترز لا تقبل   
        if len(password)<8:
            print(Fore.RED+"Password must consist of 8 characters")
        else:
            print(Fore.MAGENTA+"Welcome back to travelmat {}".format(firstName))
            break
                
            users_login(email, password)


#في حال ادخل المستخدم خيار خاطئ سينبؤه البرنامج بذلك
else:
    print(Fore.RED+"Wrong choice, please reselect")
