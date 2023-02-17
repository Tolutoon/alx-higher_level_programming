-- creates the database hbtn_0d_usa and the table cities on your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use a database
USE hbtn_0d_usa;
-- creates a table
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE NOT NULL AUTO_INCREMENT,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
PRIMARY KEY(id),
FOREIGN KEY(state_id) REFERENCES states(id));
