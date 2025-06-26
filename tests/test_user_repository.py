from lib.user_repository import UserRepository
from lib.user import User
import pytest


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
def test_get_single_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    user = repository.find(1)
    assert user == User(1, "johndo@example.com", "john_do" )

"""
Find method when user_id invalid e.g. not found
"""

def test_find_user_not_found(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)    
    with pytest.raises(ValueError, match="User with ID 999 not found"):
        repository.find(999)


"""
check if we can create a new user 
in the database
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)

    new_user = User(None, "bob@example.com", "bob_wilson")
    repository.create(new_user)
    # Check the user was added 
    users = repository.all()
    assert users == [
        User(1, "johndo@example.com", "john_do"),
        User(2, "jamiedo@example.com", "jamie_do"),
        User(3, "bob@example.com", "bob_wilson"),
    ]

"""
Check if we can delete a user
in the database
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)

    repository.delete(1)

    # Check the user was removed
    users = repository.all()
    assert users == [
        User(2, "jamiedo@example.com", "jamie_do"),
    ]
