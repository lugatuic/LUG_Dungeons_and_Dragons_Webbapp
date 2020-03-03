use lugdb;

CREATE TABLE account(
    id INT NOT NULL AUTO_INCREMENT,
    accountName VARCHAR(20) NOT NULL,
    password VARCHAR(100) NOT NULL,
    email VARCHAR(254) NOT NULL,
    PRIMARY KEY ( id )
);

CREATE TABLE charSheet(
    charid INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    race VARCHAR(20) NOT NULL,
    lore VARCHAR(1000),
    ideals VARCHAR(254),
    bonds VARCHAR(254),
    flaws VARCHAR(254),
    id INT,
    PRIMARY KEY (charid),
    FOREIGN KEY (id)
        REFERENCES account(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE classlevel(
    class VARCHAR(50) NOT NULL,
    hitDie VARCHAR(10) NOT NULL,
    classlvl INT NOT NULL,
    charid INT,
    PRIMARY KEY (class),
    FOREIGN KEY (charid)
        REFERENCES charSheet(charid)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE basestats(
    strength INT NOT NULL,
    dexterity INT NOT NULL,
    constitution INT NOT NULL,
    intelligence INT NOT NULL,
    wisdom INT NOT NULL,
    charisma INT NOT NULL,
    proficiency INT NOT NULL,
    maxhp INT NOT NULL,
    movespeed INT NOT NULL,
    charid INT,
    FOREIGN KEY (charid)
        REFERENCES charSheet(charid)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);
