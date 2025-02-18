from colorama import Fore, Back, Style
from art import *





def questions1():
    print("FIRST QUESTION: \n")
    while True:
        try:
            print("Q1 CHOICE THE RED WORD: ?")
            answer1 = (Back.RED + "RED")
            answer2 = (Fore.RED + "WORD")
            print(answer1 + Style.RESET_ALL, "               " + answer2)
            print(Style.RESET_ALL)
            ques1 = input("").lower().strip()
            if ques1 == "word":
                print(Back.GREEN + "GOOD JOB")
                print(Style.RESET_ALL)
                next = input("WRITE(" + Fore.YELLOW + " GO " + Style.RESET_ALL + ")TO GO NEXT! \n")
                if next == "go":
                   question2()
                   break
            elif  ques1 == "red":
                print(Back.RED + "FALL! TRY AGAIN.. ")
                print(Style.RESET_ALL)
        except Exception as e:
            print(e)

      

def choice():
    tprint("-WELCOME QUESTION GAME-", font="cybermedium")
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
        else:
            break
            
choice()
      