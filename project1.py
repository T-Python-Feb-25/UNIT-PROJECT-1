from colorama import Fore, Back, Style
from art import *
from list import load_leaderboard 
from login import login_menu  


def questions1():
    total = 0 
    print("FIRST QUESTION: \n")
    while True:
        try:
            print("Q1 CHOOSE THE RED WORD: ❔")
            answer1 = (Back.RED + "1️⃣  RED")
            answer2 = (Fore.RED + "2️⃣  WORD")
            print(answer1 + Style.RESET_ALL, "               " + answer2 + Style.RESET_ALL)
            ques1 = input("").lower().strip()
            if ques1 == "word":
                print(Back.GREEN + "GOOD JOB ✅" + Style.RESET_ALL)
                total += 100
                print(f"YOUR POINT {Fore.GREEN} {total} {Style.RESET_ALL} KEEP GOING TO BE BEST ONE")  
                next1 = input("WRITE(" + Fore.YELLOW + " 🆗 " + Style.RESET_ALL + ")TO GO NEXT! \n").lower()
                if next1 == "ok":
                   question2()
                   break
            elif  ques1 == "red":
                print(Back.RED + "FAIL! TRY AGAIN..❗️ " + Style.RESET_ALL)
                point11 = total
            else:
                print(Back.RED + "PLEASE CHOOSE ANSWER ⛔️")
                print(Style.RESET_ALL)
        except Exception as e:
            print(e)



def question2():
    total = 0
    print("SECOND QUESTION: \n")
    
    while True:
        try:
            print("Q2 CHOOSE THE PURPLE OPTION: ❔")
            answer3 = (Back.MAGENTA + "1️⃣  OPTION")  
            answer4 = (Fore.MAGENTA + "2️⃣  PURPLE")
            print(answer3 + Style.RESET_ALL, "               " + answer4 + Style.RESET_ALL)
            ques2 = input("" ).lower().strip()
            if ques2 == "option":
                print(Back.GREEN + "GOOD JOB ✅" + Style.RESET_ALL)
                total += 100
                print(f"YOUR POINT {Fore.GREEN} {total} {Style.RESET_ALL} KEEP GOING TO BE BEST ONE")  
                next2 = input("WRITE(" + Fore.YELLOW + " 🆗 " + Style.RESET_ALL + ")TO GO NEXT! \n").lower()
                if next2 == "ok":
                    question3()
                    break
            elif  ques2 == "pink":
                print(Back.RED + "FAIL! TRY AGAIN..❗️ " + Style.RESET_ALL)
                point11 = total
            else:
                print(Back.RED + "PLEASE CHOOSE ANSWER ⛔️")
                print(Style.RESET_ALL)
        except Exception as e:
            print(e)



def question3():
    total = 0
    print("THIRD QUESTION:")
    while True:
        try:
            print("Q3 CHOOSE NUMBER ONE: ❔")
            answer5 = (Back.BLUE + "1️⃣  NUMBER ONE")  
            answer6 = (Back.BLUE + " 2️⃣  NUMBER  1️⃣")
            print(answer5 + Style.RESET_ALL, "               " + answer6 + Style.RESET_ALL)
            ques3 = input("" ).lower().strip()
            if ques3 == "number one":
                print(Back.GREEN + "GOOD JOB ✅" + Style.RESET_ALL)
                total += 100
                print(f"YOUR POINT {Fore.GREEN} {total} {Style.RESET_ALL} KEEP GOING TO BE BEST ONE")          
                next3 = input("WRITE(" + Fore.YELLOW + " 🆗 " + Style.RESET_ALL + ")TO GO NEXT! \n").lower()
                if next3 == "ok":
                    question4()
                    break
            elif ques3 == "number 1":
                print(Back.RED + "FAIL! TRY AGAIN..❗️ " + Style.RESET_ALL)
                point11 = total
            else:
                print(Back.RED + "PLEASE CHOOSE ANSWER ⛔️" + Style.RESET_ALL)
                print(Style.RESET_ALL)
        except Exception as e:
            print(e)
            
            
def question4():
    total = 0
    print("FOURTH QUESTION:")
    while True:
        try:
            print("Q4 CHOOSE RIGHT ANSWER : ❔")
            answer7 = (Back.LIGHTWHITE_EX + "1️⃣  RIGHT")  
            answer8 = (Back.LIGHTWHITE_EX + "2️⃣  ANSWER")
            print(answer7 + Style.RESET_ALL, "               " + answer8 + Style.RESET_ALL)
            ques4 = input("").lower().strip()
            if ques4 == "right":
                print(Back.GREEN + "GOOD JOB ✅" + Style.RESET_ALL)
                total += 100
                print(f"YOUR POINT {Fore.GREEN} {total} {Style.RESET_ALL} KEEP GOING TO BE BEST ONE")          
                next4 = input("WRITE(" + Fore.YELLOW + " 🆗 " + Style.RESET_ALL + ")TO GO NEXT! \n").lower()
                if next4 == "ok":
                    question5()
                    break
            elif ques4 == "answer":
                print(Back.RED + "FAIL! TRY AGAIN..❗️ " + Style.RESET_ALL)
                point11 = total
            else:
                print(Back.RED + "PLEASE CHOOSE ANSWER ⛔️" + Style.RESET_ALL)
                print(Style.RESET_ALL)
        except Exception as e:
            print(e)
            
