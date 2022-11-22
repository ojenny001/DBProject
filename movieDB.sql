create database movie;
use movie;

create table production_cos(
    production_co_id int not null,
    production_co_name varchar(100) not null,
    production_co_country varchar(50) not null,
    production_co_description varchar(500) not null,
    primary key(production_co_id)
);

create table actors(
    actor_id int not null,
    actor_name varchar(100) not null,
    actor_bday date not null,
    actor_gender varchar(10) not null,
    actor_biography varchar(500) not null,
    primary key(actor_id)
);

create table directors(
    director_id int not null,
    director_name varchar(100) not null,
    director_bday date not null,
    director_gender varchar(10) not null,
    director_biography varchar(500) not null,
    primary key(director_id)
);

create table genre(
    genre_id int not null,
    genre_name varchar(50) not null,
    primary key(genre_id)
);

create table watch_providers(
    watch_provider_id int not null,
    watch_provider_name varchar(100) not null,
    watch_provider_country varchar(50) not null,
    watch_provider_accessmode varchar(50) not null,
    primary key(watch_provider_id)
);

create table movies(
    movie_id int not null,
    title varchar(100) not null,
    release_date date not null,
    production_co_id int not null,
    production_country varchar(50) not null,
    genre_id int not null,
    revenue float not null,
    runtime int not null,
    language varchar(50) not null,
    overview varchar(500) not null,
    primary key(movie_id),
    foreign key(production_co_id) references production_cos(production_co_id),
    foreign key(genre_id) references genre(genre_id)
);

create table translations(
    movie_id int not null,
    translated_language varchar(50) not null,
    english_movie_name varchar(100) not null,
    translated_movie_name varchar(100) not null,
    primary key(movie_id, translated_language),
    foreign key(movie_id) references movies(movie_id)
);

create table cast_members(
    movie_id int not null,
    actor_id int not null,
    character_name varchar(100) not null,
    primary key(movie_id, actor_id),
    foreign key(movie_id) references movies(movie_id),
    foreign key(actor_id) references actors(actor_id)
);

create table crew_members(
    movie_id int not null,
    crew_id int not null,
    crew_name varchar(100) not null,
    job varchar(50) not null,
    department varchar(50) not null,
    primary key(movie_id, crew_id),
    foreign key(movie_id) references movies(movie_id)
);


