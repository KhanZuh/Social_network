DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email_address text,
    username text
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text,
    views int, 
    user_id int,
    constraint fk_user foreign key(user_id)
        references users(id)
        on delete cascade
);

INSERT INTO users (email_address, username) VALUES ('johndo@example.com', 'john_do');
INSERT INTO users (email_address, username) VALUES ('jamiedo@example.com', 'jamie_do');