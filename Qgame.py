from colorama import Fore, Back, Style
from art import *
from login import load_users, save_users, login_menu 


def questions1():
    users = load_users()
    total = users[username]["points"]
    print("FIRST QUESTION: \n")
    while True:
        try:
            print("Q1 CHOOSE THE RED WORD: ❔")
            answer1 = (Back.RED + "1️⃣  RED")
            answer2 = (Fore.RED + "2️⃣  WORD")
            print(answer1 + Style.RESET_ALL, "               " + answer2 + Style.RESET_ALL)
            ques1 = input("").lower().strip()
            if ques1 == "2":
                print(Back.GREEN + "GOOD JOB ✅" + Style.RESET_ALL)
                total += 100
                users[username]["points"] = total
                save_users(users)
                print(f"YOUR POINT {Fore.GREEN} {total} {Style.RESET_ALL} KEEP GOING TO BE BEST ONE")  
                next1 = input("WRITE(" + Fore.YELLOW + " 🆗 " + Style.RESET_ALL + ")TO GO NEXT! \n").lower()
                if next1 == "ok":
                   question2()
                   break
            elif  ques1 == "1":
                print(Back.RED + "FAIL! TRY AGAIN..❗️ " + Style.RESET_ALL)
            else:
                print(Back.RED + "PLEASE CHOOSE ANSWER ⛔️ " + Style.RESET_ALL)
        except Exception as e:
            print(e)



def question2():
    users = load_users()
    total = users[username]["points"]
    print("SECOND QUESTION: \n")
    
    while True:
        try:
            print("Q2 CHOOSE THE PURPLE OPTION: ❔")
            answer3 = (Back.MAGENTA + "1️⃣  OPTION")  
            answer4 = (Fore.MAGENTA + "2️⃣  PURPLE")
            print(answer3 + Style.RESET_ALL, "               " + answer4 + Style.RESET_ALL)
            ques2 = input("" ).lower().strip()
            if ques2 == "1":
                print(Back.GREEN + "GOOD JOB ✅" + Style.RESET_ALL)
                total += 100
                users[username]["points"] = total
                save_users(users)
                print(f"YOUR POINT {Fore.GREEN} {total} {Style.RESET_ALL} KEEP GOING TO BE BEST ONE")  
                next2 = input("WRITE(" + Fore.YELLOW + " 🆗 " + Style.RESET_ALL + ")TO GO NEXT! \n").lower()
                if next2 == "ok":
                    question3()
                    break
            elif  ques2 == "2":
                print(Back.RED + "FAIL! TRY AGAIN..❗️ " + Style.RESET_ALL)
            else:
                print(Back.RED + "PLEASE CHOOSE ANSWER ⛔️ " + Style.RESET_ALL)
        except Exception as e:
            print(e)



def question3():
    users = load_users()
    total = users[username]["points"]
    print("THIRD QUESTION:")
    while True:
        try:
            print("Q3 CHOOSE NUMBER ONE: ❔")
            answer5 = (Back.BLUE + "1️⃣  NUMBER ONE")  
            answer6 = (Back.BLUE + " 2️⃣  NUMBER  1️⃣")
            print(answer5 + Style.RESET_ALL, "               " + answer6 + Style.RESET_ALL)
            ques3 = input("" ).lower().strip()
            if ques3 == "1":
                print(Back.GREEN + "GOOD JOB ✅" + Style.RESET_ALL)
                total += 100
                users[username]["points"] = total
                save_users(users)
                print(f"YOUR POINT {Fore.GREEN} {total} {Style.RESET_ALL} KEEP GOING TO BE BEST ONE")          
                next3 = input("WRITE(" + Fore.YELLOW + " 🆗 " + Style.RESET_ALL + ")TO GO NEXT! \n").lower()
                if next3 == "ok":
                    question4()
                    break
            elif ques3 == "2":
                print(Back.RED + "FAIL! TRY AGAIN..❗️ " + Style.RESET_ALL)
            else:
                print(Back.RED + "PLEASE CHOOSE ANSWER ⛔️ " + Style.RESET_ALL)
        except Exception as e:
            print(e)
            
            
