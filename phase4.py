import pymysql
from tmdbv3api import TMDb
from tmdbv3api import Movie
from tmdbv3api import Company

tmdb = TMDb()
tmdb.api_key = 'a72cc639524e6f4365d12e73e7a15ade'

# Connect to the database
def mysqlconnect():
    connection = pymysql.connect(host='localhost',
                                user = 'root',
                                password='j1025178',
                                database='movie',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    return connection


def getProductionCompanyList():
    company = Company()
    companies = []
    for i in range(1, 1000):
        companies.append(company.details(i))
        print(company.details(i))
    return companies

def getMovieList():
    movie = Movie()
    movies = []
    print("i am here")
    for i in range(1, 1000):
        movieID = movie.movie_id(i)
        movies.append(movie.details(movieID))
        print(movie.details(movieID))
    return movies


# def main():
#     with mysqlconnect().cursor() as cursor:
#         # Read a single record

#         print("hello")
#         sql = "SELECT ``, `password` FROM `users` WHERE `email`=%s"
#         cursor.execute(sql, ('webmaster@python.org',))
#         result = cursor.fetchone()
#         print(result)
    

# Driver Code
if __name__ == "__main__" :
    mysqlconnect()
    #getProductionCompanyList()
    getMovieList()
