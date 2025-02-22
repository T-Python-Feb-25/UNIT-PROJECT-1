#ملف تشغيل الكود و القائمة الرئيسية
#استداعاء للمكتبات المستخدمة في البرنامج

from colorama import Fore, Back, Style
import emoji

import log_in_and_ctreate_an_acconunt


print(Fore.MAGENTA)
print(emoji.emojize("welcome to travelmate :airplane:"))
answer=input("do you have an account yes or no")

if answer =="no":
     
     print("Well let's create one for you")
     firstName=input(Fore.MAGENTA+"Enter your first name\n")
     lastName=input(Fore.MAGENTA+"Enter your last name\n")
     while True:
        email=input(Fore.MAGENTA+"Enter your email\n")
        
#في حال لم يكن الايميل مثل الفورمات فسيتم الطلب من اليوزر اعادة كتابته
        if not log_in_and_ctreate_an_acconunt.email_format_check(email):
            print (Fore.RED+"the email format is invalid")
        else:
            break

        while True:
            password=input(Fore.MAGENTA+"Enter your password\n")
#في حال كانت كلمة المرور اقل من 8 كارتر لا تقبل 
            if len(password)<8:
                print(Fore.RED+"Password must consist of 8 characters")
            else:
                break
    
# في حال لم تتطابق كلمة المرور مع تأكيدها لا يتم انشاء الحساب حتى يدخل  المستخدم تأكيد كلمة المرور الصحيح
     while True:
        passwordConfirmation=input(Fore.RED+"Confirm your password please \n")

        if password==passwordConfirmation:
            print(Fore.MAGENTA+"Account created successfully!! Welcome to travelmate {}".format(firstName))
            log_in_and_ctreate_an_acconunt.add_users(firstName, lastName, email, password)
            break
        else :
            print(Fore.RED+"The passwords don't match ,try again please")

elif answer=="yes":

    firstName=input(Fore.MAGENTA+"Enter your first name\n")
    email=input(Fore.MAGENTA+"Enter your email\n")
    while True:
        password=input(Fore.MAGENTA+"Enter your password\n")
        #في حال كانت كلمةالمرور اقل من 8 كاركترز لا تقبل   
        if len(password)<8:
            print(Fore.RED+"Password must consist of 8 characters")
        else:
            print(Fore.MAGENTA+"Welcome back to travelmate {}".format(firstName))
            break
                
            log_in_and_ctreate_an_acconunt.users_login(email, password)


    
print("\nWhat would you like to do today :thinking_face: \n ")
while True:
    print("1.See my previous Plans   2.Create a new plan\n3.Exit the program")
    userChoice=input("\nEnter a number ")
    if userChoice=="1":
        print("your choice is num 1")
    elif userChoice=="2":
        print("your choice is num 2")
    elif userChoice=="3":
        print("thank you for using travelmate App ")
        break
    else:
        print(Fore.RED)
        print("Wrong choice, please reselect")
            
   
        