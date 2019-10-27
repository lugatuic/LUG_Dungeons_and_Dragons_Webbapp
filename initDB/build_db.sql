CREATE TABLE account(
    id INT NOT NULL AUTO_INCREMENT,
    accountName VARCHAR(20) NOT NULL,
    fullName VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    email VARCHAR(254) NOT NULL,
    PRIMARY KEY ( id )
);