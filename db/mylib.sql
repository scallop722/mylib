
/* Drop Tables */

DROP TABLE IF EXISTS lending_history;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS member;




/* Create Tables */

CREATE TABLE book
(
	id bigserial NOT NULL,
	title varchar(30) NOT NULL,
	author varchar(30) NOT NULL,
	note text,
	PRIMARY KEY (id)
) WITHOUT OIDS;


CREATE TABLE lending_history
(
	id bigserial NOT NULL,
	book_id bigint NOT NULL,
	member_id bigint NOT NULL,
	lenging_date date NOT NULL,
	returned boolean DEFAULT 'false' NOT NULL,
	PRIMARY KEY (id)
) WITHOUT OIDS;


CREATE TABLE member
(
	id bigserial NOT NULL,
	name varchar(20) NOT NULL,
	disabled boolean DEFAULT 'false' NOT NULL,
	PRIMARY KEY (id)
) WITHOUT OIDS;



/* Create Foreign Keys */

ALTER TABLE lending_history
	ADD FOREIGN KEY (book_id)
	REFERENCES book (id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;


ALTER TABLE lending_history
	ADD FOREIGN KEY (member_id)
	REFERENCES member (id)
	ON UPDATE RESTRICT
	ON DELETE RESTRICT
;



