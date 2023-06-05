from unittest import TestCase
import os
from models import db, User, Message, Follows, Likes

os.environ['DATABASE_URL'] = "postgresql://warbler-test"

from app import app

with app.app_context():
    db.create_all()


class UserModelTestCase(TestCase):
    """Test views for messages"""
    def setUp(self):
        db.drop_all()
        db.create_all()

        user = User("user1", "user1@yahoo.com", "password", None)
        self.uid = 1234
        user.id = uid
        db.session.commit()
        self.u = User.query.get(self.uid)
        self.client = app.testClient