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


print(Fore.MAGENTA)
#دالة لجلب معلومات حسابات المستخدمين من ملف جيسون 
def get_users():
    try :
        with open("users_account_file.json","r") as file:
            return json.load(file)
    except FileDoesNotExistEror :
        return {}
    
#دالة لاضافه مستخدمين جدد الى ملف جيسون 
def add_users(firstName,lastName,email,password):
    users_accounts=get_users()
    if email in users_accounts:
        print ("The email you entered already exists, please try to log in or try another email ")
        return
    users_accounts[email]={"firstName":firstName, "lastName":lastName, 
    "password":password, "Travel Plans":[]}
#فتح ملف جيسون لكتابة او اضافة معلومات المستخدم الجديد فيه
    with open("users_account_file.json", "+a") as file:
        json.dump (users_accounts, file, indent=4)
    
#لا يمكن للمستخدم الدخول الى البرنامج بدون ان يكون له حساب فيه
print("welcome to travelmate :airplane:")
userChoice1=input("do you want to \n1:Create a new account  2:Sign in\n")
# بناء على اختيار المستخدم 1 و الذي يمثل انشاء حساب جديد يتم طلب معلوماته لانشاء حساب جديد
if userChoice1=="1":
    firstName=input("Enter your first name\n")
    lastName=input("Enter your last name\n")
    email=input("Enter your email\n")
    password=input("Enter your password\n")
# في حال لم تتطابق كلمة المرور مع تأكيدها لا يتم انشاء الحساب حتى يدخل  المستخدم تأكيد كلمة المرور الصحيح
    while True:
        passwordConfirmation=input("Enter your password again for Confirmation\n")

        if password==passwordConfirmation:
            print("Account created successfully!! Welcome to travelmate {}".format(firstName))
        else :
            print(Fore.RED)
            print("The passwords don't match")

        add_users(firstName, lastName, email, password)

#بناءا على اختيار المستخدم 2 يتم تسجيل الدخول في البرنامج 
elif userChoice1=="2":
    print(Fore.MAGENTA)
    firstName=input("Enter your first name\n")
    email=input("Enter your email\n")
    while True:
        password=input("Enter your password\n")
#في حال كانت كلمةالمرور اقل من 8 كاركترز لا تقبل   
        if len(password)!=8:
            print("Password must consist of 8 characters")
        else:
            print("Welcome back to travelmat {}".format(firstName))
else:
    print(Fore.RED)
    print("Wrong choice, please reselect")
