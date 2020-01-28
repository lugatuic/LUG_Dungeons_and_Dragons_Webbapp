ALTER USER 'root'@'127.0.0.1' IDENTIFIED WITH mysql_native_password BY "test";
CREATE DATABASE lugdb;

use lugdb;

CREATE TABLE account(
    id INT NOT NULL AUTO_INCREMENT,
    accountName VARCHAR(20) NOT NULL,
    password VARCHAR(100) NOT NULL,
    email VARCHAR(254) NOT NULL,
    PRIMARY KEY ( id )
);
