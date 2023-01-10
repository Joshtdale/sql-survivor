CREATE TABLE IF NOT EXISTS heroes (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name varchar(256) UNIQUE NOT NULL,
    about_me varchar(512) NOT null,
    biography varchar(2048) NOT NULL,
    image_url VARCHAR(64)
);

INSERT INTO
    heroes (name, about_me, biography)
VALUES
    (
        'Method Man',
        'The coolest due youll ever meet.',
        'In a freak industrial accident, Method Man was dunked in toxic waste. After an agonizing transformation, she developed the ability to exhale sub-zero mist that freezes everything it touches.'
    );

INSERT INTO
    heroes (name, about_me, biography)
VALUES
    (
        'Masta Killa',
        'He can see into your soul. Literally.',
        'GZA leads a normal life, so long as he wears his special shielded glasses. Once he removes them, he can see through walls, mountains, flesh - to the secrets held within.'
    );

INSERT INTO
    heroes (name, about_me, biography)
VALUES
    (
        'Raekwon',
        'Brute strength cant solve all problems, but he doesnt believe that.',
        'Born on another planet and stranded here during an intergalactic training exercise, Muscles muscles expanded to gigantic proportion in Earths nitrogen-rich atmosphere, giving him amazing strength. The extra arms dont hurt, either.'
    );

INSERT INTO
    heroes (name, about_me, biography)
VALUES
    (
        'Inspectah Deck',
        'Its a Bird! Its a plane! Oh wait, its really just a bird... Inspectah Deck!',
        'Perhaps the next step in human evolution, Inspectah Deck gained his unique abilities manifested shortly after birth, when he floated out of the hospital nursery and into the care of General Allen Fitzpatrick and his Gamma Team. After Fitzpatricks death at the hands of Omega Force, Inspectah Deck went rogue...FOR REVENGE!'
    );

INSERT INTO
    heroes (name, about_me, biography)
VALUES
    (
        'U-God',
        'His name may be ordinary, but his powers are not!',
        'Once a famous medical researcher, U-God performed an experimental procedure on himself - with unexpected results. His full mental potential was unlocked, giving his powers over the physical world and the minds of those around him.'
    );

INSERT INTO
    heroes (name, about_me, biography)
VALUES
    (
        'Ghostface Killah',
        'If you dont tell the truth, you wont get far. Whos on the case? Ghostface Killah!',
        'Born without the ability to see, Ghostface Killah learned from a young age to use his ears. Due to his ability to listen deeply and understand body language nuances before the age of twelve, he was recruited by the Marine Special Forces to help with interviewing high profile liars. One day, he was hit with an intense ray of gamma radiation and the only way the Marine doctors could fix him was to add nanotech robots into his brain. Due to the gamma radiation, nanotech, and prior history of intense deep listening combo, he now has the ability to see everyday objects using his mind, and with immense control he can even zoom in 1000X away!'
    );



CREATE TABLE relationship_types (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name varchar(64) UNIQUE NOT NULL
);

INSERT INTO
    relationship_types (name)
VALUES
    ('Friend');

INSERT INTO
    relationship_types (name)
VALUES
    ('Enemy');

CREATE TABLE relationships (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    hero1_id INTEGER NOT NULL,
    FOREIGN KEY (hero1_id) REFERENCES heroes (id) ON DELETE CASCADE,
    hero2_id INTEGER NOT NULL,
    FOREIGN KEY (hero2_id) REFERENCES heroes (id) ON DELETE CASCADE,
    relationship_type_id INTEGER NOT NULL,
    FOREIGN KEY (relationship_type_id) REFERENCES relationship_types (id) ON DELETE CASCADE
);

INSERT INTO
    relationships (hero1_id, hero2_id, relationship_type_id)
VALUES
    (1, 5, 1);

INSERT INTO
    relationships (hero1_id, hero2_id, relationship_type_id)
VALUES
    (5, 1, 1);

INSERT INTO
    relationships (hero1_id, hero2_id, relationship_type_id)
VALUES
    (5, 3, 2);

INSERT INTO
    relationships (hero1_id, hero2_id, relationship_type_id)
VALUES
    (4, 1, 2);

INSERT INTO
    relationships (hero1_id, hero2_id, relationship_type_id)
VALUES
    (4, 5, 2);

INSERT INTO
    relationships (hero1_id, hero2_id, relationship_type_id)
VALUES
    (4, 3, 2);

INSERT INTO
    relationships (hero1_id, hero2_id, relationship_type_id)
VALUES
    (4, 2, 2);

INSERT INTO
    relationships (hero1_id, hero2_id, relationship_type_id)
VALUES
    (3, 1, 1);

INSERT INTO
    relationships (hero1_id, hero2_id, relationship_type_id)
VALUES
    (3, 5, 1);

INSERT INTO
    relationships (hero1_id, hero2_id, relationship_type_id)
VALUES
    (3, 2, 1);

INSERT INTO
    relationships (hero1_id, hero2_id, relationship_type_id)
VALUES
    (2, 1, 1);

INSERT INTO
    relationships (hero1_id, hero2_id, relationship_type_id)
VALUES
    (2, 3, 1);

INSERT INTO
    relationships (hero1_id, hero2_id, relationship_type_id)
VALUES
    (6, 1, 1);

INSERT INTO
    relationships (hero1_id, hero2_id, relationship_type_id)
VALUES
    (6, 5, 2);

INSERT INTO
    relationships (hero1_id, hero2_id, relationship_type_id)
VALUES
    (6, 2, 1);

CREATE TABLE ability_types (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(64)
);

INSERT INTO
    ability_types (name)
VALUES
    ('Super Strength');

INSERT INTO
    ability_types (name)
VALUES
    ('Flying');

INSERT INTO
    ability_types (name)
VALUES
    ('Telekinesis');

INSERT INTO
    ability_types (name)
VALUES
    ('Telepathy');

INSERT INTO
    ability_types (name)
VALUES
    ('Frost Breath');

INSERT INTO
    ability_types (name)
VALUES
    ('Super Speed');

INSERT INTO
    ability_types (name)
VALUES
    ('Super Vision');

-- SQLINES LICENSE FOR EVALUATION USE ONLY
-- CREATE SEQUENCE abilities_seq;

CREATE TABLE abilities (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    hero_id INTEGER NOT NULL,
    FOREIGN KEY (hero_id) REFERENCES heroes (id) ON DELETE CASCADE,
    ability_type_id INTEGER NOT NULL,
    FOREIGN KEY (ability_type_id) REFERENCES ability_types (id) ON DELETE CASCADE
);

INSERT INTO
    abilities (hero_id, ability_type_id)
VALUES
    (1, 5);

INSERT INTO
    abilities (hero_id, ability_type_id)
VALUES
    (2, 3);

INSERT INTO
    abilities (hero_id, ability_type_id)
VALUES
    (2, 4);

INSERT INTO
    abilities (hero_id, ability_type_id)
VALUES
    (3, 1);

INSERT INTO
    abilities (hero_id, ability_type_id)
VALUES
    (4, 2);

INSERT INTO
    abilities (hero_id, ability_type_id)
VALUES
    (4, 6);

INSERT INTO
    abilities (hero_id, ability_type_id)
VALUES
    (5, 7);

INSERT INTO
    abilities (hero_id, ability_type_id)
VALUES
    (6, 7);