import requests
from colorama import Fore

class Tvshow:
    def __init__(self,api_key):
        self.__api_key = api_key
        self.__base_url = 'https://api.themoviedb.org/3/'
    def search_query(self,query:str)->list:
        '''search for tv shows by a query and return a list of matching result
           args:
               query(str):the search key word for tv show
           return:
                list:a list of dictionires contin basic info id,title ,release date    
           raise:
                raise Exception if the request fails
             '''
        response:object=requests.get(f"{self.__base_url}search/tv?query={query}&api_key={self.__api_key}")
        response.raise_for_status()
        response=response.json()
        tvshows:list=[]
        for tv_show in response["results"]:
            tv_show_info:dict={
                "id":tv_show["id"],
                "title":tv_show["name"],
                "release_date":tv_show["first_air_date"]
            }
            tvshows.append(tv_show_info)
        return tvshows
        
    def get_more_info_by_id(self,id:str)->dict:
        '''get more detailed about a tv show by its id
           args:
               id(str):the id of the tv show 
           return:
               list:list of dictiniory contining datiled id,title,release date,geners,overview,number of seasons,tmdb rating ,imdb id
            raise:
                raise Exception if the request fails

            '''
        response:object=requests.get(f"{self.__base_url}tv/{id}?&api_key={self.__api_key}")
        response.raise_for_status()
        response=response.json()
        imdb:object=requests.get(f"{self.__base_url}tv/{id}/external_ids?&api_key={self.__api_key}")
        imdb.raise_for_status()
        imdb=imdb.json()
        tv_show_info:dict = {
            "id":response["id"],
            "title": response["name"],
            "release_date": response["first_air_date"],
            "genres": [gen["name"] for gen in response["genres"]],
            "overview": response["overview"],
            "number_of_seasons":response["number_of_seasons"],
            "number_of_episodes":response["number_of_episodes"],

            "TMDb_Rating": response["vote_average"],
            "imdb_id":imdb["imdb_id"]
        }  
        return tv_show_info
    def get_popular_tv(self)->object:
        '''
        this function get a list of popular tv show
        return:
            list:a list of dictionires contin basic info id,title ,release date    
        reaise:
            raise Exception if the request fails
  '''

        response:object=requests.get(f"{self.__base_url}tv/popular?&api_key={self.__api_key}")
        response.raise_for_status()
        response=response.json()
        tvshows:list=[]
        for movie in response["results"]:
            movie_info:dict={
                "id":movie["id"],
                "title":movie["name"],
                "release_date":movie["first_air_date"],
                "TMDb_Rating":movie['vote_average'],
                "TMDb_vote_count":movie['vote_count']
            }
            tvshows.append(movie_info)
        return tvshows
       
    def get_top_rated_tv(self):
        '''
        this function get a list of top rated tv show
        return:
            list:a list of dictionires contin basic info id,title ,release date    
        reaise:
            raise Exception if the request fails'''
        response=requests.get(f"{self.__base_url}tv/top_rated?&api_key={self.__api_key}")
        response.raise_for_status()
        response=response.json()
        tvshows=[]
        for movie in response["results"]:
            movie_info={
                "id":movie["id"],
                "title":movie["name"],
                "release_date":movie["first_air_date"],
                "TMDb_Rating":movie['vote_average'],
                "TMDb_vote_count":movie['vote_count']
            }
            tvshows.append(movie_info)
        return tvshows
    def get_basic_info_by_id(self,id):
        '''
        get detailed about a tv show by its id
           args:
               id(str):the id of the tv show 
           return:
               list:list of dictiniory contining datiled id,title,release date,geners,overview,number of seasons,tmdb rating ,imdb id
            raise:
                raise Exception if the request fails
        '''
        response=requests.get(f"{self.__base_url}tv/{id}?&api_key={self.__api_key}")
        response.raise_for_status()
        response=response.json()
       
        tv_show_info = {
            "id":response["id"],
            "title": response["name"],
            "release_date": response["first_air_date"],
            "genres": [gen["name"] for gen in response["genres"]],
            "number_of_seasons": response["number_of_seasons"],
        }
        
        return tv_show_info
    def print_genre(self):
        '''
        Prints all TV show genres available on TMDb.
        reaise:
            raise Exception if the request fails
        '''
        genre=requests.get(f"{self.__base_url}genre/tv/list?&api_key={self.__api_key}")
        genre.raise_for_status()
        genre=genre.json()
        for i,gen in enumerate(genre["genres"]):
            print(f"{Fore.MAGENTA}{i+1}.id:{gen["id"]} name:{gen["name"]}")
            print("-"*50)

    def get_tv_by_genre(self,id):
        '''
        this function get a list of tv show by specified genre id 
        return:
            list:a list of dictionires contin basic info id,title ,release date    
        reaise:
            raise Exception if the request fails'''
        response=requests.get(f"{self.__base_url}discover/tv?&api_key={self.__api_key}&sort_by=popularity.desc&with_genres={id}").json()
        tvshows=[]
        for tvshow in response["results"]:
            tvshow_info={
                "id":tvshow["id"],
                "title":tvshow["name"],
                "release_date":tvshow["first_air_date"]
            }
            tvshows.append(tvshow_info)
        return tvshows


