import joblib as jb
import pandas as pd
from PyMovieDb import IMDB
import difflib 
import json 
class Containeer:
  def __init__(self , movie , poster , type1):
      self.movie =  movie
      self.poster  =  poster  
      self.type1   =   type1
    
def pumk( movie_name ):
        movies_data = pd.read_csv("/home/jayanth119/Documents/projects/HTML ,CSS AND JAVASCRIPT/html/main/static/images/data.csv")
        similarity = jb.load('/home/jayanth119/Documents/projects/HTML ,CSS AND JAVASCRIPT/html/main/static/images/result.joblib') 
        list_of_all_titles = movies_data['source'].tolist()
        find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
        close_match = find_close_match[0]
        index_of_the_movie = movies_data[movies_data.source == close_match]['index'].values[0]
        similarity_score = list(enumerate(similarity[index_of_the_movie]))
        sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)
        print('Movies suggested for you : \n')
        i = 1
        recom  = []
        for movie in sorted_similar_movies:
            index = movie[0]
            title_from_index = movies_data[movies_data.index==index]['source'].values[0]
            if(i+1 == 10):
                break 
            if (i< 10):
                print(i, '.',title_from_index)
                recom.append(title_from_index)
                i+=1
        lom1 = recom
        mov = IMDB()
        poster = []
        type1 = []
        for  i in lom1:
            x = mov.get_by_name( i , tv=True)
            moviej =  json.loads(x)
            try:
                c = moviej["type"]
                d = moviej["poster"]
                poster.append(d)
                type1.append(c)
            except:
                continue
        obj = []
        for i in range(len(poster)):
            x = Containeer(recom[i] , poster[i] , type1[i])
            obj.append(x)
        print(poster)
        print(type1)
        movies = {"list" : obj} 
        return movies
