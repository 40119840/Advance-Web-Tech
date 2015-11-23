DROP TABLE if EXISTS users;

 CREATE TABLE user (
     interger PRIMARY KEY (ID)autoincrement,
     username varchar(50) NOT NULL,
     password varchar(300)NOT NULL,
);
 /*   
 CREATE TABLE posts (
    interger PRIMARY KEY (ID)
    text varchar(400) NOT NULL,
    image varbinary(max)
 ); 
 
 CREATE TABLE link (
    FOREIGN KEY (USER-NAME)REFERENCES user(ID)
    Foreign KEY (USER-POST)REFERENCES posts(ID)
 );
 
 
 */
 
