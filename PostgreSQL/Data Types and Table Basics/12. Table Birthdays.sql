CREATE TABLE minions_birthday (
	id serial UNIQUE NOT NULL,
	name VARCHAR(50),
	date_of_birth date,
	age int,
	present VARCHAR(50),
	party timestamptz
);
