from appmovie import AppMovie
import webbrowser
app=AppMovie()
def heandle_watchlist_and_reating(type):
    id = input("If you want more info, enter the movie ID or press Enter to continue: ").strip()
    if id.isdigit():
        valid_id=app.get_more_info(id, type)
        if not valid_id==False:
            user_choice=input("if you want to rate thie movie enter 'r' if you want to add to watchlist type 'w' press enter to continue:")
            if user_choice.lower()=='w':
                app.add_watchlist(id,type)
            elif user_choice.lower()=="r":
                while True:
                    try:
                        rating = int(input("Please enter your rating (0-10): "))
                        if rating>=0 and rating<=10:
                            break  
                        else:
                            print("Invalid input. Rating must be between 0 and 10.")
                    except ValueError:
                        print("Invalid input. Please enter a number between 0 and 10.")
                reviews=input("please enter your reaview:")       
                app.add_rating_and_reviews(id,type,rating,reviews)
                share_on_x=input("do you want share the review on x (y or n)")
                if share_on_x=="y":
                    app.share_tweet_on_x(id,type,rating,reviews)
                  

            else:
                print("Continuing without more details...")
while True:
    if app.user.get_user_useername()==None:
        user_input = input('Please select an option:\n1. login\n2. register\n3. Exit the program\nYour choice: ').strip()
        if user_input=="1":
            app.user.login()
        elif user_input=='2':
            app.user.register()
        elif user_input=='3':
            exit()
    else:    
        user_input = input('''
Please select an option:
1. Search for a Movie
2. Search for a TV Show
3. get top rated movie
4- get popular movie
5. get top rated tv show
6. get popular tv show
7. get your watchlist movie
8. get your watchlist tv
9. get your already watched
10.use ai for recommendation
11. logout
12. Exit the program
Your choice: ''').strip()
        if user_input == '1':
            title = input("Enter the title of the movie you want to search for: ").strip()
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
            app.get_top_rated("movie")
            heandle_watchlist_and_reating("movie")
        elif user_input=='4':
            app.get_popular("movie")
            heandle_watchlist_and_reating("movie")
        elif user_input=='5':
            app.get_top_rated("tv")
            heandle_watchlist_and_reating("tv")

        elif user_input=='6':
            app.get_popular("tv")
            heandle_watchlist_and_reating("tv")
        elif user_input =='7':
            app.watch_list("movie")
            user_choice=input("if you wanna delate from watchlist enter the id:")
            if user_choice.isdigit():
                app.delate_from_watch_list(user_choice,"movie")
        elif user_input =='8':
            app.watch_list("tvshow")
            user_choice=input("if you wanna delate from watchlist enter the id:")
            if user_choice.isdigit():
                app.delate_from_watch_list(user_choice,"tvshow")
        elif user_input=='9':
            app.already_watched()
        elif user_input=='10':
            ai_recommendation=input("enter something:")
            print(app.ai.recomdation_movie(ai_recommendation))
        elif user_input == '11':
            app.user.logout()
        elif user_input == '12':
            print("Thank you good bye")
            exit()
        else:
            print("Invalid option.")