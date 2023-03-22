""" Outlines the tests to ensure the gamekeeper homepage functions as
intended.
"""
import tempfile
from datetime import datetime
from django.test import TestCase
from submission.models import ImageSubmission
from accounts.models import CustomUser
from gkHomepage.views import add_points


class ImageSubmissionTestCase(TestCase):
    """ Declares each of the tests for the gamekeeper homepage section of the website.

    Args:
        TestCase: The Django test object to be used to test the submission page.
    """

    def set_up(self):
        """ Creates a model submission for use in testing. """
        test_sub = ImageSubmission(building="testBuilding", room="testRoom",
                                  lights_status="OFF",
                                  windows_status="CLOSE",
                                  litter_items=0,
                                  image=tempfile.NamedTemporaryFile(
                                      suffix=".jpg").name, user="testUser",
                                  date=datetime.today().strftime('%Y-%m-%d'))
        test_sub.save()

    def test_cant_add_negative_points(self):
        """ Check a user can't have negative points added. """
        with self.assertRaises(RuntimeError):
            add_points("test", -1)

    def test_cant_add_zero_points(self):
        """ Check a user can't have zero points added. """
        with self.assertRaises(RuntimeError):
            add_points("test", 0)

    def test_user_points_added(self):
        """ Tests a user has n points added with function. """
        user = CustomUser(
            username="test", email="test@test.com", password="password")
        user.save()
        self.assertEqual(user.points, 0)

        # Test user with no points can have 1 point added
        add_points("test", 1)
        updated_user = CustomUser.objects.get(username="test")
        self.assertEqual(updated_user.points, 1)

        # Test user with 1 point can have multiple added
        add_points("test", 5)
        updated_user = CustomUser.objects.get(username="test")
        self.assertEqual(updated_user.points, 6)
