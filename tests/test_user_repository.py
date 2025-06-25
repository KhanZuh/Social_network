from lib.user_repository import UserRepository
from lib.user import User

"""
when we call user repository with the all() method 
We get a list of user objects reflecting the seed data
"""

def test_get_all_users(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    users = repository.all()
    assert users == [
        User(1, "johndo@example.com", "john_do"),
        User(2, "jamiedo@example.com", "jamie_do"),

    ]




"""
Define method find()
get single user objects

"""


"""
check if we can create a new user 
in the database
"""

"""
Check if we can delete a user
in the database
"""