from colorama import Fore, Back, Style
from art import *
from list import load_leaderboard 
from login import login_menu  


def questions1():
    print("FIRST QUESTION: \n")
    while True:
        try:
            print("Q1 CHOOSE THE RED WORD: ?")
            answer1 = (Back.RED + "RED")
            answer2 = (Fore.RED + "WORD")
            print(answer1 + Style.RESET_ALL, "               " + answer2 + Style.RESET_ALL)
            ques1 = input("").lower().strip()
            if ques1 == "word":
                print(Back.GREEN + "GOOD JOB" + Style.RESET_ALL)
                next = input("WRITE(" + Fore.YELLOW + " GO " + Style.RESET_ALL + ")TO GO NEXT! \n").lower()
                if next == "go":
                   question2()
                   break
            elif  ques1 == "red":
                print(Back.RED + "FAIL! TRY AGAIN.. " + Style.RESET_ALL)
            else:
                print(Back.RED + "PLEASE CHOOSE ANSWER!!")
                print(Style.RESET_ALL)
        except Exception as e:
            print(e)



def question2():
    print("SECOND QUESTION: \n")
    
    while True:
        try:
            print("Q2 CHOOSE THE PURPLE OPTION: ?")
            answer3 = (Back.MAGENTA + "OPTION")  
            answer4 = (Fore.MAGENTA + "PURPLE")
            print(answer3 + Style.RESET_ALL, "               " + answer4 + Style.RESET_ALL)
            ques2 = input("" ).lower().strip()
            if ques2 == "option":
                print(Back.GREEN + "GOOD JOB" + Style.RESET_ALL)
                next1 = input("WRITE(" + Fore.YELLOW + " GO " + Style.RESET_ALL + ")TO GO NEXT! \n").lower()
                if next1 == "go":
                    question3()
                    break
            elif  ques2 == "pink":
                print(Back.RED + "FAIL! TRY AGAIN.. " + Style.RESET_ALL)
            else:
                print(Back.RED + "PLEASE CHOOSE ANSWER!!")
                print(Style.RESET_ALL)
        except Exception as e:
            print(e)



def question3():
    total=0

    print("THIRD QUESTION:")
    while True:
        try:
            print("Q3 CHOOSE NUMBER ONE: ?")
            answer5 = (Back.BLUE + "NUMBER ONE")  
            answer6 = (Back.BLUE + "NUMBER 1")
            print(answer5 + Style.RESET_ALL, "               " + answer6 + Style.RESET_ALL)
            ques3 = input("" ).lower().strip()
            if ques3 == "number one":
                print(Back.GREEN + "GOOD JOB" + Style.RESET_ALL)
                total+=10
                next2 = input("WRITE(" + Fore.YELLOW + " GO " + Style.RESET_ALL + ")TO GO NEXT! \n").lower()
                if next2 == "go":
                    trophy()
                    break
            elif ques3 == "number 1":
                print(Back.RED + "FAIL! TRY AGAIN.. " + Style.RESET_ALL)
                point=10
            else:
                print(Back.RED + "PLEASE CHOOSE ANSWER!!")
                print(Style.RESET_ALL)
        except Exception as e:
            print(e)
    print (total)



def scoreboard():
    data = load_leaderboard()
    if not data:
        print("\n🚀 No leaderboard data available yet.\n")
        return

    print("\n🏆 Leaderboard 🏆\n")
    for player in data:
       print(f"{player['Rank']}⃣ {player['UserName']} - {player['Points']} Points")



def exit1():
    print(Back.CYAN + "THANK YOU LET US SEE YOU AGAIN")
    tprint("GOOD BYE", font = "rnd-medium")
    print(Style.RESET_ALL)



def trophy():
    print(Back.YELLOW + "CONGRATULATIONS YOU HAVE REACHED THE END.")
    tprint("THANK YOU", font="cybermedium")
    print(Style.RESET_ALL)
    exit1()



def continue1():
    while True:
        print("1. PART 1..")
        print("2. PART 2..")
        print("3. PART 3..")
        print("4. PART4..")
        choice2 = input("CHOOSE AN OPTION: ")
        if choice2 == "1":
            questions1()
        elif choice2 == "2":
            question2()
        elif choice2 == "3":
            question3()
        elif choice2 == "4":
            exit1()   
            break         



def choice(username):
    tprint("-WELCOME QUESTION GAME-", font="cybermedium")
    print(f"\n👤 Logged in as: {username}")
    
    while True:
        print(Style.RESET_ALL)
        print("1. START GAME..")
        print("2. CONTINUE..")
        print("3. SCORE BOARD..")
        print("4. EXIT.")
        choice1 = input("CHOOSE AN OPTION: ")
    
        if choice1 == "1":
            questions1()
        elif choice1 == "2":
            continue1()
        elif choice1 == "3":
            scoreboard()
        elif choice1 == "4":
            exit1()
            break
        else:
            print("⚠️ Invalid choice, please try again!")

if __name__ == "__main__":
    username = login_menu()
    choice(username)
