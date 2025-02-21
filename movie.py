import requests
class Movie:
    def __init__(self,api_key):
        self.api_key = api_key
        self.base_url = 'https://api.themoviedb.org/3/'
    def search_query(self,query):
        response=requests.get(f"{self.base_url}search/movie?query={query}&api_key={self.api_key}").json()
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
        movie = requests.get(f"{self.base_url}movie/{id}?&api_key={self.api_key}")
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
        response=requests.get(f"{self.base_url}movie/popular?&api_key={self.api_key}").json()
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
        response=requests.get(f"{self.base_url}movie/top_rated?&api_key={self.api_key}").json()
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
        movie=requests.get(f"{self.base_url}movie/{id}?&api_key={self.api_key}")
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
        
       