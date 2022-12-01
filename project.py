import pymysql

def mysqlconnect():
    connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='Gjdbswn1319!', # change this to a real password when testing
                             database='MovieDB',
                             charset='utf8mb4',
                             autocommit=True,
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

def addNewMovie(movie_id, title, year, revenue, runtime, country, language):
	cur = mysqlconnect().cursor()
	sql = "insert into Movie (movie_id, title, release_year, revenue, runtime) values(%s, %s, %s, %s, %s)"
	cur.execute(sql, (movie_id, title, year, revenue, runtime))

	sql = 'insert into ProductionCountry (movie_id, country) values(%s, %s)'
	cur.execute(sql, (movie_id, country))

	sql = 'insert into OriginalLanguage (movie_id, language) values(%s, %s)'
	cur.execute(sql, (movie_id, language))

	#''' test
	cur.execute('select * from Movie')
	output = cur.fetchall()
	for o in output:
		print(o)
	

	cur.execute('select * from OriginalLanguage')
	output = cur.fetchall()
	for o in output:
		print(o)

	cur.execute('select * from ProductionCountry')
	output = cur.fetchall()
	for o in output:
		print(o)

	#'''

def addNewDirector(director_id, director_name, director_birth_date, director_gender):
	cur = mysqlconnect().cursor()
	sql = "insert into Director (director_id, director_name, director_birth_date, director_gender) values(%s, %s, %s, %s)"
	cur.execute(sql, (director_id, director_name, director_birth_date, director_gender))

	#''' test
	cur.execute('select * from Director')
	output = cur.fetchall()
	for o in output:
		print(o)
	#'''

def addNewCast(actor_id, actor_name, actor_birth_date, actor_gender):
	cur = mysqlconnect().cursor()
	sql = "insert into Actor (actor_id, actor_name, birth_date, gender) values(%s, %s, %s, %s)"
	cur.execute(sql, (actor_id, actor_name, actor_birth_date, actor_gender))

	#''' test
	cur.execute('select * from Actor')
	output = cur.fetchall()
	for o in output:
		print(o)
	#'''

def updateTitle(original_title, new_title):
	cur = mysqlconnect().cursor()
	sql = 'update Movie set title = %s where title = %s'
	cur.execute(sql, (new_title, original_title))

	#''' test
	cur.execute('select * from Movie')
	output = cur.fetchall()
	for o in output:
		print(o)
	#'''

def deleteTitle(movie_title):
	cur = mysqlconnect().cursor()
	sql = 'select movie_id from Movie where title=%s'
	cur.execute(sql, (movie_title))
	movieId = cur.fetchone()['movie_id']

	sql = 'delete from OriginalLanguage where movie_id = %s'
	cur.execute(sql, (movieId))

	sql = 'delete from ProductionCountry where movie_id = %s'
	cur.execute(sql, (movieId))

	sql = 'delete from Movie where title = %s'
	cur.execute(sql, (movie_title))

	#cur.execute('SET FOREIGN_KEY_CHECKS=OFF')
	
	#cur.execute('SET FOREIGN_KEY_CHECKS=ON')

	#''' test
	cur.execute('select * from Movie')
	output = cur.fetchall()
	for o in output:
		print(o)

	cur.execute('select * from OriginalLanguage')
	output = cur.fetchall()
	for o in output:
		print(o)

	cur.execute('select * from ProductionCountry')
	output = cur.fetchall()
	for o in output:
		print(o)

	#'''

def highestRevenue():
	cur = mysqlconnect().cursor()
	cur.execute('select title, revenue from Movie where revenue = (select max(revenue) from Movie)')
	output = cur.fetchone()
	return output

def lowestRevenue():
	cur = mysqlconnect().cursor()
	cur.execute('select title, revenue from Movie where revenue = (select min(revenue) from Movie)')
	output = cur.fetchone()
	return output

def avgRuntime():
	cur = mysqlconnect().cursor()
	cur.execute('select avg(runtime) from Movie')
	output = cur.fetchone()
	return output

def totalRevenue(actor):
	cur = mysqlconnect().cursor()
	sql = ('select sum(revenue) from Movie where movie_id in (select movie_id from MovieCast where cast_id in (select actor_id from Actor where actor_name = %s))')
	cur.execute(sql, (actor))
	output = cur.fetchone()
	return output

def actorrevenuegr(revenue):
	cur = mysqlconnect().cursor()
	sql = ('select actor_name from Actor where actor_id in (select cast_id from MovieCast where movie_id in (select movie_id from Movie where revenue > %s))')
	cur.execute(sql, (revenue))
	output = cur.fetchall()
	return output

def directorrevenuelr(revenue):
	cur = mysqlconnect().cursor()
	sql = ('select director_name from Director where director_id in (select director_id from MovieDirector where movie_id in (select movie_id from Movie where revenue < %s))')
	cur.execute(sql, (revenue))
	output = cur.fetchall()
	return output