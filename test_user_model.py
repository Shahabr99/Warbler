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

        db.drop_all()
        db.create_all()
        u1 = User.signup("test1", "email1@email.com", "password", None)
        uid1 = 1111
        u1.id = uid1
        u2 = User.signup("test2", "email2@email.com", "password", None)
        uid2 = 2222
        u2.id = uid2
        db.session.commit()
        u1 = User.query.get(uid1)
        u2 = User.query.get(uid2)
        self.u1 = u1
        self.uid1 = uid1
        self.u2 = u2
        self.uid2 = uid2
        self.client = app.test_client()

    def tearDown(self):
        res = super().tearDown()
        db.session.rollback()
        return res

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


    def test_repr(self):
        """Testing the __repr__ dunder method"""
        
        result = repr(self.u1)
        expected = "User 1: test1, email@email.com"
        self.assertEqual(result, expected)


    def test_is_following(self):
        """Testing if a user1 follows user2"""
        self.u1.following.append(self.u2)
        db.session.commit()

        self.assertTrue(self.u1.is_following(self.u2))
        self.assertFalse(self.u2.is_following(self.u1))


    def test_is_followed_by(self):
        """Testing if user1 is followed  by user2"""
        self.u1.followers.append(self.u2)
        db.session.commit()

        self.assertTrue(self.u2.followers(self.u1))
        self.assertFalse(self.u1.followers(self.u2))


    def test_valid_signup(self):
        """Testing creating a new user when a user signsup"""
        user = User.signup('user1', 'user1@email.com', 'Password', None)
        uid = 5555
        user.id = uid
        deb.session.commit()
        test_user = User.query.get(uid)
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "user1")
        self.assertEqual(user.email, "user1@email.com")
        self.assertNotEqual(user1.password, "Passwod")
        self.assertTrue(user1.password.startswith("$2b$"))


    def test_invalid_username_signup(self):
        invalid = User.signup(None, "test@test.com", "password", None)
        uid = 12345678
        invalid.id = uid
        with self.assertRaises(exc.IntegrityError) as context:
            db.session.commit()


    def test_invalid_email_signup(self):
        test_user = User.signup('test_user', None, "password", None)
        uid = 12456789
        test_user.id = uid
        with self.assertRaises(exc.IntegrityError) as context:
            db.session.commit()
    
    def test_valid_authentication(self):
        u = User.authenticate(self.u1.username, "password")
        self.assertIsNotNone(u)
        self.assertEqual(u.id, self.uid1)

    def test_invalid_username(self):
        self.assertFalse(User.authenticate("wrongusername", "password"))


    def test_wrong_password(self):
        self.assertFalse(User.authenticate(self.u1.username, "wrongpassword"))
