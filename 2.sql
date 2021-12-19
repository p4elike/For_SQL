create table if not exists genre_music (
	id integer primary key,
	genre_name varchar(40) unique not null 
);



create table if not exists performer (
	id integer primary key,
	performers_name text unique
 );



create table if not exists genre_performer (
	performer_id integer references genre_music(id),
	genre_id integer references performer(id)
 );
 
	
create table if not exists album (
	id integer primary key,
	album_name text not null,
	reLease_year integer
 );
 
 

create table if not exists albums_performers (
	performer_id integer references performer(id),
	albums_id integer references album(id)	
 );
 


create table if not exists music (
	id integer primary key,
	music_name text not null,
	duration integer not null,
	id_album integer references album(id)
 );
 
 

create table if not exists digest (
	id integer primary key,
	digest_name text not null,
	digest_year date not null
 );
 
 

create table if not exists music_digest (
	music_id integer references music(id),
	digest_id integer references digest(id)	
 );
 