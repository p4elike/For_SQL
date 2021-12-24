from sqlalchemy import create_engine
from pprint import pprint

engine = create_engine('postgresql://postgres:070777@localhost:5432/postgres', pool_pre_ping=True)
connection = engine.connect()
#

# connection.execute("""INSERT INTO performer(id, performers_name)
#                       VALUES(1, 'Макс Корж');
#                       """)
# connection.execute("""INSERT INTO performer(id, performers_name)
#                       VALUES(2, 'Сектор Газа');
#                       """)
# connection.execute("""INSERT INTO performer(id, performers_name)
#                       VALUES(3, 'Miyagi');
#                       """)
# connection.execute("""INSERT INTO performer(id, performers_name)
#                       VALUES(4, 'БИ-2');
#                       """)
# connection.execute("""INSERT INTO performer(id, performers_name)
#                       VALUES(5, 'Король и Шут') ;
#                       """)
# connection.execute("""INSERT INTO performer(id, performers_name)
#                       VALUES(6, 'Noize MC');
#                       """)
# connection.execute("""INSERT INTO performer(id, performers_name)
#                       VALUES(7, 'RASA') ;
#                       """)
# connection.execute("""INSERT INTO performer(id, performers_name)
#                       VALUES(8, 'Pizza') ;
#                       """)


# connection.execute("""INSERT INTO genre_music(id, genre_name)
#                       VALUES(1, 'Панк-рок') ;
#                       """)
# connection.execute("""INSERT INTO genre_music(id, genre_name)
#                       VALUES(2, 'Хип-Хоп') ;
#                       """)
# connection.execute("""INSERT INTO genre_music(id, genre_name)
#                       VALUES(3, 'Регги') ;
#                       """)
# connection.execute("""INSERT INTO genre_music(id, genre_name)
#                       VALUES(4, 'Рок') ;
#                       """)
# connection.execute("""INSERT INTO genre_music(id, genre_name)
#                           VALUES(5, 'Хард-Рок') ;
#                       """)


# connection.execute("""INSERT INTO album(id, album_name, release_year)
#                           VALUES(1, 'Ели мясо мужики', 2007)  ;
#                       """)
# connection.execute("""INSERT INTO album(id, album_name, release_year)
#                           VALUES(2, 'Би-2', 2002) ;
#                       """)
# connection.execute("""INSERT INTO album(id, album_name, release_year)
#                           VALUES(3, 'Buster Keaton', 2017) ;
#                       """)
# connection.execute("""INSERT INTO album(id, album_name, release_year)
#                           VALUES(4, 'Кухня', 2018) ;
#                       """)
# connection.execute("""INSERT INTO album(id, album_name, release_year)
#                           VALUES(5, 'Вой на Луну', 2015) ;
#                       """)
# connection.execute("""INSERT INTO album(id, album_name, release_year)
#                           VALUES(6, 'Гуляй, мужик', 1997) ;
#                       """)
# connection.execute("""INSERT INTO album(id, album_name, release_year)
#                           VALUES(7, 'Театръ Демона', 2002) ;
#                       """)
# connection.execute("""INSERT INTO album(id, album_name, release_year)
#                           VALUES(8, 'Сверим сердца', 2004) ;
#                       """)


