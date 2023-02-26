from django.test import TestCase
from loginApp.models import User


class UserModelTestCase(TestCase):
    def setUp(self):
        user = User(username="Test", points=0)

    def test_user_model_can_be_created(self):
        """Try create a user with standard inputs"""
        try:
            user = User(username="Test", points=0)
            user.save()
            pass
        except:
            self.fail("User model couldn't be created")

    def test_usename_cant_be_more_than_150_chars(self):
        """Try create a user with 151 chars"""
        try:
            # Create a 151 length username
            str = ""
            for i in range(0, 151):
                str = str + "c"
            user = User(username=str, points=0)
            user.save()
            self.fail("User model created with username longer than 150")
        except:
            pass

    def test_username_can_be_up_to_150_chars(self):
        """Make sure can create a user with 150 char username"""
        try:
            # Create a 150 length username
            str = ""
            for i in range(0, 150):
                str = str + "c"
            user = User(username=str, points=0)
            user.save()
            pass
        except:
            self.fail("Can't create username with 150 chars")

    def test_user_points_cant_be_neg(self):
        """Make sure user can't be created with negative points"""
        try:
            user = User(username="Test user", points=-1)
            user.save()
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
            self.fail("Created two users with the same username")
        except:
            pass

    def test_points_doesnt_have_to_be_unique(self):
        """Test username must be unique"""
        try:
            user = User(username="testuser", points=0)
            user.save()
            user1 = User(username="testuser1", points=0)
            user1.save()
            pass
        except:
            self.fail("Can't create two user's with same points")
