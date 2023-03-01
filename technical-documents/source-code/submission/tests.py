from django.test import TestCase
from submission.models import ImageSubmission
import tempfile
from submission.views import addPoints
from accounts.models import CustomUser


class ImageSubmissionTestCase(TestCase):
    """ Declares each of the tests for the submission section of the website.
    """
    def setUp(self):
        """ Creates a model submission for use in testing. """
        testSub = ImageSubmission(building="testBuilding", room="testRoom",
                                  lights="OFF", windows="AUTO",
                                  image=tempfile.NamedTemporaryFile(
                                                suffix=".jpg").name,
                                  no_litter=True, sockets_off=True
                                  )
        testSub.save()

    def test_jpg_format_can_be_created(self):
        """ Tests the jpg file extension is accepted in image submission. """
        try:
            testSub = ImageSubmission(building="testBuilding", room="testRoom",
                                      lights="AUTOMATIC", windows="CLOSE",
                                      image=tempfile.NamedTemporaryFile(
                                                    suffix=".jpg").name,
                                      no_litter=True, sockets_off=True
                                      )
            testSub.save()
            pass

        except:
            self.fail("Can't save an image file with a .jpg format")

    def test_jpeg_format_can_be_created(self):
        """ Tests the jpeg file extension is accepted in image submission. """
        try:
            testSub = ImageSubmission(building="testBuilding", room="testRoom",
                                      lights="AUTOMATIC", windows="CLOSE",
                                      image=tempfile.NamedTemporaryFile(
                                                    suffix=".jpeg").name,
                                      no_litter=True, sockets_off=True
                                      )
            testSub.save()
            pass

        except:
            self.fail("Can't save an image file with a .jpeg format")

    def test_gif_format_can_be_created(self):
        """ Tests the gif file extension is accepted in image submission. """
        try:
            testSub = ImageSubmission(building="testBuilding", room="testRoom",
                                      lights="AUTOMATIC", windows="CLOSE",
                                      image=tempfile.NamedTemporaryFile(
                                                    suffix=".gif").name,
                                      no_litter=True, sockets_off=True
                                      )
            testSub.save()
            pass

        except:
            self.fail("Can't save an image file with a .gif format")

    def test_jpg_format_can_be_created(self):
        """ Tests the png file extension is accepted in image submission. """
        try:
            testSub = ImageSubmission(building="testBuilding", room="testRoom",
                                      lights="AUTOMATIC", windows="CLOSE",
                                      image=tempfile.NamedTemporaryFile(
                                                    suffix=".png").name,
                                      no_litter=True, sockets_off=True
                                      )
            testSub.save()
            pass

        except:
            self.fail("Can't save an image file with a .png format")

    def test_cant_add_negative_points(self):
        """ Check a user can't have negative points added. """
        with self.assertRaises(RuntimeError):
            addPoints("test", -1)

    def test_cant_add_zero_points(self):
        """ Check a user can't have zero points added. """
        with self.assertRaises(RuntimeError):
            addPoints("test", 0)

    def test_user_points_added(self):
        """ Tests a user has n points added with function. """
        user = CustomUser(
            username="test", email="test@test.com", password="password")
        user.save()
        self.assertEqual(user.points, 0)

        # Test user with no points can have 1 point added
        addPoints("test", 1)
        updated_user = CustomUser.objects.get(username="test")
        self.assertEqual(updated_user.points, 1)

        # Test user with 1 point can have multiple added
        addPoints("test", 5)
        updated_user = CustomUser.objects.get(username="test")
        self.assertEqual(updated_user.points, 6)