# connection.execute("""INSERT INTO music(id, music_name, duration, id_album)
#                           VALUES(1, 'Ели мясо мужики', 185, 1) ;
#                       """)
# connection.execute("""INSERT INTO music(id, music_name, duration, id_album)
#                           VALUES(2, 'Гуляй, мужик', 201, 6) ;
#                       """)
# connection.execute("""INSERT INTO music(id, music_name, duration, id_album)
#                           VALUES(3, 'Бомж', 147, 6) ;
#                       """)
# connection.execute("""INSERT INTO music(id, music_name, duration, id_album)
#                           VALUES(4, 'Фары', 192, 4) ;
#                       """)
# connection.execute("""INSERT INTO music(id, music_name, duration, id_album)
#                           VALUES(5, 'Найки', 156, 4) ;
#                       """)
# connection.execute("""INSERT INTO music(id, music_name, duration, id_album)
#                           VALUES(6, 'Твой звонок', 192, 5) ;
#                       """)
# connection.execute("""INSERT INTO music(id, music_name, duration, id_album)
#                           VALUES(7, '30 лет', 205, 5) ;
#                       """)
# connection.execute("""INSERT INTO music(id, music_name, duration, id_album)
#                           VALUES(8, 'Волки', 166, 1) ;
#                       """)
# connection.execute("""INSERT INTO music(id, music_name, duration, id_album)
#                           VALUES(9, 'Депрессия', 155, 2) ;
#                       """)
# connection.execute("""INSERT INTO music(id, music_name, duration, id_album)
#                           VALUES(10, 'Полковнику никто не пишет', 168, 2) ;
#                       """)
# connection.execute("""INSERT INTO music(id, music_name, duration, id_album)
#                           VALUES(11, 'Capitan', 195, 3) ;
#                       """)
# connection.execute("""INSERT INTO music(id, music_name, duration, id_album)
#                           VALUES(12, 'Говори мне', 210, 3) ;
#                       """)
# connection.execute("""INSERT INTO music(id, music_name, duration, id_album)
#                           VALUES(13, 'Кукловод', 178, 7) ;
#                       """)
# connection.execute("""INSERT INTO music(id, music_name, duration, id_album)
#                           VALUES(14, 'Фокусник', 205, 7) ;
#                       """)
# connection.execute("""INSERT INTO music(id, music_name, duration, id_album)
#                           VALUES(15, 'Сверлим сердца', 168, 8) ;
#                       """)


# connection.execute("""INSERT INTO digest(id, digest_name, digest_year)
#                           VALUES(1, 'Релакс', 2020) ;
#                       """)
# connection.execute("""INSERT INTO digest(id, digest_name, digest_year)
#                           VALUES(2, 'Панки в доме', 2016) ;
#                       """)
# connection.execute("""INSERT INTO digest(id, digest_name, digest_year)
#                           VALUES(3, 'В пути', 2016) ;
#                       """)
# connection.execute("""INSERT INTO digest(id, digest_name, digest_year)
#                           VALUES(4, 'Кайфули', 2021) ;
#                       """)
# connection.execute("""INSERT INTO digest(id, digest_name, digest_year)
#                           VALUES(5, 'Попсянка', 2020) ;
#                       """)


# connection.execute("""INSERT INTO albums_performers(performer_id, albums_id)
#                           VALUES(2, 6) ;
#                       """)
# connection.execute("""INSERT INTO albums_performers(performer_id, albums_id)
#                           VALUES(2, 5) ;
#                       """)
# connection.execute("""INSERT INTO albums_performers(performer_id, albums_id)
#                           VALUES(3, 3) ;
#                       """)
# connection.execute("""INSERT INTO albums_performers(performer_id, albums_id)
#                           VALUES(4, 2) ;
#                       """)
# connection.execute("""INSERT INTO albums_performers(performer_id, albums_id)
#                           VALUES(5, 1) ;
#                       """)
# connection.execute("""INSERT INTO albums_performers(performer_id, albums_id)
#                           VALUES(5, 7) ;
#                       """)
# connection.execute("""INSERT INTO albums_performers(performer_id, albums_id)
#                           VALUES(8, 4) ;
#                       """)

