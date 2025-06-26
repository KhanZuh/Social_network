# Test-driven development for PostRepository
from lib.post_repository import PostRepository
from lib.post import Post

"""
When we call PostRepository#all
We get a list of Post objects reflecting the seed data.
READ
"""
def test_get_all_records(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    posts = repository.all()

    assert posts == [
        Post(1, "First Post", "This is my first post!", 0, 1),
        Post(2, "Another Day", "Had a great day today", 5, 1),
        Post(3, "Hello World", "Just joined the network", 2, 2),
    ]

"""
When we call PostRepository#find
We get a single Post object.
READ
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    post = repository.find(1)
    assert post == Post(1, "First Post", "This is my first post!", 0, 1)

"""
We can find posts by a specific user. 
READ
"""
def test_find_posts_by_user(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    user_posts = repository.find_by_user(1)
    assert user_posts == [
        Post(1, "First Post", "This is my first post!", 0, 1),
        Post(2, "Another Day", "Had a great day today", 5, 1),
    ]

"""
When we call PostRepository#create
We get a new post in the database.
CREATE
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    new_post = Post(None, "New Post", "This is brand new!", 0, 2)
    repository.create(new_post)

    posts = repository.all()
    assert posts == [
        Post(1, "First Post", "This is my first post!", 0, 1),
        Post(2, "Another Day", "Had a great day today", 5, 1),
        Post(3, "Hello World", "Just joined the network", 2, 2),
        Post(4, "New Post", "This is brand new!", 0, 2),
    ]

"""
We can increment view count on posts
Update method
"""
def test_increment_views(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    post_before = repository.find(1)
    repository.increment_views(1)
    post_after = repository.find(1)
    assert post_after.views == post_before.views + 1