# Two tables design recipe template

## Extract the nouns from the user stories 

As a social network user,
So I can have my information registered,
I'd like to have a user account with my email address.

As a social network user,
So I can have my information registered,
I'd like to have a user account with my username.

As a social network user,
So I can write on my timeline,
I'd like to create posts associated with my user account.

As a social network user,
So I can write on my timeline,
I'd like each of my posts to have a title and a content.

As a social network user,
So I can know who reads my posts,
I'd like each of my posts to have a number of views.

NOUNS: User, timeline, account, email_adress, posts, views, content, title, username

## 2. Infer the Table Name and Columns

```
| Record                | Properties            |
| --------------------- | --------------------- |
| User                  | email_adress, username
| Post                  | title, views, content         

# potentially timeline being a property
```

Table: Users
- id: SERIAL
- email_address: text
- username: text

Table: Posts
id: SERIAL
- title: text
- content: text
- views: int

```
# email_adress: text (stores email strings)
# username: text (stores username strings)
# title: text (post titles are strings)
# content: text (post content is strings, potentially long)
# views: int (counting views - whole numbers)
```

## 4. Decide on The Tables Relationship

1. Can one [User] have many [Posts]? (Yes)
2. Can one [Posts] have many [Users]? (No)

This means: User HAS MANY posts, Post BELONGS TO user
Therefore: foreign key goes in the posts table (user_id)

```sql

-- file: seeds/social_network.sql

-- Create the parent table (users) - no fk dependencies
CREATE TABLE users (
    id SERIAL PRIMARY KEY
    email_address text
    username text
);

-- Create the child table (posts) - includes fk to users
CREATE TABLE posts(
    id SERIAL PRIMARY KEY
    title text
    content text
    views int
-- foreign key is {other_table_singular}_id 
    user_id int
    constraint fk_user foreign key(user_id)
        references users(id)
        on delete cascade
);

## 6. Create the tables
/