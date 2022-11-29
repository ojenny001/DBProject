-- Who directed The Dark Knight? (Christopher Nolan)
select director_id, director_name from Director where director_id in (select director_id from MovieDirector where movie_id in (select movie_id from Movie where title = 'The Dark Knight'));

-- Who are the main casts of The Dark Knight? (Christian Bale, Michael Caine, Gary Oldman, Heath Ledger)
select actor_id, actor_name from Actor where actor_id in (select cast_id from MovieCast where movie_id in (select movie_id from Movie where title = 'The Dark Knight'));

-- What is the genre The Dark Knight? (Crime, Drama, Action, Mystery)
select genre from GenreType where genre in (select genre from MovieGenre where movie_id in (select movie_id from Movie where title = 'The Dark Knight'));

-- What is the original language of The Dark Knight? (English)
select language from OriginalLanguage where movie_id in (select movie_id from Movie where title = 'The Dark Knight');

-- What is the production country of The Dark Knight? (USA)
select country from ProductionCountry where movie_id in (select movie_id from Movie where title = 'The Dark Knight');

-- What is the release year of The Dark Knight? (2008)
select release_year from Movie where title = 'The Dark Knight';

-- What movies are directed by Christopher Nolan? (Batman Begins, The Dark Knight, Inception, The Dark Knight Rises, Interstellar, Dunkirk, Tenet)
select title from Movie where movie_id in (select movie_id from MovieDirector where director_id in (select director_id from Director where director_name = 'Christopher Nolan'));

-- What is the birth date of Christopher Nolan? (1970-07-30)
select director_name, director_birth_date from Director where director_name = 'Christopher Nolan';

-- What is the gender of Christopher Nolan? (Male)
select director_name, director_gender from Director where director_name = 'Christopher Nolan';

-- What movies are acted by Brad Pitt? (Moneyball, Se7en, Fight Club, The Curious Case of Benjamin Button)
select title from Movie where movie_id in (select movie_id from MovieCast where cast_id in (select actor_id from Actor where actor_name = 'Brad Pitt'));

-- What is the birth date of Brad Pitt? (1963-12-18)
select actor_name, birth_date from Actor where actor_name = 'Brad Pitt';

-- What is the nationality of Brad Pitt? (USA)
select nationality from ActorNationality where actor_id in (select actor_id from Actor where actor_name = 'Brad Pitt');

-- What is the gender of Brad Pitt? (Male)
select actor_name, gender from Actor where actor_name = 'Brad Pitt';

-- List all comedy movies (Modern Times, Trouble in Paradise, The Rules of the Game, Broken Flowers)
select title from Movie where movie_id in (select movie_id from MovieGenre where genre = 'Comedy');

-- List all German movies (Uncle Boonmee Who Can Recall His Past Lives, A History of Violence, Fight Club, M)
select title from Movie where movie_id in (select movie_id from ProductionCountry where country = 'Germany');

-- List all of the movies whose runtimes are longer than 120 minutes and their revenues.
select title, runtime, revenue from Movie where runtime > 120;

-- List the names of the directors who worked on the movies with revenues less than 6 figures.
select director_name from Director where director_id in (select director_id from MovieDirector where movie_id in (select movie_id from Movie where revenue < 1000000));

-- List the names of the actors who worked on movies with revenues greater than 6 figures.
select actor_name from Actor where actor_id in (select cast_id from MovieCast where movie_id in (select movie_id from Movie where revenue > 100000));

-- How much revenue did the movies with Brad Pitt generate?
select sum(revenue) from Movie where movie_id in (select movie_id from MovieCast where cast_id in (select actor_id from Actor where actor_name = 'Brad Pitt'));

-- What is the highest grossing movie?
select title, revenue from Movie where revenue = (select max(revenue) from Movie);

-- What is the lowest grossing movie?
select title, revenue from Movie where revenue = (select min(revenue) from Movie);

-- What is the average runtime of movies?
select avg(runtime) from Movie;
