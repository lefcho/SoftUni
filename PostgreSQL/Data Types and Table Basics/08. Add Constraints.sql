ALTER TABLE minions_info
ADD constraint unique_containt
	UNIQUE (id, email),

ADD CONSTRAINT banana_check
	CHECK (banana > 0);
