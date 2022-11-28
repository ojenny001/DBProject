from flask import Flask, render_template, url_for, request, Response, redirect
import pymysql.cursors
from project import *

app = Flask(__name__)

@app.route('/')

@app.route('/home')
def home():
	print('hello')
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

if __name__ == "__main__":
	app.run(debug=True)