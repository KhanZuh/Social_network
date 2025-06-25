from lib.post import Post

"""
Post constructs with id, title, content, views, and user_id
"""
def test_post_constructs():
    post = Post(1, "My First Post", "Hello World!", 0, 1)
    assert post.id == 1
    assert post.title == "My First Post"
    assert post.content == "Hello World!"
    assert post.views == 0
    assert post.user_id == 1

"""
We can format posts to strings nicely
"""
def test_posts_format_nicely():
    post = Post(1, "My First Post", "Hello World!", 5, 1)
    assert str(post) == "Post(1, My First Post, Hello World!, 5, 1)"

"""
We can compare two identical posts
"""
def test_posts_are_equal():
    post1 = Post(1, "Title", "Content", 10, 1)
    post2 = Post(1, "Title", "Content", 10, 1)
    assert post1 == post2




