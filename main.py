from showtime import ShowTime
from colorama import Fore,Style
import time
app=ShowTime()

def More_info(category):
    id: str = input(f"{Fore.CYAN}If you want more info, enter the {category} ID or press Enter to continue:{Fore.YELLOW} ").strip()
    if id.isdigit():
        valid_id:bool=app.get_more_info(id, category)
        input("press enter to continue")
    
def handle_watchlist_and_rating(category: str) -> None:
    id: str = input(f"{Fore.CYAN}If you want more info, enter the {category} ID or press Enter to continue:{Fore.YELLOW} ").strip()
    if id.isdigit():
        valid_id: bool = app.get_more_info(id, category)
        if not valid_id == False:
            handle_rating_watchlist_after_deleate_it_from_watchlist(category,id)
          
def handle_rating_watchlist_after_deleate_it_from_watchlist(category,id):
    user_choice: str = input(
                f"{Fore.CYAN}Choose an option for this {category}:\n"
                "r  - Rate it\n"
                "w  - Add to Watchlist\n"
                "aw - Mark as Already Watched\n"
                f"Press Enter to continue:{Fore.YELLOW} "
            ).strip()
    print(f"{Fore.CYAN}=" * 50)

    if user_choice.lower() == 'w':
        app.add_watchlist(id, category)
        time.sleep(1)
    elif user_choice.lower() == "r":
        while True:
            try:
                rating: int = int(input(f"{Fore.CYAN}Please enter your rating (0-10):{Fore.YELLOW} "))
                if rating >= 0 and rating <= 10:
                    break
                else:
                    print(Fore.RED, "Invalid input. Rating must be between 0 and 10.")
                    print(Style.RESET_ALL, end="")

            except ValueError:
                print(Fore.RED, "Invalid input. Please enter a number between 0 and 10.")
                print(Style.RESET_ALL, end="")

        reviews: str = input(f"{Fore.CYAN}please enter your reaview:{Fore.YELLOW}")
        already_added=app.add_rating_and_reviews(id, category, rating, reviews)
        if already_added==None:
            print(f"{Fore.GREEN}Your review has been added!{Style.RESET_ALL}")
            share_on_x: str = input(f"{Fore.CYAN}do you want share the review on x (y or n):{Fore.YELLOW}")
            if share_on_x == "y":
                app.share_tweet_on_x(id, category, rating, reviews)
                input(f"{Fore.CYAN}press enter to continue:{Fore.YELLOW}")
    elif user_choice.lower() == 'aw':
        already_added=app.add_rating_and_reviews(id, category, None, None)
        if already_added==None:
            print(f"{Fore.GREEN}Successfully marked as Already Watched!{Style.RESET_ALL}")
            time.sleep(1)

    elif user_choice.lower()=="":
        pass

    else:
        input(f"{Fore.RED}Invaild option press enter to continue:")
        print(Style.RESET_ALL, end="")
    

logo='''
 ███████╗██╗  ██╗ ██████╗ ██╗    ██╗████████╗██╗███╗   ███╗███████╗
 ██╔════╝██║  ██║██╔═══██╗██║    ██║╚══██╔══╝██║████╗ ████║██╔════╝
 ███████╗███████║██║   ██║██║ █╗ ██║   ██║   ██║██╔████╔██║█████╗  
 ╚════██║██╔══██║██║   ██║██║███╗██║   ██║   ██║██║╚██╔╝██║██╔══╝  
 ███████║██║  ██║╚██████╔╝╚███╔███╔╝   ██║   ██║██║ ╚═╝ ██║███████╗
 ╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝    ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝'''
