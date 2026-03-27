CREATE DATABASE IMDB;
USE IMDB;

CREATE TABLE Movie (
    movie_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100),
    release_year INT
);

INSERT INTO Movie (title, release_year) VALUES
('Inception', 2010),
('Avatar', 2009);

CREATE TABLE Media (
    media_id INT PRIMARY KEY AUTO_INCREMENT,
    movie_id INT,
    media_type ENUM('image','video'),
    url VARCHAR(255),
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id)
);

INSERT INTO Media (movie_id, media_type, url) VALUES
(1, 'image', 'img1.jpg'),
(1, 'video', 'vid1.mp4'),
(2, 'image', 'img2.jpg');

SELECT * from Media;

CREATE TABLE Genre (
    genre_id INT PRIMARY KEY AUTO_INCREMENT,
    genre_name VARCHAR(50)
);

INSERT INTO Genre (genre_name) VALUES
('Sci-Fi'), ('Action');

SELECT * from Genre;

CREATE TABLE Movie_Genre (
    movie_id INT,
    genre_id INT,
    PRIMARY KEY (movie_id, genre_id),
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id),
    FOREIGN KEY (genre_id) REFERENCES Genre(genre_id)
);

INSERT INTO Movie_Genre VALUES
(1,1),
(1,2),
(2,1);

SELECT * from Movie_Genre;

CREATE TABLE User (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50)
);

INSERT INTO User (username) VALUES
('Gayuu'),
('Gautham');

SELECT * from User;

CREATE TABLE Review (
    review_id INT PRIMARY KEY AUTO_INCREMENT,
    movie_id INT,
    user_id INT,
    rating INT,
    comment TEXT,
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

INSERT INTO Review (movie_id, user_id, rating, comment) VALUES
(1,1,5,'Amazing movie'),
(1,2,4,'Superb visuals');

SELECT * from Review;

CREATE TABLE Artist (
    artist_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100)
);

INSERT INTO Artist (name) VALUES
('DiCaprio'),
('James Cameron');

SELECT * FROM Artist;

CREATE TABLE Skill (
    skill_id INT PRIMARY KEY AUTO_INCREMENT,
    skill_name VARCHAR(50)
);

INSERT INTO Skill (skill_name) VALUES
('Acting'), ('Direction');

SELECT * FROM Skill;

CREATE TABLE Artist_Skill (
    artist_id INT,
    skill_id INT,
    PRIMARY KEY (artist_id, skill_id),
    FOREIGN KEY (artist_id) REFERENCES Artist(artist_id),
    FOREIGN KEY (skill_id) REFERENCES Skill(skill_id)
);

INSERT INTO Artist_Skill VALUES
(1,1),
(2,2);

SELECT * FROM Artist_Skill;

CREATE TABLE Artist_Role (
    artist_id INT,
    movie_id INT,
    role VARCHAR(50),
    PRIMARY KEY (artist_id, movie_id, role),
    FOREIGN KEY (artist_id) REFERENCES Artist(artist_id),
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id)
);

INSERT INTO Artist_Role VALUES
(1,1,'Actor'),
(2,2,'Director');

SELECT * FROM Artist_Role;

SELECT u.username, r.rating, r.comment
FROM Review r
RIGHT JOIN User u
ON r.user_id = u.user_id;

SELECT m.title, me.media_type, me.url
FROM Movie m
INNER JOIN Media me 
ON m.movie_id = me.movie_id;