def question4():
    users = load_users()
    total = users[username]["points"]
    print("FOURTH QUESTION:")
    while True:
        try:
            print("Q4 CHOOSE RIGHT ANSWER : ❔")
            answer7 = (Back.LIGHTWHITE_EX + "1️⃣  RIGHT")  
            answer8 = (Back.LIGHTWHITE_EX + "2️⃣  ANSWER")
            print(answer7 + Style.RESET_ALL, "               " + answer8 + Style.RESET_ALL)
            ques4 = input("").lower().strip()
            if ques4 == "1":
                print(Back.GREEN + "GOOD JOB ✅" + Style.RESET_ALL)
                total += 100
                users[username]["points"] = total
                save_users(users)
                print(f"YOUR POINT {Fore.GREEN} {total} {Style.RESET_ALL} KEEP GOING TO BE BEST ONE")          
                next4 = input("WRITE(" + Fore.YELLOW + " 🆗 " + Style.RESET_ALL + ")TO GO NEXT! \n").lower()
                if next4 == "ok":
                    question5()
                    break
            elif ques4 == "2":
                print(Back.RED + "FAIL! TRY AGAIN..❗️ " + Style.RESET_ALL)
            else:
                print(Back.RED + "PLEASE CHOOSE ANSWER ⛔️ " + Style.RESET_ALL)
        except Exception as e:
            print(e)
            
def question5():
    users = load_users()
    total = users[username]["points"]
    print("FIFTH QUESTION:")
    while True:
        try:
            print("Q5 CHOOSE FIRST ANSWER : ❔")
            answer9 = (Back.MAGENTA + "1️⃣  SECOND")  
            answer10 = (Back.MAGENTA + "2️⃣  FIRST")
            print(answer9 + Style.RESET_ALL, "               " + answer10 + Style.RESET_ALL)
            ques5 = input("").lower().strip()
            if ques5 == "1":
                print(Back.GREEN + "GOOD JOB ✅" + Style.RESET_ALL)
                total += 100
                users[username]["points"] = total
                save_users(users)
                print(f"YOUR POINT {Fore.GREEN} {total} {Style.RESET_ALL} KEEP GOING TO BE BEST ONE")          
                next5 = input("WRITE(" + Fore.YELLOW + " 🆗 " + Style.RESET_ALL + ")TO GO NEXT! \n").lower()
                if next5 == "ok":
                    CATEGORY()
                    break
            elif ques5 == "2":
                print(Back.RED + "FAIL! TRY AGAIN..❗️ " + Style.RESET_ALL)
            else:
                print(Back.RED + "PLEASE CHOOSE ANSWER ⛔️ " + Style.RESET_ALL)
        except Exception as e:
            print(e)


def question6():
    users = load_users()
    total = users[username]["points"]
    print("SIXTH QUESTION:")
    while True:
        try:
            print("Q6 THE FIRST WOMAN TO WIN A NOBEL PRIZE WAS MARIE CURIE : ❔")
            answer11 = (Back.GREEN + "1️⃣  Lexi Anderson.")  
            answer12 = (Back.GREEN + "2️⃣  Marie Curie.")
            print(answer11 + Style.RESET_ALL, "               " + answer12 + Style.RESET_ALL)
            ques6 = input("").lower().strip()
            if ques6 == "2":
                print(Back.GREEN + "GOOD JOB ✅" + Style.RESET_ALL)
                total += 100
                users[username]["points"] = total
                save_users(users)
                print(f"YOUR POINT {Fore.GREEN} {total} {Style.RESET_ALL} KEEP GOING TO BE BEST ONE")          
                next6 = input("WRITE(" + Fore.YELLOW + " 🆗 " + Style.RESET_ALL + ")TO GO NEXT! \n").lower()
                if next6 == "ok":
                    question7()
                    break
            elif ques6 == "1":
                print(Back.RED + "FAIL! TRY AGAIN..❗️ " + Style.RESET_ALL)
            else:
                print(Back.RED + "PLEASE CHOOSE ANSWER ⛔️ " + Style.RESET_ALL)
        except Exception as e:
            print(e)
    