while True:
    if app.user.get_user_useername() == None:
        print(Fore.CYAN,logo)
        print("=" * 50)
        user_input: str = input(
            f'Please select an option:\n1. login\n2. register\n3. Continue as Guest\n4. Exit the program\nYour choice: {Style.RESET_ALL}{Fore.YELLOW}{Style.RESET_ALL}').strip()
        print(f"{Fore.CYAN}=" * 50)
        if user_input == "1":
            app.user.login()
        elif user_input == '2':
            app.user.register()
            time.sleep(1)
        elif user_input=='3':
            while True:
                print(Fore.CYAN,logo)
                print("=" * 50)
                user_input: str = input(f'''
Please select an option:
1.  Search for a Movie
2.  Search for a TV Show
3.  Search for a Movie by Genre
4.  Search for a TV Show by Genre
5.  Get AI Recommendations
6.  View Top Rated Movies
7.  View Popular Movies
8.  View Top Rated TV Shows
9.  View Popular TV Shows
10. login
11. Exit Program
Your choice:{Fore.YELLOW} ''').strip()
                print(f"{Fore.CYAN}=" * 50)
                if user_input=='1':
                    title: str = input(f"{Fore.CYAN}Enter the title of the movie you want to search for:{Fore.YELLOW} ").strip()
                    if not title == "":
                        empty=app.search_by_qurey(title, "movie")
                        if empty==None:
                            More_info("movie")

                    else:
                        print(f"{Fore.RED}Please enter a valid movie title.{Style.RESET_ALL}")
                        time.sleep(1)
                elif user_input=='2':
                    title: str = input(f"{Fore.CYAN}Enter the title of the Tvshow you want to search for:{Fore.YELLOW} ").strip()
                    if not title == "":
                        empty=app.search_by_qurey(title, "tvshow")
                        if empty==None:
                            More_info("tvshow")

                    else:
                        print(f"{Fore.RED}Please enter a valid Tvshow title.{Style.RESET_ALL}")
                        time.sleep(1)
                elif user_input == '3':
                    get_more_info=app.get_movie_by_genre("movie")
                    More_info("movie")
                elif user_input == '4':
                    get_more_info=app.get_movie_by_genre("tvshow")
                    More_info("tvshow")

                elif user_input == '5':
                    user_choice: str = input(
                        f"Would you like a recommendation for a movie or a TV show? Enter 'm' for movie or 't' for TV show: {Fore.YELLOW}").strip()
                    if user_choice.lower() == 'm':
                        app.ai_recomdation("movie")
                        title: str = input(f"{Fore.CYAN}Enter the title of the movie if you want more detailed:{Fore.YELLOW}").strip()
                        if not title == "":
                            app.search_by_qurey(title, "movie")
                            More_info("movie")

                        else:
                            print(f"{Fore.RED}Please enter a valid movie title.")
                            print(Style.RESET_ALL, end="")
                            time.sleep(1)


                    elif user_choice.lower() == 't':
                        app.ai_recomdation("tvshow")
                        title: str = input(f"{Fore.CYAN}Enter the title of the movie if you want more detailed:{Fore.YELLOW}").strip()
                        if not title == "":
                            app.search_by_qurey(title, "tvshow")
                            More_info("tvshow")

                        else:
                            print(f"{Fore.RED}Please enter a valid movie title.")
                            print(Style.RESET_ALL, end="")
                            time.sleep(1)
                    else:
                        print(f"{Fore.RED}Invalid option. Please try again.{Style.RESET_ALL}")
                        time.sleep(1)
                elif user_input == '6':
                    app.get_top_rated("movie")
                    More_info("movie")
                elif user_input == '7':
                    app.get_popular("movie")
                    More_info("movie")
                elif user_input == '8':
                    app.get_top_rated("tvshow")
                    More_info("tvshow")

                elif user_input == '9':
                    app.get_popular("tvshow")
                    More_info("tvshow")
                elif user_input == '10':
                    break
                elif user_input == '11':
                    print("Thank you good bye")
                    time.sleep(1)
                    exit()

                else:
                    print(Fore.RED, "Invalid option.")
                    print(Style.RESET_ALL, end="")
                    time.sleep(1)


            

        elif user_input == '4':
            print("Thank you good bye")
            exit()
        else:
            print(f"{Fore.RED}Invalid option. Please try again.{Style.RESET_ALL}")
            time.sleep(1)
    else:
        print(Fore.CYAN,logo)
        print("=" * 50)
        user_input: str = input(f'''
Please select an option:
1.  Search for a Movie
2.  Search for a TV Show
3.  Search for a Movie by Genre
4.  Search for a TV Show by Genre
5.  Get AI Recommendations
6.  View Top Rated Movies
7.  View Popular Movies
8.  View Top Rated TV Shows
9.  View Popular TV Shows
10. View Your Movie Watchlist
11. View Your TV Show Watchlist
12. View Movies You’ve Watched
13. View TV Shows You’ve Watched
14. Logout
15. Exit Program
Your choice:{Fore.YELLOW} ''').strip()
        print(f"{Fore.CYAN}=" * 50)
        if user_input=='1':
            title: str = input(f"{Fore.CYAN}Enter the title of the movie you want to search for:{Fore.YELLOW} ").strip()
            if not title == "":
                empty=app.search_by_qurey(title, "movie")
                if empty==None:
                    handle_watchlist_and_rating("movie")
            else:
                print(f"{Fore.RED}Please enter a valid movie title.{Style.RESET_ALL}")
                time.sleep(1)
        elif user_input=='2':
            title: str = input(f"{Fore.CYAN}Enter the title of the Tvshow you want to search for:{Fore.YELLOW} ").strip()
            if not title == "":
                empty=app.search_by_qurey(title, "tvshow")
                if empty==None:
                    handle_watchlist_and_rating("tvshow")
            else:
                print(f"{Fore.RED}Please enter a valid Tvshow title.{Style.RESET_ALL}")
                time.sleep(1)
        elif user_input == '3':
            get_more_info=app.get_movie_by_genre("movie")
            if not get_more_info==False:
                handle_watchlist_and_rating("movie")
        elif user_input == '4':
            get_more_info=app.get_movie_by_genre("tvshow")
            if not get_more_info==False:
                handle_watchlist_and_rating("tvshow")
        elif user_input == '5':
            user_choice: str = input(
                f"Would you like a recommendation for a movie or a TV show? Enter 'm' for movie or 't' for TV show: {Fore.YELLOW}").strip()
            if user_choice.lower() == 'm':
                app.ai_recomdation("movie")
                title: str = input(f"{Fore.CYAN}Enter the title of the movie if you want more detailed:{Fore.YELLOW}").strip()
                if not title == "":
                    app.search_by_qurey(title, "movie")
                    handle_watchlist_and_rating("movie")

                else:
                    print(f"{Fore.RED}Please enter a valid movie title.")
                    print(Style.RESET_ALL, end="")
                    time.sleep(1)


            elif user_choice.lower() == 't':
                app.ai_recomdation("tvshow")
                title: str = input(f"{Fore.CYAN}Enter the title of the movie if you want more detailed:{Fore.YELLOW}").strip()
                if not title == "":
                    app.search_by_qurey(title, "tvshow")
                    handle_watchlist_and_rating("tvshow")

                else:
                    print(f"{Fore.RED}Please enter a valid movie title.")
                    print(Style.RESET_ALL, end="")
                    time.sleep(1)
            else:
                print(f"{Fore.RED}Invalid option. Please try again.{Style.RESET_ALL}")
                time.sleep(1)
        elif user_input == '6':
            app.get_top_rated("movie")
            handle_watchlist_and_rating("movie")
        elif user_input == '7':
            app.get_popular("movie")
            handle_watchlist_and_rating("movie")
        elif user_input == '8':
            app.get_top_rated("tvshow")
            handle_watchlist_and_rating("tvshow")

        elif user_input == '9':
            app.get_popular("tvshow")
            handle_watchlist_and_rating("tvshow")
        elif user_input == '10':
            found_movie = app.watch_list("movie")
            if not found_movie == False:
                id: str = input(f"{Fore.CYAN}Enter the ID to remove from the watchlist or press enter to continue:{Fore.YELLOW}")
                if id.isdigit():
                    valid: bool = app.delate_from_watch_list(id, "movie")
                    if valid:
                        print(f"{Fore.GREEN}The movie has been removed successfully.{Style.RESET_ALL}")
                        time.sleep(1)
                        handle_rating_watchlist_after_deleate_it_from_watchlist("movie",id)     
                elif id == '':
                    pass
                else:
                    print(Fore.RED, "Invaild id")
                    print(Style.RESET_ALL, end="")
                    time.sleep(1)


            else:
                print(f"{Fore.RED}There are no movie in your watchlist.")
                time.sleep(1)
        elif user_input == '11':
            found_tv = app.watch_list("tvshow")
            if not found_tv == False:
                id: str = input(f"{Fore.CYAN}Enter the ID to remove from the watchlist or press enter to continue:{Fore.YELLOW}")
                if id.isdigit():
                    valid: bool = app.delate_from_watch_list(id, "tvshow")
                    if valid:
                        print(f"{Fore.GREEN}The tvshow has been removed successfully.{Style.RESET_ALL}")
                        time.sleep(1)
                        handle_rating_watchlist_after_deleate_it_from_watchlist("tvshow",id)
                elif id == '':
                    pass
                else:
                    print(f"{Fore.RED}Invaild id.{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}There are no Tvshow in your watchlist.{Style.RESET_ALL}")
                time.sleep(1)
        elif user_input == '12':
            found_movie = app.already_watched("movie")
            if not found_movie == False:
                id = input(f"{Fore.CYAN}Enter the ID to remove from your watched list, or press Enter to continue: {Fore.YELLOW}")

                if id.isdigit() and not id == "":
                    app.delate_from_already_watched(id, "movie")
                    print(f"{Fore.GREEN}The movie has been removed successfully.")
                    time.sleep(1)
            else:
                print(f"{Fore.RED}You haven't watched any movies yet. press enter to continue:{Fore.YELLOW}")
                time.sleep(1)


        elif user_input == '13':
            found_tv = app.already_watched("tv")
            if not found_tv == False:
                id = input(f"{Fore.CYAN}Enter the ID to remove from your watched list, or press Enter to continue: {Fore.YELLOW}")
                if id.isdigit() and not id == "":
                    app.delate_from_already_watched(id, "tv")
                    print(f"{Fore.GREEN}The tvshow has been removed successfully.")
                    time.sleep(1)

            else:
                print(f"{Fore.RED}You haven't watched any TV shows yet. press enter to continue:{Fore.YELLOW}")
                time.sleep(1)
        elif user_input == '14':
            app.user.logout()
        elif user_input == '15':
            print("Thank you good bye")
            time.sleep(1)
            exit()

        else:
            print(Fore.RED, "Invalid option.")
            print(Style.RESET_ALL, end="")
            time.sleep(1)




