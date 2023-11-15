-- Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).
DROP DATABASE IF EXISTS hbtn_0d_usa;
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT UNIQUE auto_increment not null PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