def question7():
    users = load_users()
    total = users[username]["points"]
    print("SEVENTH QUESTION:")
    while True:
        try:
            print("Q7 WHAT IS THE CAPITAL OF JAPAN : ❔")
            answer13 = (Back.YELLOW + "1️⃣  TOKYO")  
            answer14 = (Back.YELLOW + "2️⃣  KYOTO")
            print(answer13 + Style.RESET_ALL, "               " + answer14 + Style.RESET_ALL)
            ques7 = input("").lower().strip()
            if ques7 == "1":
                print(Back.GREEN + "GOOD JOB ✅" + Style.RESET_ALL)
                total += 100
                users[username]["points"] = total
                save_users(users)
                print(f"YOUR POINT {Fore.GREEN} {total} {Style.RESET_ALL} KEEP GOING TO BE BEST ONE")          
                next7 = input("WRITE(" + Fore.YELLOW + " 🆗 " + Style.RESET_ALL + ")TO GO NEXT! \n").lower()
                if next7 == "ok":
                    question8()
                    break
            elif ques7 == "2":
                print(Back.RED + "FAIL! TRY AGAIN..❗️ " + Style.RESET_ALL)
            else:
                print(Back.RED + "PLEASE CHOOSE ANSWER ⛔️ " + Style.RESET_ALL)
        except Exception as e:
            print(e)

def question8():
    users = load_users()
    total = users[username]["points"]
    print("EIGHTH QUESTION:")
    while True:
        try:
            print("Q8 WHO INVENTED THE ELECTRIC LIGHT BULB : ❔")
            answer15 = (Back.BLUE + "1️⃣  THOMAS EDISON")  
            answer16 = (Back.BLUE + "2️⃣  NIKOLA TESLA")
            print(answer15 + Style.RESET_ALL, "               " + answer16 + Style.RESET_ALL)
            ques8 = input("").lower().strip()
            if ques8 == "1":
                print(Back.GREEN + "GOOD JOB ✅" + Style.RESET_ALL)
                total += 100
                users[username]["points"] = total
                save_users(users)
                print(f"YOUR POINT {Fore.GREEN} {total} {Style.RESET_ALL} KEEP GOING TO BE BEST ONE")          
                next8 = input("WRITE(" + Fore.YELLOW + " 🆗 " + Style.RESET_ALL + ")TO GO NEXT! \n").lower()
                if next8 == "ok":
                    question9()
                    break
            elif ques8 == "2":
                print(Back.RED + "FAIL! TRY AGAIN..❗️ " + Style.RESET_ALL)
            else:
                print(Back.RED + "PLEASE CHOOSE ANSWER ⛔️ " + Style.RESET_ALL)
        except Exception as e:
            print(e)

def question9():
    users = load_users()
    total = users[username]["points"]
    print("NINTH QUESTION:")
    while True:
        try:
            print("Q9 WHAT IS THE LARGEST OCEAN IN THE WORLD : ❔")
            answer17 = (Back.RED + "1️⃣  PACIFIC OCEAN")  
            answer18 = (Back.RED + "2️⃣  ATLANTIC OCEAN")
            print(answer17 + Style.RESET_ALL, "               " + answer18 + Style.RESET_ALL)
            ques9 = input("").lower().strip()
            if ques9 == "1":
                print(Back.GREEN + "GOOD JOB ✅" + Style.RESET_ALL)
                total += 100
                users[username]["points"] = total
                save_users(users)
                print(f"YOUR POINT {Fore.GREEN} {total} {Style.RESET_ALL} KEEP GOING TO BE BEST ONE")          
                next9 = input("WRITE(" + Fore.YELLOW + " 🆗 " + Style.RESET_ALL + ")TO GO NEXT! \n").lower()
                if next9 == "ok":
                    question10(username)
                    break
            elif ques9 == "2":
                print(Back.RED + "FAIL! TRY AGAIN..❗️ " + Style.RESET_ALL)
            else:
                print(Back.RED + "PLEASE CHOOSE ANSWER ⛔️ " + Style.RESET_ALL)
        except Exception as e:
            print(e)

