""" Creates the class for testing the methods in the accounts app. """
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from accounts.models import CustomUser


class CustomUserModel(TestCase):
    """ Declares each of the tests for the accounts section of the website.

    Args:
        TestCase (TestCase): The test case object to test the accounts with.
    """

    def setUp(self):
        """ Creates a model user for use in testing. """
        user = CustomUser(username="testUser",
                          email="test@exeter.ac.uk", password="password")
        user.save()

    def test_user_has_correct_attributes_saved(self):
        """ Makes sure user has correct attributes saved. """
        user = CustomUser.objects.get(username="testUser")
        self.assertEqual(user.username, "testUser")
        self.assertEqual(user.email, "test@exeter.ac.uk")

    def test_user_not_creater_as_superuser(self):
        """ Tests the user is not automatically created as a superuser. """
        user = CustomUser.objects.get(username="testUser")
        self.assertFalse(user.is_superuser)

    def test_user_cant_be_created_without_username(self):
        """ Tests user must have username. """
        user = get_user_model()
        # Tests user must have username
        with self.assertRaises(TypeError):
            user.objects.create_user(
                email="test1@exeter.ac.uk", password="password")

        # Tests username can't be empty
        with self.assertRaises(ValueError):
            user.objects.create_user(
                username="", email="test1@exeter.ac.uk", password="password")

    def test_username_must_be_unique(self):
        """ Makes sure the username of a user is unique. """
        user1 = CustomUser(username="dupUser",
                           email="dupUser1@exeter.ac.uk", password="password")
        user2 = CustomUser(username="dupUser",
                           email="dupUser2@exeter.ac.uk", password="password")
        user1.save()
        with self.assertRaises(IntegrityError):
            user2.save()

    def test_email_must_be_unique(self):
        """ Asserts the email must be unique. """
        user1 = CustomUser(username="dupUser1",
                           email="dupUser@exeter.ac.uk", password="password")
        user2 = CustomUser(username="dupUser2",
                           email="dupUser@exeter.ac.uk", password="password")
        user1.save()
        with self.assertRaises(IntegrityError):
            user2.save()

    def test_user_default_with_0_points(self):
        """ Asserts that a user is created with 0 points. """
        user = CustomUser.objects.get(username="testUser")
        self.assertEqual(user.points, 0)
