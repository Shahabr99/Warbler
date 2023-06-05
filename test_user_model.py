"""User model tests."""

# run these tests like:
#
#    python -m unittest test_user_model.py


import os
from unittest import TestCase

from models import db, User, Message, Follows

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"


# Now we can import app

from app import app

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

with app.app_context(): 
    db.create_all()


class UserModelTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()
        Message.query.delete()
        Follows.query.delete()

        self.client = app.test_client()

    def test_user_model(self):
        """Does basic model work?"""

        u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )

        db.session.add(u)
        db.session.commit()

        # User should have no messages & no followers
        self.assertEqual(len(u.messages), 0)
        self.assertEqual(len(u.followers), 0)

<<<<<<< HEAD
=======

>>>>>>> fb05c5b (adding the tests)
    def test_repr(self):
        """Testing the __repr__ dunder method"""
        test_user = User(username="test1", email="test@gmail.com", password='test123')
        result = repr(test_user)
        expected = "User 1: test1, test@gmail.com"
        self.assertEqual(result, expected)
<<<<<<< HEAD
        
=======


    def test_is_following(self):
        """Testing if a user1 follows user2"""
        user1 = User(username='test1', email="test@gmail.com", password="test123")
        user2 = User(username='test2', email="test2@gmail.com", password="test321")

        found_user_list = [user for user in self.following if user == user2]

>>>>>>> fb05c5b (adding the tests)
