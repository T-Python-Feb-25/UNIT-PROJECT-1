#ملف تشغيل الكود و القائمة الرئيسية
#استداعاء للمكتبات المستخدمة في البرنامج
from art import text2art
from colorama import Fore
import emoji
import Weather
import restaurants_suggestions
import log_in_and_ctreate_an_acconunt
import events_and_activities
import Previous_Plans

print(Fore.LIGHTBLUE_EX)
print(emoji.emojize(text2art("welcome to travelmate",font="standard")))
print(Fore.LIGHTBLACK_EX+"------------------------------------------")
answer=input(Fore.LIGHTBLUE_EX+"\ndo you have an account yes or no\n")

if answer =="no":
     
     print(Fore.BLUE+"Well let's create one for you")
     firstName=input(Fore.LIGHTBLACK_EX+"Enter your first name\n")
     lastName=input(Fore.LIGHTBLACK_EX+"Enter your last name\n")

     while True:
        email=input(Fore.LIGHTBLACK_EX+"Enter your email\n")
        
#في حال لم يكن الايميل مثل الفورمات فسيتم الطلب من اليوزر اعادة كتابته
        if not log_in_and_ctreate_an_acconunt.email_format_check(email):
            print (Fore.RED+"the email format is invalid")
        else:
            break    
            

     while True:
            password=input(Fore.LIGHTBLACK_EX+"Enter your password\n")
#في حال كانت كلمة المرور اقل من 8 كارتر لا تقبل 
            if len(password)<8:
                print(Fore.RED+"Password must consist of 8 characters")
            else:
                break
    
# في حال لم تتطابق كلمة المرور مع تأكيدها لا يتم انشاء الحساب حتى يدخل  المستخدم تأكيد كلمة المرور الصحيح
     while True:
        passwordConfirmation=input(Fore.BLUE+"Confirm your password please \n")

        if password==passwordConfirmation:
            print(Fore.GREEN+"Account created successfully!! Welcome {} :airplane:".format(firstName))
            print(Fore.LIGHTBLACK_EX+"------------------------------------------")
            log_in_and_ctreate_an_acconunt.add_users(firstName, lastName, email, password)
            break
        else :
            print(Fore.RED+"The passwords don't match ,try again please")

elif answer=="yes":

    users_accounts=log_in_and_ctreate_an_acconunt.get_users()
    firstName=input(Fore.LIGHTBLACK_EX+"Enter your first name\n")
    while True:  
        email=input(Fore.LIGHTBLACK_EX+"Enter your email\n") 
        
        if email not in users_accounts:
            print(Fore.RED+"This email does not exist. Make sure the email is correct ")
        else:
            break
    while True:

        password=input(Fore.LIGHTBLACK_EX+"Enter your password\n")
        #في حال كانت كلمةالمرور اقل من 8 كاركترز لا تقبل   
        if len(password)<8:
            print(Fore.RED+"Password must consist of 8 characters")
            continue
        
        if users_accounts[email]["password"] !=password:
            print(Fore.RED+"Incorrect password, please check it")
        else:
            print(Fore.GREEN+"Welcome back to travelmat {}".format(firstName))
            print(Fore.LIGHTBLACK_EX+"------------------------------------------")
            break
    
       
while True:  
    print(Fore.BLUE+"\nWhat would you like to do today  \n ")
    print(Fore.LIGHTBLACK_EX+"1.See my previous Plans   \n2.Create a new plan\n"+Fore.RED+"3.Exit the program")
    userChoice=input(Fore.LIGHTBLACK_EX+"\nEnter a number ")
    if userChoice=="1":
       Previous_Plans.view_Previous_Plans(email)

    elif userChoice=="2":
        city=input(Fore.BLUE+"Please enter the name of the city you would like to go to \n")
        date=input(Fore.BLUE+"What is the arrival date? (YYYY-MM-DD)\n")
        Weather.get_weather(email,city,date)
        print(Fore.LIGHTBLACK_EX+"------------------------------------------")
        restaurants_suggestions=restaurants_suggestions.get_restaurant(email,city)

        if restaurants_suggestions:
            print(Fore.LIGHTBLUE_EX+"\nRestaurant recommendations in {} are:".format(city))
            for r in restaurants_suggestions:
                print(Fore.LIGHTBLACK_EX+"{} Restaurant ".format(r["name"]))
                print(Fore.LIGHTBLACK_EX+"------------------------------------------")
                break
            else:
                print(Fore.RED + "No restaurant suggestions found.")
            continue
        
        temperature, weather_condition = Weather.get_weather(email, city,date)
        events_and_activities.add_events(email,city, temperature)

    elif userChoice=="3":
        print(Fore.GREEN+"thank you for using travelmate App, Come back again")
        break
    else:
        print(Fore.RED+"Wrong choice, please reselect")
            
