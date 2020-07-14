-- creates the database hbtn_0d_usa and the table
-- cities (in the database hbtn_0d_usa) on your MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(id INT NOT NULL UNIQUE AUTO_INCREMENT, name VARCHAR(256), PRIMARY KEY(ID), FOREIGN KEY(states_id), REFERENCES(states));
