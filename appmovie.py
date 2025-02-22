import requests
import json
from movie import Movie
from tvshow import Tvshow
from user import User
from ai import Ai
import urllib.parse
import webbrowser
from colorama import Fore, Back, Style
from dotenv import load_dotenv
import os
class AppMovie:    
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
    def search_by_qurey(self,query,type):
        try:
            if type=="movie":
                movies=self.movie.search_query(query)
                print("="*50)
                for i,movie in enumerate(movies):
                    print(f"{i+1}.id:{movie["id"]} title:{movie["title"]} release_date:{movie["release_date"]}")
                    print("-"*80)
            else:
                tv_shows=self.tvshow.search_query(query)
                print("="*50)


                for i,tvshow in enumerate(tv_shows):
                    print(f"{i+1}.id:{tvshow["id"]} title:{tvshow["title"]} release_date:{tvshow["release_date"]}")
                    print("-"*80)
        except Exception as e:
            print(e)
    
    def get_more_info(self,id,type):
        try:
            if type=="movie":
                movies=self.movie.get_more_info_by_id(id)
                url=f"https://www.imdb.com/title/{movies["imdb_id"]}"
                print(f"id: {movies["id"]}\nTitle: {movies["title"]}\nRelease Date: {movies["release_date"]}\nGenres: {" ".join([gen for gen in movies["genres"]])}\nOverview: {movies["overview"]}\nTMDb Rating: {movies["TMDb_Rating"]}")
                print("for more info:",end="")
                print(Fore.BLUE,url)    
                print(Style.RESET_ALL,end="")
                print("="*50)

            
            else:
                tv_show=self.tvshow.get_more_info_by_id(id)
                url=f"https://www.imdb.com/title/{tv_show["imdb_id"]}"
                print(f"id: {tv_show["id"]}\nTitle: {tv_show["title"]}\nRelease Date: {tv_show["release_date"]}\nGenres: {" ".join([gen for gen in tv_show["genres"]])}\nnumber of seasons: {tv_show["number_of_seasons"]}\nOverview: {tv_show["overview"]}\nTMDb Rating: {tv_show["TMDb_Rating"]}")
                print("for more info:",end="")
                print(Fore.BLUE,url) 
                print(Style.RESET_ALL,end="")
                print("="*50)


        except Exception as e:
            print(e)
            return False
    def get_popular(self,type):
        try:
            if type=="movie":
                movies=self.movie.get_popular_movie()
                for movie in movies:
                    print(f"id: {movie["id"]}\ntitle: {movie["title"]}\nRelease Date: {movie["release_date"]}\nTMDb Rating: {movie["TMDb_Rating"]}\nvote count: {movie["TMDb_vote_count"]}")
                    print("-"*20)
            else:
                tv_shows=self.tvshow.get_popular_tv()  
                for tvshow in tv_shows:
                    print(f"id: {tvshow["id"]}\ntitle: {tvshow["title"]}\nRelease Date: {tvshow["release_date"]}\nTMDb Rating: {tvshow["TMDb_Rating"]}\nvote count: {tvshow["TMDb_vote_count"]}")
                    print("-"*20)      
        except Exception as e:
            print(e)
    def get_top_rated(self,type):
        try:
            if type=="movie":
                movies=self.movie.get_top_rated_movie()
                for movie in movies:
                    print(f"id: {movie["id"]}\nTitle: {movie["title"]}\nRelease Date: {movie["release_date"]}\nTMDb Rating: {movie["TMDb_Rating"]}\nvote count: {movie["TMDb_vote_count"]}")
                    print("-"*20)
            else:
                tv_shows=self.tvshow.get_top_rated_tv()
                for tvshow in tv_shows:
                    print(f"id: {tvshow["id"]}\ntitle: {tvshow["title"]}\nRelease Date: {tvshow["release_date"]}\nTMDb Rating: {tvshow["TMDb_Rating"]}\nvote count: {tvshow["TMDb_vote_count"]}")
                    print("-"*20)   
        except Exception as e:
            print(e)
    def get_basic_info_by_id(self,id,type):
        try:
            if type=="movie":
                movies=self.movie.get_basic_info_by_id(id)
                print(f"id: {movies["id"]}\nTitle: {movies["title"]}\nRelease Date: {movies["release_date"]}\nGenres: {" ".join([gen for gen in movies["genres"]])}\nduration: {movies["duration"]}")
            else:
                tv_shows=self.tvshow.get_basic_info_by_id(id)
                print(f"id: {tv_shows["id"]}\nTitle: {tv_shows["title"]}\nRelease Date: {tv_shows["release_date"]}\nGenres: {" ".join([gen for gen in tv_shows["genres"]])}\nnumber of seasons: {tv_shows["number_of_seasons"]}")
        except Exception as e:
            print(e)    
    def add_watchlist(self,id,type):
        if type=="movie":
            if id not in   self.user.get_user_data_login()["movie"]["movie_watch_list"]:
                self.user.get_user_data_login()["movie"]["movie_watch_list"].append(id)
                self.user.save_data()
                print("The movie is added to the watchlist.")
            else:
                print("The movie is already added to the watchlist.")
        else:
            if id not in self.user.get_user_data_login()["tv"]["tv_watch_list"]:
                self.user.get_user_data_login()["tv"]["tv_watch_list"].append(id)
                self.user.save_data()
                print("The tv show is added to the watchlist.")
            else:
                print("The tv show is already added to the watchlist.")
    def add_rating_and_reviews(self,id,type,rating,reviews):
        already_rated=False
        if type=="movie":
            if id in  self.user.get_user_data_login()["movie"]["movie_watch_list"]:
                self.delate_from_watch_list(id,"movie")
            
            for movie_id in self.user.get_user_data_login()["movie"]["rating"]:
                if id in movie_id:
                    already_rated=True
            if already_rated==False:
                self.user.get_user_data_login()["movie"]["rating"].append({id:{"review":reviews,"rating":rating}})
                self.user.save_data()
            else:
                print("you already rating the movie")
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
                print("you already rating the movie")

    def watch_list(self,type):
        try:
            if type=="tvshow":
                if  self.user.get_user_data_login()["tv"]["tv_watch_list"]:
                    print("your tvshow:")
                    print("-"*10)
                    for watchlist in  self.user.get_user_data_login()["tv"]["tv_watch_list"]:
                        self.get_basic_info_by_id(watchlist,"tv")
                        print("-"*10)
                else:
                    return False
                    
            else:
                if self.user.get_user_data_login()["movie"]["movie_watch_list"]:
                    print("your movie:")
                    print("-"*10)
                    for watchlist in  self.user.get_user_data_login()["movie"]["movie_watch_list"]:
                        self.get_basic_info_by_id(watchlist,"movie")
                        print("-"*10)
                else:
                    return False
        except Exception as e:
            print(e)
    def delate_from_watch_list(self,id,type):
        if type=="movie":
            if id in  self.user.get_user_data_login()["movie"]["movie_watch_list"]:
                self.user.get_user_data_login()["movie"]["movie_watch_list"].remove(id)
                self.user.save_data()
                print("The movie has been removed from your watch list.")
                return True
            else:
                print("Invaild id")
                return False
        else:
            if id in  self.user.get_user_data_login()["tv"]["tv_watch_list"]:
                self.user.get_user_data_login()["tv"]["tv_watch_list"].remove(id)
                self.user.save_data()
                print("The tvshow has been removed from your watch list.")
                return True
            else:
                print("Invaild id")
                return False
    def already_watched(self,type):
        try:
            if type=="tv":
                if self.user.get_user_data_login()["tv"]["rating"]:
                    print("your tvshow:")
                    print("-"*10)
                    for id in  self.user.get_user_data_login()["tv"]["rating"]:
                        for i in id:
                            tv_show=self.tvshow.get_basic_info_by_id(i)
                            print(f"id: {tv_show["id"]}\ntitle: {tv_show["title"]}\nrating: {id[i]["rating"]}\nreview:{id[i]["review"]}")
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
                            print(f"id: {movie["id"]}\ntitle: {movie["title"]}\nrating: {id[i]["rating"]}\nreview:{id[i]["review"]}")
                            print("-"*10)
                else:
                    return False
        except Exception as e:
            print(e)
        
    def share_tweet_on_x(self, id, type, rating, reviews):
        try:
            if type=="movie":
                movie = self.movie.get_more_info_by_id(id)
                imdb_url = f"https://www.imdb.com/title/{movie['imdb_id']}/"
                post_content = (
                f"I just watched '{movie['title']}' {type}!\n"
                f"I gave it a {rating}/10\n"
                f"My Thoughts: {reviews}\n"
                f"More on IMDb: {imdb_url}\n")        
                encoded_content = urllib.parse.quote(post_content)
                x_url = f"https://x.com/intent/tweet?text={encoded_content}"
                webbrowser.open(x_url)
            else:
                type="TvShow"
                tv_show = self.tvshow.get_more_info_by_id(id)
                imdb_url = f"https://www.imdb.com/title/{tv_show['imdb_id']}/"
                post_content = (
                f"I just watched {tv_show['title']} {type}!\n"
                f"I gave it a {rating}/10\n"
                f"My review: {reviews}\n"
                f"More on IMDb: {imdb_url}\n")        
                encoded_content = urllib.parse.quote(post_content)
                x_url = f"https://x.com/intent/tweet?text={encoded_content}"
                webbrowser.open(x_url)
        except Exception as e:
            print(e)
    def delate_from_already_watched(self,id,type):
        if type=="movie":
            for data in self.user.get_user_data_login()["movie"]["rating"]:
                if id in data:
                    del data[id]
                    self.user.get_user_data_login()["movie"]["rating"]=[data for data in  self.user.get_user_data_login()["movie"]["rating"] if data]
                    self.user.save_data()
                    break
            else:
                print(f"No rating found for id:{id}")
            
        else:
            for data in self.user.get_user_data_login()["tv"]["rating"]:
                if id in data:
                    del data[id]
                    self.user.get_user_data_login()["tv"]["rating"]=[data for data in  self.user.get_user_data_login()["tv"]["rating"] if data]
                    self.user.save_data()
                    break
            else:
                print(f"No rating found for id:{id}")
    def get_movie_by_genre(self,type):
        try:
            if type=="movie":
                self.movie.print_genre()
                id=input("enter the id:")
                movies=self.movie.get_movie_by_genre(id)
                print()
                for i,movie in enumerate(movies):
                    print(f"{i+1}.id:{movie["id"]} title:{movie["title"]} release_date:{movie["release_date"]}")
                    print("-"*80)
            else:
                self.tvshow.print_genre()
                id=input("enter the id:")
                tv_shows=self.tvshow.get_tv_by_genre(id)
                print()

                for i,tvshow in enumerate(tv_shows):
                    print(f"{i+1}.id:{tvshow["id"]} title:{tvshow["title"]} release_date:{tvshow["release_date"]}")
                    print("-"*80)
        except Exception as e:
            print(e)
    def ai_recomdation(self,type):
        mood=input("Describe what you're in the mood to watch: ")
        print("-"*20)
        if type=="movie":
            print(self.ai.recomdation_movie(mood))
            print("-"*20)

        else:
            print(self.ai.recomdation_tvshow(mood))
            print("-"*20)



