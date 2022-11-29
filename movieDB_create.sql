create database MovieDB;
use MovieDB;

create table GenreType (
    genre varchar(50) not null,
    primary key (genre)
    );

create table Movie (
  movie_id int null auto_increment,
  title varchar(100) not null,
  release_year int not null,
  primary key (movie_id)
);

create table Director (
    director_id int null auto_increment,
    director_name varchar(100) not null,
    director_birth_date date not null,
    director_gender varchar(10) not null,
    primary key (director_id)
    );

create table Actor (
    actor_id int null auto_increment,
    actor_name varchar(100) not null,
    birth_date date not null,
    gender varchar(10) not null,
    primary key (actor_id)
    );

create table ActorNationality (
    actor_id int null,
    nationality varchar(50) not null,
    primary key (actor_id, nationality),
    foreign key (actor_id) references Actor(actor_id)
    );

create table MovieDirector (
    movie_id int null,
    director_id int null,
    primary key (movie_id, director_id),
    foreign key (movie_id) references Movie(movie_id),
    foreign key (director_id) references Director(director_id)
    );

create table MovieCast (
    movie_id int null,
    cast_id int null,
    primary key (movie_id, cast_id),
    foreign key (movie_id) references Movie(movie_id),
    foreign key (cast_id) references Actor(actor_id)
    );

create table MovieGenre (
    movie_id int null,
    genre varchar(50) not null,
    primary key (movie_id, genre),
    foreign key (movie_id) references Movie(movie_id),
    foreign key (genre) references GenreType(genre)
    );

create table ProductionCountry (
    movie_id int null,
    country varchar(50) not null,
    primary key (movie_id, country),
    foreign key (movie_id) references Movie(movie_id)
    );

create table OriginalLanguage (
    movie_id int null,
    language varchar(50) not null,
    primary key (movie_id, language),
    foreign key (movie_id) references Movie(movie_id)
    );