def question10(username):
    users = load_users()
    total = users[username]["points"]
    print("TENTH QUESTION:")
    while True:
        try:
            print("Q10 ON WHICH CONTINENT IS EGYPT LOCATED : ❔")
            answer19 = (Back.CYAN + "1️⃣  ASIA")  
            answer20 = (Back.CYAN + "2️⃣  AFRICA")
            print(answer19 + Style.RESET_ALL, "               " + answer20 + Style.RESET_ALL)
            ques10 = (input("").lower().strip())
            if ques10 == "1":
                print(Back.GREEN + "GOOD JOB ✅" + Style.RESET_ALL)
                total += 100
                users[username]["points"] = total
                save_users(users)
                print(f"YOUR POINT {Fore.GREEN} {total} {Style.RESET_ALL} KEEP GOING TO BE BEST ONE")          
                next10 = input("WRITE(" + Fore.YELLOW + " 🆗 " + Style.RESET_ALL + ")TO GO NEXT! \n").lower()
                if next10 == "ok":
                    trophy()
                    return False
            elif ques10 == "2":
                print(Back.RED + "FAIL! TRY AGAIN..❗️ " + Style.RESET_ALL)
            else:
                print(Back.RED + "PLEASE CHOOSE ANSWER ⛔️ " + Style.RESET_ALL)
        except Exception as e:
            print(e)
            
            

def load_leaderboard():
    users = load_users()

    sorted_users = sorted(users.items(), key=lambda x: x[1]['points'], reverse=True)
    return sorted_users


def scoreboard():
    leaderboard = load_leaderboard()
    if not leaderboard:
        print("\n🚀 No leaderboard data available yet.\n")
        return

    print("\n🏆 Leaderboard 🏆\n")
    for rank, (username, data) in enumerate(leaderboard, start=1):
        print(f"{rank}️⃣ {data['name']} ({username}) - {data['points']} points")


def exit1():
    print(Back.CYAN + "THANK YOU LET US SEE YOU AGAIN")
    tprint("GOOD BYE", font = "rnd-medium")
    print(Style.RESET_ALL)



def trophy():
    print(Back.YELLOW + "CONGRATULATIONS YOU HAVE REACHED THE END.")
    tprint("THANK YOU", font="cybermedium")
    print(Style.RESET_ALL)
    scoreboard()



def CATEGORY():
    while True:
        print("-BRIN QUESTIONS 1️⃣\n-CULTURAL QUESTIONS 2️⃣\n-MATH QUESTIONS (SOON) 3️⃣\n-EXIT 4️⃣")
        choice2 = input("CHOOSE AN OPTION: ")
        if choice2 == "1":
            questions1()
            continue
        elif choice2 == "2":
            output = question6()
            if output == False:
                return False
        elif choice2 == "3":
            print(Back.GREEN + "SOON IN NEXT UPDATE" + Style.RESET_ALL)
        elif choice2 == "4":
            return False        



def choice(username):
    tprint("-WELCOME QUESTION GAME-", font="cybermedium")
    print(f"\n👤 Logged in as: {username}")
    
    while True:
        print(Style.RESET_ALL)
        print("1️⃣  START GAME.. \n2️⃣  CATEGORY.. \n3️⃣  SCORE BOARD.. \n4️⃣  EXIT..")
        choice1 = input("CHOOSE AN OPTION: ")
    
        if choice1 == "1":
            questions1()
        elif choice1 == "2":
            output = CATEGORY()
            if output == False:
                exit1()
                break
        elif choice1 == "3":
            scoreboard()
        elif choice1 == "4":
            exit1()
            break
        else:
            print("⛔️ Invalid choice, please try again ⛔️")

if __name__ == "__main__":
    username = login_menu()
    choice(username)
