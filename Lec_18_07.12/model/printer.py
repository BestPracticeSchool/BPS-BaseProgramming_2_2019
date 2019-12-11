from actor import Actor
from base import Session
from movie import Movie 


session = Session()

movies = session.query(Movie).all()

print("ALL MOVIES")
for movie in movies:
    print("{} released {} ".format(movie.title, movie.release_date))