def question5():
    total = 0
    print("FIFTH QUESTION:")
    while True:
        try:
            print("Q5 CHOOSE FIRST ANSWER : ❔")
            answer9 = (Back.LIGHTWHITE_EX + "1️⃣  SECOND")  
            answer10 = (Back.LIGHTWHITE_EX + "2️⃣  FIRST")
            print(answer9 + Style.RESET_ALL, "               " + answer10 + Style.RESET_ALL)
            ques5 = input("").lower().strip()
            if ques5 == "second":
                print(Back.GREEN + "GOOD JOB ✅" + Style.RESET_ALL)
                total += 100
                point11 = total
                print(point11)
                print(f"YOUR POINT {Fore.GREEN} {total} {Style.RESET_ALL} KEEP GOING TO BE BEST ONE")          
                next5 = input("WRITE(" + Fore.YELLOW + " 🆗 " + Style.RESET_ALL + ")TO GO NEXT! \n").lower()
                if next5 == "ok":
                    question6()
                    break
            elif ques5 == "first":
                print(Back.RED + "FAIL! TRY AGAIN..❗️ " + Style.RESET_ALL)
            else:
                print(Back.RED + "PLEASE CHOOSE ANSWER ⛔️" + Style.RESET_ALL)
                print(Style.RESET_ALL)
        except Exception as e:
            print(e)


def question6():
    total = 0
    print("SIXTH QUESTION:")
    while True:
        try:
            print("Q6 WHICH WORD IS SPELLED CORRECTLY : ❔")
            answer11 = (Back.LIGHTWHITE_EX + "1️⃣  CORRECTLY")  
            answer12 = (Back.LIGHTWHITE_EX + "2️⃣  WRONG")
            print(answer11 + Style.RESET_ALL, "               " + answer12 + Style.RESET_ALL)
            ques6 = input("").lower().strip()
            if ques6 == "correctly":
                print(Back.GREEN + "GOOD JOB ✅" + Style.RESET_ALL)
                total += 100
                point11 = total
                print(point11)
                print(f"YOUR POINT {Fore.GREEN} {total} {Style.RESET_ALL} KEEP GOING TO BE BEST ONE")          
                next6 = input("WRITE(" + Fore.YELLOW + " 🆗 " + Style.RESET_ALL + ")TO GO NEXT! \n").lower()
                if next6 == "ok":
                    question7()
                    break
            elif ques6 == "wrong":
                print(Back.RED + "FAIL! TRY AGAIN..❗️ " + Style.RESET_ALL)
            else:
                print(Back.RED + "PLEASE CHOOSE ANSWER ⛔️" + Style.RESET_ALL)
                print(Style.RESET_ALL)
        except Exception as e:
            print(e)
    
def question7():
    total = 0
    print("SEVENTH QUESTION:")
    while True:
        try:
            print("Q7 WHICH ONE IS THE ODD ONE OUT : ❔")
            answer13 = (Back.LIGHTWHITE_EX + "1️⃣  THIS ONE")  
            answer14 = (Back.LIGHTWHITE_EX + "2️⃣  THE OTHER ONE")
            print(answer13 + Style.RESET_ALL, "               " + answer14 + Style.RESET_ALL)
            ques7 = input("").lower().strip()
            if ques7 == "this one":
                print(Back.GREEN + "GOOD JOB ✅" + Style.RESET_ALL)
                total += 100
                point11 = total
                print(point11)
                print(f"YOUR POINT {Fore.GREEN} {total} {Style.RESET_ALL} KEEP GOING TO BE BEST ONE")          
                next7 = input("WRITE(" + Fore.YELLOW + " 🆗 " + Style.RESET_ALL + ")TO GO NEXT! \n").lower()
                if next7 == "ok":
                    question8()
                    break
            elif ques7 == "this other one":
                print(Back.RED + "FAIL! TRY AGAIN..❗️ " + Style.RESET_ALL)
            else:
                print(Back.RED + "PLEASE CHOOSE ANSWER ⛔️" + Style.RESET_ALL)
                print(Style.RESET_ALL)
        except Exception as e:
            print(e)

def question8():
    total = 0
    print("EIGHTH QUESTION:")
    while True:
        try:
            print("Q8 WHAT HAPPENS IF YOU PICK THIS OPTION : ❔")
            answer15 = (Back.LIGHTWHITE_EX + "1️⃣  NOTHING")  
            answer16 = (Back.LIGHTWHITE_EX + "2️⃣  YOU WIN")
            print(answer15 + Style.RESET_ALL, "               " + answer16 + Style.RESET_ALL)
            ques8 = input("").lower().strip()
            if ques8 == "nothing":
                print(Back.GREEN + "GOOD JOB ✅" + Style.RESET_ALL)
                total += 100
                point11 = total
                print(point11)
                print(f"YOUR POINT {Fore.GREEN} {total} {Style.RESET_ALL} KEEP GOING TO BE BEST ONE")          
                next8 = input("WRITE(" + Fore.YELLOW + " 🆗 " + Style.RESET_ALL + ")TO GO NEXT! \n").lower()
                if next8 == "ok":
                    question9()
                    break
            elif ques8 == "you win":
                print(Back.RED + "FAIL! TRY AGAIN..❗️ " + Style.RESET_ALL)
            else:
                print(Back.RED + "PLEASE CHOOSE ANSWER ⛔️" + Style.RESET_ALL)
                print(Style.RESET_ALL)
        except Exception as e:
            print(e)

