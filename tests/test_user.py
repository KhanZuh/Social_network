from lib.user import User

"""
User constructs with id, email_address and username
"""

def test_user_constructs():
    user = User(1, "test@example.com", "test_user")
    assert user.id == 1
    assert user.email_address == "test@example.com"
    assert user.username == "test_user"

def test_formatting():
    user = User(1, "test@example.com", "test_user")
    assert str(user) == "User(1, test@example.com, test_user)"

#compare two identical users and have them be equal

def test_users_are_equal():
    user_1 = User(1, "test@example.com", "test_user")
    user_2 = User(1, "test@example.com", "test_user")
    assert user_1 == user_2 

