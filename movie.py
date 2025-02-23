import requests
from colorama import Fore, Style

class Movie:
    def __init__(self,api_key):
        self.__api_key = api_key
        self.__base_url = 'https://api.themoviedb.org/3/'
    def search_query(self,query:str)->list:
        '''search for movie by a query and return a list of matching result
           args:
               query(str):the search key word for movie
           return:
                list:a list of dictionires contin basic info id,title ,release date    
           raise:
                raise Exception if the request fails'''
        response=requests.get(f"{self.__base_url}search/movie?query={query}&api_key={self.__api_key}")
        response.raise_for_status()
        response=response.json()
        movies=[]
        for movie in response["results"]:
            movie_info={
                "id":movie["id"],
                "title":movie["title"],
                "release_date":movie["release_date"]
            }
            movies.append(movie_info)
        return movies
    def get_more_info_by_id(self, id):
        '''get more detailed about a movie by its id
           args:
               id(str):the id of the movie 
           return:
               list:list of dictiniory contining datiled id,title,release date,geners,overview,number of seasons,tmdb rating ,imdb id
            raise:
                raise Exception if the request fails'''
        movie = requests.get(f"{self.__base_url}movie/{id}?&api_key={self.__api_key}")
        movie.raise_for_status()
        movie = movie.json()        
        movie_info = {
            "id":movie["id"],
            "title": movie["title"],
            "release_date": movie["release_date"],
            "genres": [gen["name"] for gen in movie["genres"]],
            "duration": movie["runtime"],
            "overview": movie["overview"],
            "TMDb_Rating": movie["vote_average"],
            "poster":movie["poster_path"],
            "imdb_id":movie["imdb_id"]
        }
        
        return movie_info

    def get_popular_movie(self):
        ''' this function get a list of popular movie
        return:
            list:a list of dictionires contin basic info id,title ,release date    
        reaise:
            raise Exception if the request fails'''
        response=requests.get(f"{self.__base_url}movie/popular?&api_key={self.__api_key}")
        response.raise_for_status()
        response=response.json()
        movies=[]
        for movie in response["results"]:
            movie_info={
                "id":movie["id"],
                "title":movie["title"],
                "release_date":movie["release_date"],
                "TMDb_Rating":movie['vote_average'],
                "TMDb_vote_count":movie['vote_count']
            }
            movies.append(movie_info)
        return movies
    def get_top_rated_movie(self):
        '''this function get a list of top rated movie
        return:
            list:a list of dictionires contin basic info id,title ,release date    
        reaise:
            raise Exception if the request fails'''
        
        response=requests.get(f"{self.__base_url}movie/top_rated?&api_key={self.__api_key}")
        response.raise_for_status()
        response=response.json()
        movies=[]
        for movie in response["results"]:
            movie_info={
                "id":movie["id"],
                "title":movie["title"],
                "release_date":movie["release_date"],
                "TMDb_Rating":movie['vote_average'],
                "TMDb_vote_count":movie['vote_count']

            }
            movies.append(movie_info)
        return movies
       
    def get_basic_info_by_id(self,id):
        ''' get detailed about a movie by its id
           args:
               id(str):the id of the movie
           return:
               list:list of dictiniory contining datiled id,title,release date,geners,overview,number of seasons,tmdb rating ,imdb id
            raise:
                raise Exception if the request fails'''
        movie=requests.get(f"{self.__base_url}movie/{id}?&api_key={self.__api_key}")
        movie.raise_for_status()
        movie=movie.json()
        movie_info = {
            "id":movie["id"],
            "title": movie["title"],
            "release_date": movie["release_date"],
            "genres": [gen["name"] for gen in movie["genres"]],
            "duration": movie["runtime"],
        }
        
        return movie_info
        
    def print_genre(self):
        '''  Prints all movie genres available on TMDb.
        reaise:
            raise Exception if the request fails'''
        genre=requests.get(f"{self.__base_url}genre/movie/list?&api_key={self.__api_key}")
        genre.raise_for_status()
        genre=genre.json()
        for i,gen in enumerate(genre["genres"]):
            print(f"{Fore.MAGENTA}{i+1}.id:{gen["id"]} name:{gen["name"]}")
            print("-"*50)

    def get_movie_by_genre(self,id):
        '''
        this function get a list of movie by specified genre id 
        return:
            list:a list of dictionires contin basic info id,title ,release date    
        reaise:
            raise Exception if the request fails'''
        response=requests.get(f"{self.__base_url}discover/movie?&api_key={self.__api_key}&sort_by=popularity.desc&with_genres={id}").json()
        movies=[]
        for movie in response["results"]:
            movie_info={
                "id":movie["id"],
                "title":movie["title"],
                "release_date":movie["release_date"]
            }
            movies.append(movie_info)
        return movies

