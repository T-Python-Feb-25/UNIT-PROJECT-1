from movie import Movie
from tvshow import Tvshow
from user import User
from ai import Ai
import urllib.parse
import webbrowser
from colorama import Fore, Back, Style
from dotenv import load_dotenv
import os
import time
class ShowTime:    
    def __init__(self):
        load_dotenv()
        self.__api_key = os.getenv('api_key_movie')
        self.__base_url = 'https://api.themoviedb.org/3/'
        self.movie=Movie(self.__api_key)
        self.tvshow=Tvshow(self.__api_key)
        self.user=User()
        self.ai=Ai()
    def configure(self):
        load_dotenv()
    def search_by_qurey(self,query,category):
        '''Searches for movies or TV shows based on a query string.
            
            args:
                query(str):the search key word
                category:category to search for.

                '''
        try:
            if category=="movie":
                movies=self.movie.search_query(query)
                if movies:
                    print(f"{Fore.MAGENTA}="*50)
                    for i,movie in enumerate(movies):
                        print(f"{Fore.MAGENTA}{i+1}.id:{movie["id"]} title:{movie["title"]} release_date:{movie["release_date"]}")
                        print("-"*80)
                else:
                    print(f"{Fore.RED}No Movies found for '{query}'.{Style.RESET_ALL}")
                    time.sleep(1)
                    return False

            else:
                tv_shows=self.tvshow.search_query(query)
                if tv_shows:
                    print(F"{Fore.CYAN}="*50)


                    for i,tvshow in enumerate(tv_shows):
                        print(f"{Fore.MAGENTA}{i+1}.id:{tvshow["id"]} title:{tvshow["title"]} release_date:{tvshow["release_date"]}")
                        print("-"*80)
                else:
                    print(f"{Fore.RED}No TV shows found for '{query}'.{Style.RESET_ALL}")
                    time.sleep(1)
                    return False

        except Exception as e:
            print(f"{Fore.RED}{e}")
            print(f"{Fore.RED}{f"Error: {category} not found. The ID may be invalid."}{Style.RESET_ALL}")
            time.sleep(1)
    
    def get_more_info(self,id,category):
        '''get and displays detailed information about a movie or TV show.
           args:
                id(str):the id of the movie or tvshow
                category(str):(movie or tvshow)
            return:
                none:if its done correctly
                False:if there is exception

                

'''
        try:
            if category=="movie":
                movies=self.movie.get_more_info_by_id(id)
                url=f"https://www.imdb.com/title/{movies["imdb_id"]}"
                print(f"{Fore.MAGENTA}id: {movies["id"]}\nTitle: {movies["title"]}\nRelease Date: {movies["release_date"]}\nGenres: {" ".join([gen for gen in movies["genres"]])}\nOverview: {movies["overview"]}\nTMDb Rating: {movies["TMDb_Rating"]}")
                print("for more info:",end="")
                print(Fore.BLUE,url)    
                print(Style.RESET_ALL,end="")
                print(f"{Fore.CYAN}="*50)

            
            else:
                tv_show=self.tvshow.get_more_info_by_id(id)
                url=f"https://www.imdb.com/title/{tv_show["imdb_id"]}"
                print(f"{Fore.MAGENTA}id: {tv_show["id"]}\nTitle: {tv_show["title"]}\nRelease Date: {tv_show["release_date"]}\nGenres: {" ".join([gen for gen in tv_show["genres"]])}\nnumber of seasons: {tv_show["number_of_seasons"]}\nnumber_of_episodes:{tv_show["number_of_episodes"]}\nOverview: {tv_show["overview"]}\nTMDb Rating: {tv_show["TMDb_Rating"]}")
                print("for more info:",end="")
                print(Fore.BLUE,url) 
                print(Style.RESET_ALL,end="")
                print(f"{Fore.CYAN}="*50)
        except Exception as e:
            print(f"{Fore.RED}{e}")
            print(f"{Fore.RED}{f"Error: {category} not found. The ID may be invalid."}{Style.RESET_ALL}")
            time.sleep(1)
            return False
    def get_popular(self,category):
        ''' get and print a list of popular movies or TV shows.
            args:                
                category:category to search for.'''
        try:
            if category=="movie":
                movies=self.movie.get_popular_movie()
                for movie in movies:
                    print(f"{Fore.MAGENTA}id: {movie["id"]}\ntitle: {movie["title"]}\nRelease Date: {movie["release_date"]}\nTMDb Rating: {movie["TMDb_Rating"]}\nvote count: {movie["TMDb_vote_count"]}")
                    print("-"*20)
            else:
                tv_shows=self.tvshow.get_popular_tv()  
                for tvshow in tv_shows:
                    print(f"{Fore.MAGENTA}id: {tvshow["id"]}\ntitle: {tvshow["title"]}\nRelease Date: {tvshow["release_date"]}\nTMDb Rating: {tvshow["TMDb_Rating"]}\nvote count: {tvshow["TMDb_vote_count"]}")
                    print("-"*20)      
        except Exception as e:
            print(f"{Fore.RED}{e}")
            print(f"{Fore.RED}{f"Error: {category} not found. The ID may be invalid."}{Style.RESET_ALL}")
            time.sleep(1)
    def get_top_rated(self,category):
        ''' get and print a list of top rated movies or TV shows.
            args:                
                category:category to search for.'''
        try:
            if category=="movie":
                movies=self.movie.get_top_rated_movie()
                for movie in movies:
                    print(f"{Fore.MAGENTA}id: {movie["id"]}\nTitle: {movie["title"]}\nRelease Date: {movie["release_date"]}\nTMDb Rating: {movie["TMDb_Rating"]}\nvote count: {movie["TMDb_vote_count"]}")
                    print("-"*20)
            else:
                tv_shows=self.tvshow.get_top_rated_tv()
                for tvshow in tv_shows:
                    print(f"{Fore.MAGENTA}id: {tvshow["id"]}\ntitle: {tvshow["title"]}\nRelease Date: {tvshow["release_date"]}\nTMDb Rating: {tvshow["TMDb_Rating"]}\nvote count: {tvshow["TMDb_vote_count"]}")
                    print("-"*20)   
        except Exception as e:
            print(f"{Fore.RED}{e}")
            print(f"{Fore.RED}{f"Error: {category} not found. The ID may be invalid."}{Style.RESET_ALL}")
            time.sleep(1)
    def get_basic_info_by_id(self,id,category):
        '''get and print basic information about a movie or TV show.
            args:
                id(str):the id of the movie or tvshow
                category(str):(movie or tvshow)


'''
        try:
            if category=="movie":
                movies=self.movie.get_basic_info_by_id(id)
                print(f"id: {movies["id"]}\nTitle: {movies["title"]}\nRelease Date: {movies["release_date"]}\nGenres: {" ".join([gen for gen in movies["genres"]])}\nduration: {movies["duration"]}")
            else:
                tv_shows=self.tvshow.get_basic_info_by_id(id)
                print(f"id: {tv_shows["id"]}\nTitle: {tv_shows["title"]}\nRelease Date: {tv_shows["release_date"]}\nGenres: {" ".join([gen for gen in tv_shows["genres"]])}\nnumber of seasons: {tv_shows["number_of_seasons"]}")
        except Exception as e:
            print(f"{Fore.RED}{e}")
            print(f"{Fore.RED}{f"Error: {category} not found. The ID may be invalid."}{Style.RESET_ALL}")
            time.sleep(1)
    def add_watchlist(self,id,category):
        '''Adds a movie or TV show to the user's watchlist.
            args:
                id(str):the id of the movie or tvshow
                category(str):(movie or tvshow)
        '''
        if category=="movie":
            if id not in   self.user.get_user_data_login()["movie"]["movie_watch_list"]:
                self.user.get_user_data_login()["movie"]["movie_watch_list"].append(id)
                self.user.save_data()
                print(f"{Fore.GREEN}The movie is added to the watchlist.{Style.RESET_ALL}")
            else:
                print(Fore.RED,"The movie is already added to the watchlist.")
                print(Style.RESET_ALL,end="")


        else:
            if id not in self.user.get_user_data_login()["tv"]["tv_watch_list"]:
                self.user.get_user_data_login()["tv"]["tv_watch_list"].append(id)
                self.user.save_data()
                print("The tv show is added to the watchlist.")
            else:
                print(Fore.RED,"The tv show is already added to the watchlist.")
                print(Style.RESET_ALL,end="")

    def add_rating_and_reviews(self,id,category,rating,reviews):
        '''Adds a rating and review for a movie or TV show.
            args:
                id(str):the id of the movie or tvshow
                category(str):(movie or tvshow)
                rating (int): User's rating from 0 to 10.
                reviews(str):user review


        '''
        already_rated=False
        if category=="movie":
            if id in  self.user.get_user_data_login()["movie"]["movie_watch_list"]:
                self.delate_from_watch_list(id,"movie")
            
            for movie_id in self.user.get_user_data_login()["movie"]["rating"]:
                if id in movie_id:
                    already_rated=True
            if already_rated==False:
                self.user.get_user_data_login()["movie"]["rating"].append({id:{"review":reviews,"rating":rating}})
                self.user.save_data()
            else:
                print(f"{Fore.RED}You have already rated this movie.{Style.RESET_ALL}")
                time.sleep(1)
                return False

        else:
            if id in self.user.get_user_data_login()["tv"]["tv_watch_list"]:
                self.delate_from_watch_list(id,"tv")
            for tv_show_id in self.user.get_user_data_login()["tv"]["rating"]:
                if id in tv_show_id:
                    already_rated=True
            if already_rated==False:
                self.user.get_user_data_login()["tv"]["rating"].append({id:{"review":reviews,"rating":rating}})
                self.user.save_data()
            else:
                print(f"{Fore.RED}You have already rated this tvshow.{Style.RESET_ALL}")
                time.sleep(1)
                return False


    def watch_list(self,category):
        '''Displays the user's watchlist for movies or TV shows.
            args:
                category(str):(movie or tvshow)
                

        '''
        try:
            if category=="tvshow":
                if  self.user.get_user_data_login()["tv"]["tv_watch_list"]:
                    print(f"{Fore.MAGENTA}your tvshow:")
                    print("-"*10)
                    for watchlist in  self.user.get_user_data_login()["tv"]["tv_watch_list"]:
                        self.get_basic_info_by_id(watchlist,"tv")
                        print("-"*10)
                else:
                    return False
                    
            else:
                if self.user.get_user_data_login()["movie"]["movie_watch_list"]:
                    print(f"{Fore.MAGENTA}your movie:")
                    print("-"*10)
                    for watchlist in  self.user.get_user_data_login()["movie"]["movie_watch_list"]:
                        self.get_basic_info_by_id(watchlist,"movie")
                        print("-"*10)
                else:
                    return False
        except Exception as e:
            print(f"{Fore.RED}{e}")
            print(f"{Fore.RED}{f"Error: {category} not found. The ID may be invalid."}{Style.RESET_ALL}")
            time.sleep(1)
    def delate_from_watch_list(self,id,category):
        '''Removes a movie or TV show from the user's watchlist.
            args:
                id(str):the id of the movie or tvshow
                category(str):(movie or tvshow)'''
        if category=="movie":
            if id in  self.user.get_user_data_login()["movie"]["movie_watch_list"]:
                self.user.get_user_data_login()["movie"]["movie_watch_list"].remove(id)
                self.user.save_data()
                return True
            else:
                print(Fore.RED,"Invaild id")
                print(Style.RESET_ALL,end="")
                time.sleep(1)
                

                return False
        else:
            if id in  self.user.get_user_data_login()["tv"]["tv_watch_list"]:
                self.user.get_user_data_login()["tv"]["tv_watch_list"].remove(id)
                self.user.save_data()
                return True
            else:
                print(Fore.RED,"Invaild id")
                print(Style.RESET_ALL,end="")
                time.sleep(1)


                return False
    def already_watched(self,category):
        '''"""
        print the list of already watched movies or TV shows with ratings and reviews.
        args:
            category(str):(movie or tvshow)

        return:
            None:if its found
            False:if its not found
    """'''
        try:
            if category=="tv":
                if self.user.get_user_data_login()["tv"]["rating"]:
                    print("your tvshow:")
                    print("-"*10)
                    for id in  self.user.get_user_data_login()["tv"]["rating"]:
                        for i in id:
                            tv_show=self.tvshow.get_basic_info_by_id(i)
                            print(f"{Fore.MAGENTA}id: {tv_show["id"]}\ntitle: {tv_show["title"]}\nrating: {id[i]["rating"]}\nreview:{id[i]["review"]}")
                            print("-"*10)
                else:
                    return False
            else:
                if self.user.get_user_data_login()["movie"]["rating"]:
                    print("your movie:")
                    print("-"*10)
                    for id in  self.user.get_user_data_login()["movie"]["rating"]:
                        for i in id:
                            movie=self.movie.get_basic_info_by_id(i)
                            print(f"{Fore.MAGENTA}id: {movie["id"]}\ntitle: {movie["title"]}\nrating: {id[i]["rating"]}\nreview:{id[i]["review"]}")
                            print("-"*10)
                else:
                    return False
        except Exception as e:
            print(f"{Fore.RED}{e}")
            print(f"{Fore.RED}{f"Error: {category} not found. The ID may be invalid."}{Style.RESET_ALL}")
            time.sleep(1)

        
    def share_tweet_on_x(self, id, category, rating, reviews):
        '''  
        Shares a review on X (Twitter) for a movie or TV show.


        args:
        - id(str):the id of the movie or tvshow
        - category (str): movie or tvshow.
        - rating (int): User rating (0-10).
        - reviews (str): User's review.
    '''
        try:
            if category=="movie":
                movie = self.movie.get_more_info_by_id(id)
                imdb_url = f"https://www.imdb.com/title/{movie['imdb_id']}/"
                post_content = (
                f"I just watched '{movie['title']}' {category}!\n"
                f"I gave it a {rating}/10\n"
                f"My Thoughts: {reviews}\n"
                f"More on IMDb: {imdb_url}\n")        
                encoded_content = urllib.parse.quote(post_content)
                x_url = f"https://x.com/intent/tweet?text={encoded_content}"
                webbrowser.open(x_url)
            else:
                category="Tv Show"
                tv_show = self.tvshow.get_more_info_by_id(id)
                imdb_url = f"https://www.imdb.com/title/{tv_show['imdb_id']}/"
                post_content = (
                f"I just watched {tv_show['title']} {category}!\n"
                f"I gave it a {rating}/10\n"
                f"My review: {reviews}\n"
                f"More on IMDb: {imdb_url}\n")        
                encoded_content = urllib.parse.quote(post_content)
                x_url = f"https://x.com/intent/tweet?text={encoded_content}"
                webbrowser.open(x_url)
        except Exception as e:
            print(f"{Fore.RED}{e}")
            print(f"{Fore.RED}{f"Error: {category} not found. The ID may be invalid."}{Style.RESET_ALL}")
            time.sleep(1)

    def delate_from_already_watched(self,id,category):
        '''  
        Removes a movie or tvshow from the already watched list.


        args:
        - id(str):the id of the movie or tvshow
        - category (str): movie or tvshow.
        -
    '''
        if category=="movie":
            for data in self.user.get_user_data_login()["movie"]["rating"]:
                if id in data:
                    del data[id]
                    self.user.get_user_data_login()["movie"]["rating"]=[data for data in  self.user.get_user_data_login()["movie"]["rating"] if data]
                    self.user.save_data()
                    break
            else:
                print(Fore.RED+f"No rating found for id:{id}"+Fore.RESET)
            
        else:
            for data in self.user.get_user_data_login()["tv"]["rating"]:
                if id in data:
                    del data[id]
                    self.user.get_user_data_login()["tv"]["rating"]=[data for data in  self.user.get_user_data_login()["tv"]["rating"] if data]
                    self.user.save_data()
                    break
            else:
                print(Fore.RED+f"No rating found for id:{id}"+Fore.RESET)
    def get_movie_by_genre(self,category):
        '''Shows movies or TV shows by genre.

            args:
            - category (str): movie or tv.'''
        try:
            if category=="movie":
                self.movie.print_genre()
                id=input(f"{Fore.CYAN}enter the id or press enter to continue:{Fore.YELLOW}")
                if not id=="":
                    movies=self.movie.get_movie_by_genre(id)
                    print()
                    for i,movie in enumerate(movies):
                        print(f"{Fore.MAGENTA}{i+1}.id:{movie["id"]} title:{movie["title"]} release_date:{movie["release_date"]}")
                        print("-"*80)
                else:
                    return False
            else:
                self.tvshow.print_genre()
                id=input(f"{Fore.CYAN}enter the id or press enter to continue:{Fore.YELLOW}")
                if not id=="":
                    tv_shows=self.tvshow.get_tv_by_genre(id)
                    print()

                    for i,tvshow in enumerate(tv_shows):
                        print(f"{Fore.MAGENTA}{i+1}.id:{tvshow["id"]} title:{tvshow["title"]} release_date:{tvshow["release_date"]}")
                        print("-"*80)
                else:
                    return False
        except Exception as e:
            print(f"{Fore.RED}{e}")
            print(f"{Fore.RED}{f"Error: {category} not found. The ID may be invalid."}{Style.RESET_ALL}")
            time.sleep(1)
    def ai_recomdation(self,category):
        '''
        gives ai recommendations based on the user mood.

        args:
            category (str): movie or tv'''
        mood=input(f"{Fore.CYAN}Describe what you're in the mood to watch:{Fore.YELLOW} ")
        print(f"{Fore.MAGENTA}-"*20)
        if category=="movie":
            print(f"{Fore.MAGENTA}{self.ai.recomdation_movie(mood)}")
            print("-"*20)

        else:
            print(f"{Fore.MAGENTA}{self.ai.recomdation_tvshow(mood)}")
            print("-"*20)



