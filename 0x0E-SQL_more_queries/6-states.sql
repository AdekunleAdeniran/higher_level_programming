-- MySQL script to create Database and table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
       id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(256)
);
