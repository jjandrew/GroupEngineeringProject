from django.test import TestCase
from submission.models import ImageSubmission, RoomModel
import tempfile
from submission.views import addPoints, calc_user_streaks
from accounts.models import CustomUser
from submission.crowd_source import input_stats
from datetime import datetime, timedelta
from freezegun import freeze_time


class ImageSubmissionTestCase(TestCase):
    """ Declares each of the tests for the submission section of the website.
    """

    def setUp(self):
        """ Creates a model submission for use in testing. """
        testSub = ImageSubmission(building="testBuilding", room="testRoom",
                                  lights_status="OFF",
                                  windows_status="CLOSE",
                                  litter_items=0,
                                  image=tempfile.NamedTemporaryFile(
                                      suffix=".jpg").name, user="testUser",
                                  date=datetime.today().strftime('%Y-%m-%d'))
        testSub.save()

    def test_jpg_format_can_be_created(self):
        """ Tests the jpg file extension is accepted in image submission. """
        try:
            testSub = ImageSubmission(building="testBuilding", room="testRoom",
                                      lights_status="OFF",
                                      windows_status="CLOSE",
                                      litter_items=0,
                                      image=tempfile.NamedTemporaryFile(
                                          suffix=".jpg").name, user="testUser",
                                      date=datetime.today().strftime('%Y-%m-%d')
                                      )
            testSub.save()
            pass

        except:
            self.fail("Can't save an image file with a .jpg format")

    def test_jpeg_format_can_be_created(self):
        """ Tests the jpeg file extension is accepted in image submission. """
        try:
            testSub = ImageSubmission(building="testBuilding", room="testRoom",
                                      lights_status="OFF",
                                      windows_status="CLOSE",
                                      litter_items=0,
                                      image=tempfile.NamedTemporaryFile(
                                          suffix=".jpeg").name, user="testUser",
                                      date=datetime.today().strftime('%Y-%m-%d')
                                      )
            testSub.save()
            pass

        except:
            self.fail("Can't save an image file with a .jpeg format")

    def test_gif_format_can_be_created(self):
        """ Tests the gif file extension is accepted in image submission. """
        try:
            testSub = ImageSubmission(building="testBuilding", room="testRoom",
                                      lights_status="OFF",
                                      windows_status="CLOSE",
                                      litter_items=0,
                                      image=tempfile.NamedTemporaryFile(
                                          suffix=".gif").name, user="testUser",
                                      date=datetime.today().strftime('%Y-%m-%d')
                                      )
            testSub.save()
            pass

        except:
            self.fail("Can't save an image file with a .gif format")

    def test_png_format_can_be_created(self):
        """ Tests the png file extension is accepted in image submission. """
        try:
            testSub = ImageSubmission(building="testBuilding", room="testRoom",
                                      lights_status="OFF",
                                      windows_status="CLOSE",
                                      litter_items=0,
                                      image=tempfile.NamedTemporaryFile(
                                          suffix=".png").name, user="testUser",
                                      date=datetime.today().strftime('%Y-%m-%d')
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


class RoomSubmissionTestCase(TestCase):
    existing_room: RoomModel

    def setUp(self):
        """Create a room for use"""
        self.existing_room = RoomModel(building="Test Building", name="existingroom",
                                       number_lights_on=5, number_windows_open=5,
                                       litter_items=5, number_submissions=5)
        self.existing_room.save()

    def test_input_stats_changes_stats_if_on_and_open(self):
        """Tests stats are changed if windows open and lights on"""
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
        """Tests stats don't change if windows closed and lights off"""
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
        """Tests stats don't change if windows and lights are automatic"""
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
    """A testing case for user streaks"""
    user: CustomUser

    def setUp(self):
        """Creates a custom user with default values"""
        self.user = CustomUser(
            username="test", email="test@test.com", password="password")
        self.user.save()

    def test_new_user_has_streak_of_0(self):
        """Tests a user is created with default streak  value 0"""
        user = CustomUser.objects.get(username="test")
        self.assertEqual(user.streak, 0)

    def test_when_submission_added_streak_is_1(self):
        """Tests a user's streak increments to 1 when submission completed"""
        user = CustomUser(
            username="test1", email="test1@test.com", password="password")
        user.save()
        date = datetime(2024, 1, 1)
        calc_user_streaks(user, date)
        self.assertEqual(user.streak, 1)

    def test_when_submission_added_twice_streak_stays_1(self):
        """Tests streak only increments on change in day"""
        user = CustomUser(
            username="test2", email="test2@test.com", password="password")
        user.save()
        date = datetime(2024, 1, 1)
        calc_user_streaks(user, date)
        calc_user_streaks(user, date)
        date += timedelta(days=1)
        self.assertEqual(user.streak, 1)

    def test_when_submission_added_for_tomorrow_streak_is_2(self):
        """Tests the streak can increment when added for each day"""
        user = CustomUser(
            username="test3", email="test3@test.com", password="password")
        user.save()
        date = datetime(2024, 1, 1)
        calc_user_streaks(user, date)
        date += timedelta(days=1)
        calc_user_streaks(user, date)
        self.assertEqual(user.streak, 2)

    def test_when_date_missed_streak_goes_to_1(self):
        """Tests a streak is reset if a user missed a day of submissions"""
        user = CustomUser(
            username="test4", email="test4@test.com", password="password")
        user.save()
        date = datetime(2024, 1, 1)
        calc_user_streaks(user, date)
        date += timedelta(days=1)
        calc_user_streaks(user, date)
        self.assertEqual(user.streak, 2)
        date += timedelta(days=2)
        calc_user_streaks(user, date)
        self.assertEqual(user.streak, 1)
