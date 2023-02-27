from django.test import TestCase
from loginApp.models import User


class UserModelTestCase(TestCase):
    def setUp(self):
        user = User(username="Test", points=0)

    def test_user_model_can_be_created(self):
        """Try create a user with standard inputs"""
        try:
            user = User(username="Test", points=1)
            user.save()
            pass
        except:
            self.fail("User model couldn't be created")

    def test_user_points_cant_be_neg(self):
        """Make sure user can't be created with negative points"""
        try:
            user = User(username="Test user", points=-1)
            user.save()
            raise RuntimeError
        except RuntimeError:
            self.fail("User created with negative points")
        except:
            pass

    def test_username_must_be_unique(self):
        """Test username must be unique"""
        try:
            user = User(username="testuser", points=0)
            user.save()
            user1 = User(username="testuser", points=0)
            user1.save()
            raise RuntimeError
        except RuntimeError:
            self.fail("Created two users with the same username")
        except:
            pass

    def test_points_doesnt_have_to_be_unique(self):
        """Test multiple users can be created with same points"""
        try:
            user = User(username="testuser", points=0)
            user.save()
            user1 = User(username="testuser1", points=0)
            user1.save()
            pass
        except:
            self.fail("Can't create two user's with same points")
