DROP TABLE if EXISTS user;

CREATE TABLE user (
    id integer PRIMARY KEY autoincrement,
    username text NOT NULL,
    password text NOT NULL
   );
/*
 CREATE TABLE posts (
    idPost PRIMARY KEY autoincrement,
    idUser integer,
    text varchar(400) NOT NULL,
    FOREIGN KEY (idUser) REFERENCES user(idUser)
 ); 
 */
