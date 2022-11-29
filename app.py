from flask import Flask, render_template, url_for, request, Response, redirect
import pymysql.cursors
from project import *

app = Flask(__name__)

@app.route('/')

@app.route('/home')
def home():
	return render_template('index.html')

@app.route('/movieinfo', methods=['POST', 'GET'])
def movieinfo():
	movieTitle = request.form.to_dict()['movie_title']
	director = titleToDirector(movieTitle)
	cast = titleToCast(movieTitle)
	genre = titleToGenre(movieTitle)
	language = titleToLanguage(movieTitle)
	country = titleToCountry(movieTitle)
	year = titleToYear(movieTitle)
	
	return render_template('movieinfo.html', director=director, cast=cast, genre=genre, language=language, country=country, year=year)

@app.route('/directorinfo', methods=['POST', 'GET'])
def directorinfo():
	director = request.form.to_dict()['movie_director']
	movie = directorToMovie(director)
	birthdate = directorToBirthdate(director)
	gender = directorToGender(director)

	return render_template('directorinfo.html', director=director, movie=movie, birthdate=birthdate, gender=gender)

@app.route('/castinfo', methods=['POST', 'GET'])
def castinfo():
	cast = request.form.to_dict()['movie_cast']
	movie = actorToMovie(cast)
	birthdate = actorToBirthdate(cast)
	nationality = actorToNationality(cast)
	gender = actorToGender(cast)

	return render_template('castinfo.html', cast=cast, movie=movie, birthdate=birthdate, nationality=nationality, gender=gender)

@app.route('/genreinfo', methods=['POST', 'GET'])
def genreinfo():
	genre = request.form.to_dict()['movie_genre']
	movie = genreToMovie(genre)

	return render_template('genreinfo.html', genre=genre, movie=movie)

@app.route('/countryinfo', methods=['POST', 'GET'])
def countryinfo():
	country = request.form.to_dict()['movie_country']
	movie = countryToMovie(country)

	return render_template('countryinfo.html', country=country, movie=movie)

@app.route('/addMovie', methods=['POST', 'GET'])
def addMovie():
	data = request.form.to_dict()
	movie_id = data['add_id']
	title = data['add_title']
	year = data['add_year']
	addNewMovie(movie_id, title, year)

	return render_template('addedmovie.html')

@app.route('/addDirector', methods=['POST', 'GET'])
def addDirector():
	data = request.form.to_dict()
	director_id = data['add_director_id']
	director = data['add_director']
	birth = data['add_director_bd']
	gender = data['add_director_gd']
	addNewDirector(director_id, director, birth, gender)

	return render_template('addeddirector.html')

@app.route('/addCast', methods=['POST', 'GET'])
def addCast():
	data = request.form.to_dict()
	cast_id = data['add_cast_id']
	cast = data['add_cast']
	birth = data['add_cast_bd']
	gender = data['add_cast_gd']
	addNewCast(cast_id, cast, birth, gender)

	return render_template('addedcast.html')

@app.route('/updateMovie', methods=['POST', 'GET'])
def updateMovie():
	data = request.form.to_dict()
	original_title = data['original_title']
	new_title = data['new_title']
	updateTitle(original_title, new_title)

	return render_template('updatedtitle.html')

@app.route('/deleteMovie', methods=['POST', 'GET'])
def deleteMovie():
	data = request.form.to_dict()
	movie_title = data['movie_title']
	deleteTitle(movie_title)

	return render_template('deletedtitle.html', title=movie_title)


if __name__ == "__main__":
	app.run(debug=True)