# connection.execute("""INSERT INTO genre_performer(performer_id, genre_id)
#                           VALUES(1, 2) ;
#                       """)
# connection.execute("""INSERT INTO genre_performer(performer_id, genre_id)
#                           VALUES(2, 1) ;
#                       """)
# connection.execute("""INSERT INTO genre_performer(performer_id, genre_id)
#                           VALUES(2, 4) ;
#                       """)
# connection.execute("""INSERT INTO genre_performer(performer_id, genre_id)
#                           VALUES(3, 2) ;
#                       """)
# connection.execute("""INSERT INTO genre_performer(performer_id, genre_id)
#                           VALUES(3, 3) ;
#                       """)
# connection.execute("""INSERT INTO genre_performer(performer_id, genre_id)
#                           VALUES(4, 4) ;
#                       """)
# connection.execute("""INSERT INTO genre_performer(performer_id, genre_id)
#                           VALUES(5, 4) ;
#                       """)
# connection.execute("""INSERT INTO genre_performer(performer_id, genre_id)
#                           VALUES(5, 1) ;
#                       """)
# connection.execute("""INSERT INTO genre_performer(performer_id, genre_id)
#                           VALUES(5, 5) ;
#                       """)
# connection.execute("""INSERT INTO genre_performer(performer_id, genre_id)
#                           VALUES(6, 2) ;
#                       """)
# connection.execute("""INSERT INTO genre_performer(performer_id, genre_id)
#                           VALUES(7, 2) ;
#                       """)
# connection.execute("""INSERT INTO genre_performer(performer_id, genre_id)
#                           VALUES(7, 2) ;
#                       """)


# connection.execute("""INSERT INTO music_digest(music_id, digest_id)
#                           VALUES(1, 2) ;
#                       """)
# connection.execute("""INSERT INTO music_digest(music_id, digest_id)
#                           VALUES(2, 2) ;
#                       """)
# connection.execute("""INSERT INTO music_digest(music_id, digest_id)
#                           VALUES(3, 2) ;
#                       """)
# connection.execute("""INSERT INTO music_digest(music_id, digest_id)
#                           VALUES(4, 2) ;
#                       """)
# connection.execute("""INSERT INTO music_digest(music_id, digest_id)
#                           VALUES(5, 5) ;
#                       """)
# connection.execute("""INSERT INTO music_digest(music_id, digest_id)
#                           VALUES(6, 5) ;
#                       """)
# connection.execute("""INSERT INTO music_digest(music_id, digest_id)
#                           VALUES(7, 2) ;
#                       """)
# connection.execute("""INSERT INTO music_digest(music_id, digest_id)
#                           VALUES(8, 2) ;
#                       """)
# connection.execute("""INSERT INTO music_digest(music_id, digest_id)
#                           VALUES(9, 3) ;
#                       """)
# connection.execute("""INSERT INTO music_digest(music_id, digest_id)
#                           VALUES(10, 3) ;
#                       """)
# connection.execute("""INSERT INTO music_digest(music_id, digest_id)
#                           VALUES(11, 1) ;
#                       """)
# connection.execute("""INSERT INTO music_digest(music_id, digest_id)
#                           VALUES(12, 1) ;
#                       """)
# connection.execute("""INSERT INTO music_digest(music_id, digest_id)
#                           VALUES(13, 4) ;
#                       """)
# connection.execute("""INSERT INTO music_digest(music_id, digest_id)
#                           VALUES(14, 4) ;
#                       """)
# connection.execute("""INSERT INTO music_digest(music_id, digest_id)
#                           VALUES(15, 4) ;
#                       """)


sel1 = connection.execute("""SELECT album_name, release_year FROM album
                                WHERE release_year = 2018;
                            """)
sel2 = connection.execute("""SELECT music_name, duration FROM music
                               ORDER BY duration  DESC
                               LIMIT 1;
                            """)
# название треков, продолжительность которых не менее 3 минут;
sel3 = connection.execute("""SELECT music_name, duration FROM music
                               WHERE duration >= 180;
                            """)
sel4 = connection.execute("""SELECT digest_name, digest_year FROM digest
                               WHERE digest_year BETWEEN 2018 AND 2020;
                            """)
sel5 = connection.execute("""SELECT performers_name FROM performer
                               WHERE performers_name NOT LIKE '%% %%';
                            """)
# название треков, которые содержат слово "мужик".
sel6 = connection.execute("""SELECT music_name FROM music
                               WHERE music_name LIKE '%%мужик%%';
                            """)
