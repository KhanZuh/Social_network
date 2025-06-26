from lib.post import Post

class PostRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        # Get all posts from database
        rows = self._connection.execute('SELECT * from posts')
        posts = []
        for row in rows:
            item = Post(row["id"], row["title"], row["content"], row["views"], row["user_id"])
            posts.append(item)
        return posts  
    
    def find(self, post_id):
        # Find a specific post by ID
        rows = self._connection.execute(
            'SELECT * from posts WHERE id = %s', (post_id,))  
        if rows:
            row = rows[0]
            return Post(row["id"], row["title"], row["content"], row["views"], row["user_id"])
        return None
    
    def find_by_user(self, user_id):
        # Find all posts by a specific user
        rows = self._connection.execute(
            'SELECT * from posts WHERE user_id = %s', (user_id,)) # again using tuples here (user_id,) instead of [user_id] since tuples are immutable --> safe against SQL injection
        posts = []
        for row in rows:
            item = Post(row["id"], row["title"], row["content"],row["views"], row["user_id"])
            posts.append(item)
        return posts
    
    def create(self, post):
        # Create a new post
        self._connection.execute(
            'INSERT INTO posts (title, content, views, user_id) VALUES (%s, %s, %s, %s)',
            (post.title, post.content, post.views, post.user_id))
        return None
    
    def increment_views(self, post_id):
        self._connection.execute('UPDATE posts SET views = views + 1 WHERE id = %s', (post_id,))
        return None