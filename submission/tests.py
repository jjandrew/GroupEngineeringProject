from django.test import TestCase
from submission.models import ImageSubmission
import tempfile
from submission.views import addPoints
from loginApp.models import User


class ImageSubmissionTestCase(TestCase):
    def setUp(self):
        """Creates a model submission for use in testing"""
        testSub = ImageSubmission(building="testBuilding", room="testRoom", lights="OFF", windows="AUTO",
                                  image=tempfile.NamedTemporaryFile(suffix=".jpg").name, no_litter=True, sockets_off=True)
        testSub.save()
        # Creates a user for testing
        user = User(username="test", points=1)
        user.save()

    def test_windows_can_be_close_or_auto(self):
        """Makes sure more than 5 characters not accepted in windows field"""
        try:
            testSub = ImageSubmission(building="testBuilding", room="testRoom", lights="OFF", windows="AUTOMA",
                                      image=tempfile.NamedTemporaryFile(suffix=".jpg").name, no_litter=True, sockets_off=True)
            raise RuntimeError
        except RuntimeError:
            self.fail("More than 5 letters accepted for windows")
        except:
            pass

    def test_lights_can_be_off_or_auto(self):
        """Makes sure more than 4 characters not accepted in lights field"""
        try:
            testSub = ImageSubmission(building="testBuilding", room="testRoom", lights="AUTOM", windows="CLOSE",
                                      image=tempfile.NamedTemporaryFile(suffix=".jpg").name, no_litter=True, sockets_off=True)
            raise RuntimeError
        except RuntimeError:
            self.fail("More than 5 letters accepted for lights")
        except:
            pass

    def test_jpg_format_can_be_created(self):
        """Tests the jpg file extension is accepted in image submission"""
        try:
            testSub = ImageSubmission(building="testBuilding", room="testRoom", lights="AUTOMATIC", windows="CLOSE",
                                      image=tempfile.NamedTemporaryFile(suffix=".jpg").name, no_litter=True, sockets_off=True)
            testSub.save()
            pass
        except:
            self.fail("Can't save an image file with a .jpg format")

    def test_jpeg_format_can_be_created(self):
        """Tests the jpeg file extension is accepted in image submission"""
        try:
            testSub = ImageSubmission(building="testBuilding", room="testRoom", lights="AUTOMATIC", windows="CLOSE",
                                      image=tempfile.NamedTemporaryFile(suffix=".jpeg").name, no_litter=True, sockets_off=True)
            testSub.save()
            pass
        except:
            self.fail("Can't save an image file with a .jpeg format")

    def test_gif_format_can_be_created(self):
        """Tests the gif file extension is accepted in image submission"""
        try:
            testSub = ImageSubmission(building="testBuilding", room="testRoom", lights="AUTOMATIC", windows="CLOSE",
                                      image=tempfile.NamedTemporaryFile(suffix=".gif").name, no_litter=True, sockets_off=True)
            testSub.save()
            pass
        except:
            self.fail("Can't save an image file with a .gif format")

    def test_jpg_format_can_be_created(self):
        """Tests the png file extension is accepted in image submission"""
        try:
            testSub = ImageSubmission(building="testBuilding", room="testRoom", lights="AUTOMATIC", windows="CLOSE",
                                      image=tempfile.NamedTemporaryFile(suffix=".png").name, no_litter=True, sockets_off=True)
            testSub.save()
            pass
        except:
            self.fail("Can't save an image file with a .png format")

    def test_non_img_format_denied(self):
        """Tests other non-image file extensions not accepted in image submission"""
        try:
            testSub = ImageSubmission(building="testBuilding", room="testRoom", lights="AUTOMATIC", windows="CLOSE",
                                      image=tempfile.NamedTemporaryFile(suffix=".py").name, no_litter=True, sockets_off=True)
            testSub.save()
            testSub1 = ImageSubmission(building="testBuilding", room="testRoom", lights="AUTOMATIC", windows="CLOSE",
                                       image=tempfile.NamedTemporaryFile(suffix=".txt").name, no_litter=True, sockets_off=True)
            testSub1.save()
            raise RuntimeError
        except RuntimeError:
            self.fail("Accepted non img format as image")
        except:
            pass

    def test_user_can_be_added_to_leaderboard_if_first_submission(self):
        """Checks an unused user can have points added"""
        addPoints("unusedUser", 1)
        user = User.objects.get(username="unusedUser")
        self.assertEqual(user.points, 1)

    def test_user_can_have_points_added(self):
        """Checks a used user can haev points added"""
        addPoints("test", 4)
        user = User.objects.get(username="test")
        self.assertEqual(user.points, 5)

    def test_cant_add_negative_points(self):
        """Check a user can't have negative points added"""
        try:
            addPoints("test", -1)
            raise RuntimeError
        except RuntimeError:
            self.fail("Added negative points to user")
        except RuntimeError:
            pass
