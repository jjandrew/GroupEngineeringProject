""" Creates the class for testing the methods in the accounts app. """
import tempfile
from datetime import datetime, timedelta
from django.test import TestCase
from accounts.models import CustomUser
from leaderboard.models import BuildingModel
from submission.models import ImageSubmission, RoomModel
import tempfile
from submission.views import add_points, calc_points
from accounts.models import CustomUser
from gkHomepage.crowd_source import input_stats
from datetime import datetime


class ImageSubmissionTestCase(TestCase):
    """ Declares each of the tests for the submission section of the website.

    Args:
        TestCase (TestCase): The test case object to test the submission
        models with.
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

    def test_jpg_format_can_be_created(self):
        """ Tests the jpg file extension is accepted in image submission. """
        try:
            test_sub = ImageSubmission(building="testBuilding", room="testRoom",
                                      lights_status="OFF",
                                      windows_status="CLOSE",
                                      litter_items=0,
                                      image=tempfile.NamedTemporaryFile(
                                          suffix=".jpg").name, user="testUser",
                                      date=datetime.today().strftime('%Y-%m-%d')
                                      )
            test_sub.save()
            pass

        except:
            self.fail("Can't save an image file with a .jpg format")

    def test_jpeg_format_can_be_created(self):
        """ Tests the jpeg file extension is accepted in image submission. """
        try:
            test_sub = ImageSubmission(building="testBuilding", room="testRoom",
                                      lights_status="OFF",
                                      windows_status="CLOSE",
                                      litter_items=0,
                                      image=tempfile.NamedTemporaryFile(
                                          suffix=".jpeg").name, user="testUser",
                                      date=datetime.today().strftime('%Y-%m-%d')
                                      )
            test_sub.save()
            pass

        except:
            self.fail("Can't save an image file with a .jpeg format")

    def test_gif_format_can_be_created(self):
        """ Tests the gif file extension is accepted in image submission. """
        try:
            test_sub = ImageSubmission(building="testBuilding", room="testRoom",
                                      lights_status="OFF",
                                      windows_status="CLOSE",
                                      litter_items=0,
                                      image=tempfile.NamedTemporaryFile(
                                          suffix=".gif").name, user="testUser",
                                      date=datetime.today().strftime('%Y-%m-%d')
                                      )
            test_sub.save()
            pass

        except:
            self.fail("Can't save an image file with a .gif format")

    def test_png_format_can_be_created(self):
        """ Tests the png file extension is accepted in image submission. """
        try:
            test_sub = ImageSubmission(building="testBuilding", room="testRoom",
                                      lights_status="OFF",
                                      windows_status="CLOSE",
                                      litter_items=0,
                                      image=tempfile.NamedTemporaryFile(
                                          suffix=".png").name, user="testUser",
                                      date=datetime.today().strftime('%Y-%m-%d')
                                      )
            test_sub.save()
            pass

        except:
            self.fail("Can't save an image file with a .png format")

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


class RoomSubmissionTestCase(TestCase):
    """ Declares each of the tests for the room submissions.

    Args:
        TestCase (TestCase): The test case object to test the submission
        models with.
    """
    existing_room: RoomModel

    def set_up(self):
        """ Create a room for use """
        self.existing_room = RoomModel(building="Test Building", name="existingroom",
                                       number_lights_on=5, number_windows_open=5,
                                       litter_items=5, number_submissions=5)
        self.existing_room.save()

    def test_input_stats_changes_stats_if_on_and_open(self):
        """ Tests stats are changed if windows open and lights on """
        existing_submission = ImageSubmission(building="Test Building", room="existingroom",
                                              lights_status="ON",
                                              windows_status="OPEN",
                                              litter_items=1,
                                              image=tempfile.NamedTemporaryFile(
                                                  suffix=".jpg").name
                                              )
        input_stats(existing_submission)
        room = RoomModel.objects.get(
            name="existingroom", building="Test Building")
        self.assertEquals(room.number_lights_on, 6)
        self.assertEquals(room.number_windows_open, 6)
        self.assertEquals(room.litter_items, 6)
        self.assertEquals(room.number_submissions, 6)

        # Reset existing room
        self.existing_room = RoomModel(building="Test Building", name="existingroom",
                                       number_lights_on=5, number_windows_open=5,
                                       litter_items=5, number_submissions=5)
        self.existing_room.save()

    def test_input_stats_dont_change_if_closed_and_off(self):
        """ Tests stats don't change if windows closed and lights off """
        existing_submission = ImageSubmission(building="Test Building", room="existingroom",
                                              lights_status="OFF",
                                              windows_status="CLOSE",
                                              litter_items=0,
                                              image=tempfile.NamedTemporaryFile(
                                                  suffix=".jpg").name
                                              )
        input_stats(existing_submission)
        room = RoomModel.objects.get(
            name="existingroom", building="Test Building")
        self.assertEquals(room.number_lights_on, 5)
        self.assertEquals(room.number_windows_open, 5)
        self.assertEquals(room.litter_items, 5)
        self.assertEquals(room.number_submissions, 6)

        # Reset existing room
        self.existing_room = RoomModel(building="Test Building", name="existingroom",
                                       number_lights_on=5, number_windows_open=5,
                                       litter_items=5, number_submissions=5)
        self.existing_room.save()

    def test_input_stats_dont_change_if_automatic(self):
        """ Tests stats don't change if windows and lights are automatic """
        existing_submission = ImageSubmission(building="Test Building", room="existingroom",
                                              lights_status="AUTO",
                                              windows_status="AUTO",
                                              litter_items=0,
                                              image=tempfile.NamedTemporaryFile(
                                                  suffix=".jpg").name
                                              )
        input_stats(existing_submission)
        room = RoomModel.objects.get(
            name="existingroom", building="Test Building")
        self.assertEquals(room.number_lights_on, 5)
        self.assertEquals(room.number_windows_open, 5)
        self.assertEquals(room.litter_items, 5)
        self.assertEquals(room.number_submissions, 6)

        # Reset existing room
        self.existing_room = RoomModel(building="Test Building", name="existingroom",
                                       number_lights_on=5, number_windows_open=5,
                                       litter_items=5, number_submissions=5)
        self.existing_room.save()


class test_user_streaks(TestCase):
    """ Declares each of the tests for the user streaks.

    Args:
        TestCase (TestCase): The test case object to test the submission
        models with.
    """
    user: CustomUser

    def set_up(self):
        """ Creates a custom user with default values """
        self.user = CustomUser(
            username="test", email="test@test.com", password="password")
        self.user.save()

    def test_new_user_has_streak_of_0(self):
        """ Tests a user is created with default streak  value 0 """
        user = CustomUser.objects.get(username="test")
        self.assertEqual(user.streak, 0)


class CalcPointsTest(TestCase):
    """ Declares each of the tests for calculating user points.

    Args:
        TestCase (TestCase): The test case object to test the submission
        models with.
    """
    building = 'AMORY'

    def test_one_point_added_if_new_room(self):
        """ Test one point for a new room """
        BuildingModel(name=self.building).save()
        points = calc_points(self.building)
        self.assertEqual(points, 1)

    def test_two_points_added_if_two_days_passed(self):
        """ Test 3 points added if three days have passed """
        # Create a new building model
        BuildingModel(name=self.building).save()
        points = calc_points(self.building)
        self.assertEqual(points, 1)

        # Set the last_done date to 3 days ago for the building
        building = BuildingModel.objects.get(name=self.building)
        building.last_done = datetime.now() - timedelta(days=3)
        building.save()

        # Check three points given for the building
        points = calc_points(self.building)
        self.assertEqual(points, 3)
