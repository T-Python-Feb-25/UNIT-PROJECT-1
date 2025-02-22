from appmovie import AppMovie
import webbrowser
app=AppMovie()
def heandle_watchlist_and_reating(type:str)->None:
    id:str = input(f"If you want more info, enter the {type} ID or press Enter to continue: ").strip()
    if id.isdigit():
        valid_id:bool=app.get_more_info(id, type)
        if not valid_id==False:
            user_choice:str=input(f"if you want to rate thie {type} enter 'r' if you want to add to watchlist type 'w' press enter to continue:")
            print("="*50)

            if user_choice.lower()=='w':
                app.add_watchlist(id,type)
                input("press enter to continue:")
            elif user_choice.lower()=="r":
                while True:
                    try:
                        rating:int = int(input("Please enter your rating (0-10): "))
                        if rating>=0 and rating<=10:
                            break  
                        else:
                            print("Invalid input. Rating must be between 0 and 10.")
                    except ValueError:
                        print("Invalid input. Please enter a number between 0 and 10.")
                reviews:str=input("please enter your reaview:")       
                app.add_rating_and_reviews(id,type,rating,reviews)
                share_on_x:str=input("do you want share the review on x (y or n):")
                if share_on_x=="y":
                    app.share_tweet_on_x(id,type,rating,reviews)
                input("press enter to continue:")  

           
