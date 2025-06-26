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

INSERT INTO posts (title, content, views, user_id) VALUES ('First Post', 'This is my first post!', 0, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('Another Day', 'Had a great day today', 5, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('Hello World', 'Just joined the network', 2, 2);
