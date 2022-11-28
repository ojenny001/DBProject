import pymysql

def mysqlconnect():
    connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='temporary_password', # change this to a real password when testing
                             database='MovieDB',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

    return connection

def titleToDirector(movieTitle):
	cur = mysqlconnect().cursor()
	sql = "select director_id, director_name from Director where director_id in (select director_id from MovieDirector where movie_id in (select movie_id from Movie where title = %s))"
	cur.execute(sql, (movieTitle))
	output = cur.fetchall()
	return output

def titleToCast(movieTitle):
	cur = mysqlconnect().cursor()
	sql = "select actor_id, actor_name from Actor where actor_id in (select cast_id from MovieCast where movie_id in (select movie_id from Movie where title = %s))"
	cur.execute(sql, (movieTitle))
	output = cur.fetchall()
	return output

def titleToGenre(movieTitle):
	cur = mysqlconnect().cursor()
	sql = "select genre from GenreType where genre in (select genre from MovieGenre where movie_id in (select movie_id from Movie where title = %s))"
	cur.execute(sql, (movieTitle))
	output = cur.fetchall()
	return output

def titleToLanguage(movieTitle):
	cur = mysqlconnect().cursor()
	sql = "select language from OriginalLanguage where movie_id in (select movie_id from Movie where title = %s)"
	cur.execute(sql, (movieTitle))
	output = cur.fetchall()
	return output

def titleToCountry(movieTitle):
	cur = mysqlconnect().cursor()
	sql = "select country from ProductionCountry where movie_id in (select movie_id from Movie where title = %s)"
	cur.execute(sql, (movieTitle))
	output = cur.fetchall()
	return output

def titleToYear(movieTitle):
	cur = mysqlconnect().cursor()
	sql = "select release_year from Movie where title = %s"
	cur.execute(sql, (movieTitle))
	output = cur.fetchall()
	return output

def directorToMovie(directorName):
	cur = mysqlconnect().cursor()
	sql = "select title from Movie where movie_id in (select movie_id from MovieDirector where director_id in (select director_id from Director where director_name = %s))"
	cur.execute(sql, (directorName))
	output = cur.fetchall()
	return output

def directorToBirthdate(directorName):
	cur = mysqlconnect().cursor()
	sql = "select director_name, director_birth_date from Director where director_name = %s"
	cur.execute(sql, (directorName))
	output = cur.fetchall()
	return output

def directorToGender(directorName):
	cur = mysqlconnect().cursor()
	sql = "select director_name, director_gender from Director where director_name = %s"
	cur.execute(sql, (directorName))
	output = cur.fetchall()
	return output

def actorToMovie(actorName):
	cur = mysqlconnect().cursor()
	sql = "select title from Movie where movie_id in (select movie_id from MovieCast where cast_id in (select actor_id from Actor where actor_name = %s))"
	cur.execute(sql, (actorName))
	output = cur.fetchall()
	return output

def actorToBirthdate(actorName):
	cur = mysqlconnect().cursor()
	sql = "select actor_name, birth_date from Actor where actor_name = %s"
	cur.execute(sql, (actorName))
	output = cur.fetchall()
	return output

def actorToNationality(actorName):
	cur = mysqlconnect().cursor()
	sql = "select nationality from ActorNationality where actor_id in (select actor_id from Actor where actor_name = %s)"
	cur.execute(sql, (actorName))
	output = cur.fetchall()
	return output

def actorToGender(actorName):
	cur = mysqlconnect().cursor()
	sql = "select actor_name, gender from Actor where actor_name = %s"
	cur.execute(sql, (actorName))
	output = cur.fetchall()
	return output

def genreToMovie(genreType):
	cur = mysqlconnect().cursor()
	sql = "select title from Movie where movie_id in (select movie_id from MovieGenre where genre = %s)"
	cur.execute(sql, (genreType))
	output = cur.fetchall()
	return output

def countryToMovie(country):
	cur = mysqlconnect().cursor()
	sql = "select title from Movie where movie_id in (select movie_id from ProductionCountry where country = %s)"
	cur.execute(sql, (country))
	output = cur.fetchall()
	return output

#if __name__ == "__main__" :
	#titleToDirector('The Dark Knight')
	#titleToCast('The Dark Knight')
	#titleToGenre('The Dark Knight')
	#titleToLanguage('The Dark Knight')
	#titleToCountry('The Dark Knight')
	#titleToYear('The Dark Knight')
	#directorToMovie('Christopher Nolan')
	#directorToBirthdate('Christopher Nolan')
	#directorToGender('Christopher Nolan')
	#actorToMovie('Brad Pitt')
	#actorToBirthdate('Brad Pitt')
	#actorToNationality('Brad Pitt')
	#actorToGender('Brad Pitt')
	#genreToMovie('comedy')
	#countryToMovie('Germany')