# Social Network Project

A simple social network application built with Python and PostgreSQL that allows users to create accounts, write posts, and track post engagement through view counts.

## Features

- **User Management**: Users can register with email addresses and usernames
- **Post Creation**: Users can create posts with titles and content
- **View Tracking**: Posts automatically track how many times they've been viewed
- **Timeline**: Users can write posts associated with their accounts

## User Stories

This project implements the following user stories:

> As a social network user,  
> So I can have my information registered,  
> I'd like to have a user account with my email address.

> As a social network user,  
> So I can have my information registered,  
> I'd like to have a user account with my username.

> As a social network user,  
> So I can write on my timeline,  
> I'd like to create posts associated with my user account.

> As a social network user,  
> So I can write on my timeline,  
> I'd like each of my posts to have a title and a content.

> As a social network user,  
> So I can know who reads my posts,  
> I'd like each of my posts to have a number of views.

## Project Structure
![Screenshot 2025-06-26 at 17 05 54](https://github.com/user-attachments/assets/3b94e2de-5096-4903-a95a-bdc0e5979fe8)

## Getting Started

### Prerequisites

- Python 3.x
- PostgreSQL
- pytest (for running tests)

### Installation

1. Clone the repository
2. Set up your PostgreSQL database
3. Install dependencies (if any)
4. Run the seed file to populate test data

### Running the Application

Run the main demo to see all features in action:

```bash
python app.py
```

This will demonstrate:

User account creation and management
Post creation with titles and content
View count tracking and incrementing

## Running Tests
```bash
pytest
```


## Key Methods
### PostRepository
- all() - Get all posts
- find(post_id) - Find a specific post by ID
- find_by_user(user_id) - Get all posts by a specific user
- create(post) - Create a new post
- increment_views(post_id) - Increment the view count for a post

### UserRepository
- all() - Get all users
- find(user_id) - Find a specific user by ID
- create(user) - Create a new user account

## Database Schema
### Users Table
- id (Primary Key)
- username (String)
- email (String)

### Posts Table
- id (Primary Key)
- title (String)
- content (Text)
- views (Integer)
- user_id (Foreign Key to Users)

___Built as a learning project to understand database interactions, repository patterns, and social network fundamentals.___
