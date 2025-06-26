from lib.user import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            item = User(row["id"], row["email_address"], row["username"])
            users.append(item)
        return users
    
    def find(self, user_id):
        rows = self._connection.execute('SELECT * from users WHERE id = %s', (user_id,)) #  The Python Database API specification requires parameters to be passed as a sequence, and tuples (user_id,) and not a list [user_id] are the conventional choice because they're immutable.
        if rows:
            row = rows[0]
            return User(row["id"], row["email_address"], row["username"])
        raise ValueError(f"User with ID {user_id} not found")

    def create(self, user):
        # Create a new user account
        self._connection.execute(
            'INSERT INTO users (email_address, username) VALUES (%s, %s)',
            (user.email_address, user.username))
        return None
        
    def delete(self, user_id):
    # RETURNING is a PostgreSQL feature that gives us back data from the row we just modified
    # It's like saying "delete this user AND tell me their ID so I know you actually deleted something"
    # If no user exists with that ID, PostgreSQL deletes nothing and returns nothing
        rows = self._connection.execute(
        'DELETE FROM users WHERE id = %s RETURNING id', (user_id,))
    
    # Now we check what came back:
    # - If result is None: the database connection had issues
    # - If result is an empty list []: no user was found with that ID, so nothing got deleted
    # - If result has data: we successfully deleted a user!
        if not rows or len(rows) == 0:
        # This means "we tried to delete but found no user with that ID"
            raise ValueError(f"User with ID {user_id} not found")
    
    # If we get here, it means we successfully deleted exactly one user
        return None