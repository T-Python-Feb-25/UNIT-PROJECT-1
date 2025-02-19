#ملف تشغيل الكود و القائمة الرئيسية
#استداعاء للمكتبات المستخدمة في البرنامج

from art import text2art
from colorama import Fore, Back, Style
import emoji
#استدعاء لملفات البرنامج

while True:
    print(Fore.MAGENTA)
    print("welcome to travelmate")
    print("\nWhat would you like to do today\n ")
    print("1.See my previous Plans   2.Create a new plan\n3.Exit the program")
    userChoice=input("\nEnter a number ")

    if userChoice=="1":
        print("your choice is num 1")
    elif userChoice=="2":
        print("your choice is num 2")
    elif userChoice=="3":
        print("thank you for using BookSwap app")
        break
    else:
        print(Fore.RED)
        print("Wrong choice, please reselect")
            
   
        