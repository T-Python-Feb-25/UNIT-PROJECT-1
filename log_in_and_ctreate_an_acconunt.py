'''
This file has been created for the account creation process for 
the new user and login for the user who has used the program before

git_users function is to upload and read Json's 
file and check if the user exists or not  

add_users Created to add new user 
information to Json's file 

'''
from colorama import Fore
import json
import emoji
#مكتبة ضمنية في البايثون للتحقق من صحة طريقه متابة الايميل المدخل من المستخدم 
import re 

#دالة لجلب معلومات حسابات المستخدمين من ملف جيسون 
def get_users():
    try :
        with open("users_account_file.json","r",encoding="utf-8") as file:
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

 # دالة للتحقق من صحة صيغة الايميبل المدخل من قبل المستخدم 
def email_format_check(email):
    format=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{3,}$'
    return re.fullmatch(format ,email)
