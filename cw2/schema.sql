DROP TABLE if EXISTS user;

CREATE TABLE user (
    id integer NOT NULL,
    user text NOT NULL,
    password text NOT NULL,
    CONSTRAINT ID PRIMARY KEY (id));
/*
 CREATE TABLE posts (
    idPost PRIMARY KEY autoincrement,
    idUser integer,
    text varchar(400) NOT NULL,
    FOREIGN KEY (idUser) REFERENCES user(idUser)
 ); 
 */
