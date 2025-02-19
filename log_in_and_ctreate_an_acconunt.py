'''
This file has been created for the account creation process for 
the new user and login for the user who has used the program before 

'''
from colorama import Fore, Back, Style

print(Fore.MAGENTA)
#لا يمكن للمستخدم الدخول الى البرنامج بدون ان يكون له حساب فيه
print("welcome to travelmate")
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
#بناءا على اختيار المستخدم 2 يتم تسجيل الدخول في البرنامج 
elif userChoice1=="2":
    print(Fore.MAGENTA)
    firstName=input("Enter your first name\n")
    email=input("Enter your email\n")
    password=input("Enter your password\n")
    print("Welcome back to travelmat {}".format(firstName))
else:
    print(Fore.RED)
    print("Wrong choice, please reselect")
