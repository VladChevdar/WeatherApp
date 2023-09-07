# Vlad Chevdar | CS302 | August 21
# This test aims to test AVL class methods
import pytest
from Main import AVL, User
from random import randint

@pytest.fixture
def tree():
    return AVL()

@pytest.fixture
def random_user():
    first = 'User' + str(randint(0, 999999))
    last = str(randint(0, 999999))
    user = User(first, last)
    return user

def test_insert_and_find(tree, random_user):
    for _ in range(1000):
        assert not tree.find(random_user), 'Found non-existing user'
        assert tree.insert(random_user), 'Error inserting new user'
        random_user = User('User' + str(randint(0, 999999)), str(randint(0, 999999)))

def test_count_users(tree, random_user):
    n = 10000
    for _ in range(n):
        tree.insert(random_user)
        random_user = User('User' + str(randint(0, 999999)), str(randint(0, 999999)))
    assert tree.count_users() == n, 'Incorrect count of users'

def test_password_verification_correct_password(tree, random_user):
    random_user.setPassword('pass')
    tree.insert(random_user)
    assert tree.verify(random_user), 'Failed verification with correct password'

def test_password_verification_wrong_password(tree, random_user):
    random_user.setPassword('none')  # Setting a wrong password
    assert not tree.verify(random_user), 'Passed verification with incorrect password'

if __name__ == '__main__':
    unittest.main()
