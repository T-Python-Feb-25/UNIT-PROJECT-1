#ملف تشغيل الكود و القائمة الرئيسية
#استداعاء للمكتبات المستخدمة في البرنامج

from art import text2art
from colorama import Fore, Back, Style
#استدعاء لملفات البرنامج
'''
import log_in_and_ctreate_an_acconunt
import available_books 
import favorite_books_list 
import book_purchase_requeste 
'''
while True:
    print(Fore.MAGENTA)
    print("welcome to bookswap App\nchose what do you want to do\n ")

    try: 
        print("1.See available books    2.Go to my favorite\n3.go to my requests      4.Search for a book\n5.Exit the program")
        userChoice=input("\nEnter a number ")

        if userChoice=="1":
            print("your choice is num 1")
        elif userChoice=="2":
            print("your choice is num 2")
        elif userChoice=="3":
            print("your choice is num 3")
        elif userChoice=="4":
            print("your choice is num 4")
        elif userChoice=="5":
            print("thank you for using BookSwap")
            break  
    except :
        if userChoice!="1"|"2"|"3"|"4"|"5":
          print("Wrong choice, please reselect ")