def question9():
    total = 0
    print("NINTH QUESTION:")
    while True:
        try:
            print("Q9 WHICH OPTION IS THE CORRECT ONE : ❔")
            answer17 = (Back.LIGHTWHITE_EX + "1️⃣  THE INCORRECT ONE")  
            answer18 = (Back.LIGHTWHITE_EX + "2️⃣  THE CORRECT ONE")
            print(answer17 + Style.RESET_ALL, "               " + answer18 + Style.RESET_ALL)
            ques9 = input("").lower().strip()
            if ques9 == "the correct one":
                print(Back.GREEN + "GOOD JOB ✅" + Style.RESET_ALL)
                total += 100
                point11 = total
                print(point11)
                print(f"YOUR POINT {Fore.GREEN} {total} {Style.RESET_ALL} KEEP GOING TO BE BEST ONE")          
                next9 = input("WRITE(" + Fore.YELLOW + " 🆗 " + Style.RESET_ALL + ")TO GO NEXT! \n").lower()
                if next9 == "ok":
                    question10()
                    break
            elif ques9 == "the incorrect one":
                print(Back.RED + "FAIL! TRY AGAIN..❗️ " + Style.RESET_ALL)
            else:
                print(Back.RED + "PLEASE CHOOSE ANSWER ⛔️" + Style.RESET_ALL)
                print(Style.RESET_ALL)
        except Exception as e:
            print(e)

def question10():
    total = 0
    print("TENTH QUESTION:")
    while True:
        try:
            print("Q10 WHICH NUMBER COMES LAST IN THIS LIST : ❔")
            answer17 = (Back.LIGHTWHITE_EX + "1️⃣  3")  
            answer18 = (Back.LIGHTWHITE_EX + "2️⃣  2")
            print(answer17 + Style.RESET_ALL, "               " + answer18 + Style.RESET_ALL)
            ques10 = input("").lower().strip()
            if ques10 == "3":
                print(Back.GREEN + "GOOD JOB ✅" + Style.RESET_ALL)
                total += 100
                point11 = total
                print(point11)
                print(f"YOUR POINT {Fore.GREEN} {total} {Style.RESET_ALL} KEEP GOING TO BE BEST ONE")          
                next10 = input("WRITE(" + Fore.YELLOW + " 🆗 " + Style.RESET_ALL + ")TO GO NEXT! \n").lower()
                if next10 == "ok":
                    trophy()
                    return False
            elif ques10 == "2":
                print(Back.RED + "FAIL! TRY AGAIN..❗️ " + Style.RESET_ALL)
            else:
                print(Back.RED + "PLEASE CHOOSE ANSWER ⛔️" + Style.RESET_ALL)
                print(Style.RESET_ALL)
        except Exception as e:
            print(e)
            
            
def scoreboard():
    data = load_leaderboard()
    if not data:
        print("\n🚀 No leaderboard data available yet.\n")
        return

    print("\n🏆 Leaderboard 🏆\n")
    for player in data:
       print(f"{player} - {data[player]['points']} points")



def exit1():
    print(Back.CYAN + "THANK YOU LET US SEE YOU AGAIN")
    tprint("GOOD BYE", font = "rnd-medium")
    print(Style.RESET_ALL)



def trophy():
    print(Back.YELLOW + "CONGRATULATIONS YOU HAVE REACHED THE END.")
    tprint("THANK YOU", font="cybermedium")
    print(Style.RESET_ALL)
    scoreboard()



def continue1():
    while True:
        print("-PART 1️⃣\n-PART 2️⃣\n-PART 3️⃣\n-PART 4️⃣\n-EXIT 5️⃣")
        choice2 = input("CHOOSE AN OPTION: ")
        if choice2 == "1":
            questions1()
            continue
        elif choice2 == "2":
            question2()
            continue
        elif choice2 == "3":
            question3()
            continue
        elif choice2 == "4":
            output = question5()
            if output == False:
                return False
        elif choice2 == "5":
            return False        



def choice(username):
    tprint("-WELCOME QUESTION GAME-", font="cybermedium")
    print(f"\n👤 Logged in as: {username}")
    
    while True:
        print(Style.RESET_ALL)
        print("1️⃣  START GAME.. \n2️⃣  CONTINUE.. \n3️⃣  SCORE BOARD.. \n4️⃣  EXIT..")
        choice1 = input("CHOOSE AN OPTION: ")
    
        if choice1 == "1":
            questions1()
        elif choice1 == "2":
            output = continue1()
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
