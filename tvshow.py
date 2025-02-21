import requests
class Tvshow:
    def __init__(self,api_key):
        self.api_key = api_key
        self.base_url = 'https://api.themoviedb.org/3/'
    def search_query(self,query):
        response=requests.get(f"{self.base_url}search/tv?query={query}&api_key={self.api_key}").json()
        tvshows=[]
        for tv_show in response["results"]:
            tv_show_info={
                "id":tv_show["id"],
                "title":tv_show["name"],
                "release_date":tv_show["first_air_date"]
            }
            tvshows.append(tv_show_info)
        return tvshows
        
    def get_more_info_by_id(self,id):
        response=requests.get(f"{self.base_url}tv/{id}?&api_key={self.api_key}")
        response.raise_for_status()
        response=response.json()
        imdb=requests.get(f"{self.base_url}tv/{id}/external_ids?&api_key={self.api_key}")
        imdb.raise_for_status()
        imdb=imdb.json()
        tv_show_info = {
            "id":response["id"],
            "title": response["name"],
            "release_date": response["first_air_date"],
            "genres": [gen["name"] for gen in response["genres"]],
            "overview": response["overview"],
            "number_of_seasons":response["number_of_seasons"],
            "TMDb_Rating": response["vote_average"],
            "imdb_id":imdb["imdb_id"]
        }  
        return tv_show_info
    def get_popular_tv(self):
        response=requests.get(f"{self.base_url}tv/popular?&api_key={self.api_key}").json()
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
       
    def get_top_rated_tv(self):
        response=requests.get(f"{self.base_url}tv/top_rated?&api_key={self.api_key}").json()
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
        response=requests.get(f"{self.base_url}tv/{id}?&api_key={self.api_key}")
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
        
