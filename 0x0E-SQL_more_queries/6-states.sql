-- creates the database hbtn_0d_usa and the table states on your MySQL server
-- creates the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use the database
USE hbtn_0d_usa;
-- creates the table 
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL , PRIMARY KEY(id));
