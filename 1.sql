
create table if not exists genre_music (
	id integer primary key,
	genre_name varchar(40) unique not null
);


create table if not exists performers (
	id integer primary key,
	performers_name text unique
	genre_id integer references genre_music(id)
 );


create table if not exists albums (
	id integer primary key,
	album_name text not null,
	reLease_year integer,
	id_performer integer references performers(id)
 );
 
create table if not exists music (
	id integer primary key,
	music_name text not null,
	duration integer,
	id_album integer references albums(id)
 );