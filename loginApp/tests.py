from django.test import TestCase
from loginApp.models import User


class UserModelTestCase(TestCase):
    def test_user_model_can_be_created(self):
        """Try create a user with standard inputs"""
        try:
            user = User(username="Test", points=1, email='test@test.com',
                        first_name="testf", last_name="testl")
            user.save()
            pass
        except:
            self.fail("User model couldn't be created")

    def test_user_points_cant_be_neg(self):
        """Make sure user can't be created with negative points"""
        try:
            user = User(username="Test user", points=-1,
                        email='test@test.com', first_name="testf", last_name="testl")
            user.save()
            raise RuntimeError
        except RuntimeError:
            self.fail("User created with negative points")
        except:
            pass

    def test_username_must_be_unique(self):
        """Test username must be unique"""
        try:
            user = User(username="testuser", points=0, email='test@test.com',
                        first_name="testf1", last_name="testl1")
            user.save()
            user1 = User(username="testuser", points=0, email='test@test1.com',
                         first_name="testf2", last_name="testl2")
            user1.save()
            raise RuntimeError
        except RuntimeError:
            self.fail("Created two users with the same username")
        except:
            pass

    def test_email_must_be_unique(self):
        """Test email must be unique"""
        try:
            user = User(username="testuser", points=0, email='test@test.com',
                        first_name="testf1", last_name="testl1")
            user.save()
            user1 = User(username="testuser1", points=0, email='test@test.com',
                         first_name="testf2", last_name="testl2")
            user1.save()
            raise RuntimeError
        except RuntimeError:
            self.fail("Created two users with the same username")
        except:
            pass

    def test_points_doesnt_have_to_be_unique(self):
        """Test multiple users can be created with same points"""
        try:
            user = User(username="testuser", points=0, email='test1@test.com',
                        first_name="testf1", last_name="testl1")
            user.save()
            user1 = User(username="testuser1", points=0, email='test2@test.com',
                         first_name="testf2", last_name="testl2")
            user1.save()
            pass
        except:
            self.fail("Can't create two user's with same points")

    def test_firstname_doesnt_have_to_be_unique(self):
        """Test multiple users can be created with same first name"""
        try:
            user = User(username="testuser", points=0, email='test1@test.com',
                        first_name="testf1", last_name="testl1")
            user.save()
            user1 = User(username="testuser1", points=1, email='test2@test.com',
                         first_name="testf1", last_name="testl2")
            user1.save()
            pass
        except:
            self.fail("Can't create two user's with same firstname")

    def test_lastname_doesnt_have_to_be_unique(self):
        """Test multiple users can be created with same last name"""
        try:
            user = User(username="testuser", points=0, email='test1@test.com',
                        first_name="testf1", last_name="testl1")
            user.save()
            user1 = User(username="testuser1", points=1, email='test2@test.com',
                         first_name="testf2", last_name="testl1")
            user1.save()
            pass
        except:
            self.fail("Can't create two user's with same lastname")