while True:
    if app.user.get_user_useername()==None:
        print("""
 ███████╗██╗  ██╗ ██████╗ ██╗    ██╗████████╗██╗███╗   ███╗███████╗
 ██╔════╝██║  ██║██╔═══██╗██║    ██║╚══██╔══╝██║████╗ ████║██╔════╝
 ███████╗███████║██║   ██║██║ █╗ ██║   ██║   ██║██╔████╔██║█████╗  
 ╚════██║██╔══██║██║   ██║██║███╗██║   ██║   ██║██║╚██╔╝██║██╔══╝  
 ███████║██║  ██║╚██████╔╝╚███╔███╔╝   ██║   ██║██║ ╚═╝ ██║███████╗
 ╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝    ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝
""")
        print("="*50)
        user_input:str = input('Please select an option:\n1. login\n2. register\n3. Exit the program\nYour choice: ').strip()
        print("="*50)
        if user_input=="1":
            app.user.login()
        elif user_input=='2':
            app.user.register()
        elif user_input=='3':
            exit()
        
    else:
        print("""
 ███████╗██╗  ██╗ ██████╗ ██╗    ██╗████████╗██╗███╗   ███╗███████╗
 ██╔════╝██║  ██║██╔═══██╗██║    ██║╚══██╔══╝██║████╗ ████║██╔════╝
 ███████╗███████║██║   ██║██║ █╗ ██║   ██║   ██║██╔████╔██║█████╗  
 ╚════██║██╔══██║██║   ██║██║███╗██║   ██║   ██║██║╚██╔╝██║██╔══╝  
 ███████║██║  ██║╚██████╔╝╚███╔███╔╝   ██║   ██║██║ ╚═╝ ██║███████╗
 ╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝    ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝
""")
        print("="*50)    
        user_input:str = input('''
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
Your choice: ''').strip()
        print("="*50)    

        if user_input == '1':
            title:str = input("Enter the title of the movie you want to search for: ").strip()
            if not title=="":
                app.search_by_qurey(title, "movie")
                heandle_watchlist_and_reating("movie")
             
            else:
                print("Please enter a valid movie title.")
        elif user_input == '2':
            title = input("Enter the title of the TV show you want to search for: ").strip()
            if not title=="":
                app.search_by_qurey(title, "tv")
                heandle_watchlist_and_reating("tv")
            else:
                print("Please enter a valid TV show title.")
        elif user_input=='3':
            app.get_movie_by_genre("movie")
            heandle_watchlist_and_reating("movie")
        elif user_input=='4':
            app.get_movie_by_genre("tvshow")
            heandle_watchlist_and_reating("tvshow")
        elif user_input=='5':
            user_choice:str=input("Would you like a recommendation for a movie or a TV show? Enter 'm' for movie or 't' for TV show: ").strip()
            if user_choice.lower()=='m':
                app.ai_recomdation("movie")
                title:str = input("Enter the title of the movie if you want more detailed:").strip()
                if not title=="":
                    app.search_by_qurey(title, "movie")
                    heandle_watchlist_and_reating("movie")
                
                else:
                    print("Please enter a valid movie title.")
                    
            elif user_choice.lower()=='t':
                app.ai_recomdation("tvshow")
                title:str = input("Enter the title of the tvshow if you want more detailed:").strip()
                if not title=="":
                    app.search_by_qurey(title, "tvshow")
                    heandle_watchlist_and_reating("tvshow")
                
                else:
                    print("Please enter a valid movie title.")


        elif user_input=='6':
            app.get_top_rated("movie")
            heandle_watchlist_and_reating("movie")
        elif user_input=='7':
            app.get_popular("movie")
            heandle_watchlist_and_reating("movie")
        elif user_input=='8':
            app.get_top_rated("tvshow")
            heandle_watchlist_and_reating("tvshow")

        elif user_input=='9':
            app.get_popular("tvshow")
            heandle_watchlist_and_reating("tvshow")
        elif user_input =='10':
            app.watch_list("movie")
            id:str=input("if you wanna delate from watchlist enter the id  or press enter to continue:")
            if id.isdigit():
                valid:bool=app.delate_from_watch_list(id,"movie")
                if valid:
                    user_choice:str=input("if you want to rate the movie type (r) or press enter to continue")
                    if user_choice.lower()=='r':
                        while True:
                            try:
                                rating:int = int(input("Please enter your rating (0-10): "))
                                if rating>=0 and rating<=10:
                                    break  
                                else:
                                    print("Invalid input. Rating must be between 0 and 10.")
                            except ValueError:
                                print("Invalid input. Please enter a number between 0 and 10.")
                    reviews:str=input("please enter your reaview:")       
                    app.add_rating_and_reviews(id,"movie",rating,reviews)
                    share_on_x:str=input("do you want share the review on x (y or n):")
                    if share_on_x=="y":
                        app.share_tweet_on_x(id,"movie",rating,reviews)
            elif id == '':
                pass
            else:
                input("Invaild id press enter to continue")
        elif user_input =='11':
            app.watch_list("tvshow")
            id:str=input("if you wanna delate from watchlist enter the id or press enter to continue:")
            if id.isdigit():
                valid:bool=app.delate_from_watch_list(id,"tvshow")
                if valid:
                    user_choice:str=input("if you want to rate the movie type (r) or press enter to continue")
                    if user_choice.lower()=='r':
                        while True:
                            try:
                                rating:int = int(input("Please enter your rating (0-10): "))
                                if rating>=0 and rating<=10:
                                    break  
                                else:
                                    print("Invalid input. Rating must be between 0 and 10.")
                            except ValueError:
                                print("Invalid input. Please enter a number between 0 and 10.")
                    reviews:str=input("please enter your reaview:")       
                    app.add_rating_and_reviews(id,"tv",rating,reviews)
                    share_on_x:str=input("do you want share the review on x (y or n):")
                    if share_on_x=="y":
                        app.share_tweet_on_x(id,"tv",rating,reviews)
            elif id == '':
                pass
            else:
                input("Invaild id press enter to continue")
        elif user_input=='12':
            app.already_watched("movie")
            user_choice:str=input("if you wanna delate from already watched enter the id:")
            if user_choice.isdigit() and not user_choice == "":
                app.delate_from_already_watched(user_choice,"movie")
            
        elif user_input=='13':
            app.already_watched("tv")
            user_choice:str=input("if you wanna delate from already watched enter the id:")
            if user_choice.isdigit() and not user_choice  == "":
                app.delate_from_already_watched(user_choice,"tv")
        elif user_input == '14':
            app.user.logout()
        elif user_input == '15':
            print("Thank you good bye")
            exit()
      
        else:
            print("Invalid option.")