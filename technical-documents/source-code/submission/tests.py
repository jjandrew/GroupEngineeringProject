from django.test import TestCase
from submission.models import ImageSubmission, RoomModel
import tempfile
from submission.views import addPoints
from accounts.models import CustomUser
from submission.crowd_source import get_statistics, statistics_valid, input_stats


class ImageSubmissionTestCase(TestCase):
    """ Declares each of the tests for the submission section of the website.
    """

    def setUp(self):
        """ Creates a model submission for use in testing. """
        testSub = ImageSubmission(building="testBuilding", room="testRoom",
                                  number_of_lights=0, number_lights_on=0, number_of_windows=0,
                                  number_windows_open=0, number_plugs=0, number_plugs_on=0,
                                  litter_items=0,
                                  image=tempfile.NamedTemporaryFile(
                                      suffix=".jpg").name
                                  )
        testSub.save()

    def test_jpg_format_can_be_created(self):
        """ Tests the jpg file extension is accepted in image submission. """
        try:
            testSub = ImageSubmission(building="testBuilding", room="testRoom",
                                      number_of_lights=0, number_lights_on=0, number_of_windows=0,
                                      number_windows_open=0, number_plugs=0, number_plugs_on=0,
                                      litter_items=0,
                                      image=tempfile.NamedTemporaryFile(
                                          suffix=".jpg").name
                                      )
            testSub.save()
            pass

        except:
            self.fail("Can't save an image file with a .jpg format")

    def test_jpeg_format_can_be_created(self):
        """ Tests the jpeg file extension is accepted in image submission. """
        try:
            testSub = ImageSubmission(building="testBuilding", room="testRoom",
                                      number_of_lights=0, number_lights_on=0, number_of_windows=0,
                                      number_windows_open=0, number_plugs=0, number_plugs_on=0,
                                      litter_items=0,
                                      image=tempfile.NamedTemporaryFile(
                                          suffix=".jpeg").name
                                      )
            testSub.save()
            pass

        except:
            self.fail("Can't save an image file with a .jpeg format")

    def test_gif_format_can_be_created(self):
        """ Tests the gif file extension is accepted in image submission. """
        try:
            testSub = ImageSubmission(building="testBuilding", room="testRoom",
                                      number_of_lights=0, number_lights_on=0, number_of_windows=0,
                                      number_windows_open=0, number_plugs=0, number_plugs_on=0,
                                      litter_items=0,
                                      image=tempfile.NamedTemporaryFile(
                                          suffix=".gif").name
                                      )
            testSub.save()
            pass

        except:
            self.fail("Can't save an image file with a .gif format")

    def test_png_format_can_be_created(self):
        """ Tests the png file extension is accepted in image submission. """
        try:
            testSub = ImageSubmission(building="testBuilding", room="testRoom",
                                      number_of_lights=0, number_lights_on=0, number_of_windows=0,
                                      number_windows_open=0, number_plugs=0, number_plugs_on=0,
                                      litter_items=0,
                                      image=tempfile.NamedTemporaryFile(
                                          suffix=".png").name
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
    room: RoomModel
    new_room: RoomModel
    existing_room: RoomModel
    sample_submission: ImageSubmission

    def setUp(self):
        """Create a room for use"""
        self.room = RoomModel(building="Test Building", name="testroom")
        self.room.save()

        self.new_room = RoomModel(building="Test Building", name="newroom", number_of_lights=10,
                                  number_of_windows=10, number_plugs=10, number_submissions=1)
        self.new_room.save()

        self.existing_room = RoomModel(building="Test Building", name="existingroom", number_of_lights=10,
                                       number_lights_on=1, number_of_windows=10, number_windows_open=1,
                                       number_plugs=10, number_plugs_on=1, litter_items=1, number_submissions=5)
        self.existing_room.save()

        self.sample_submission = ImageSubmission(building="testBuilding", room="testRoom",
                                                 number_of_lights=0, number_lights_on=0, number_of_windows=0,
                                                 number_windows_open=0, number_plugs=0, number_plugs_on=0,
                                                 litter_items=0,
                                                 image=tempfile.NamedTemporaryFile(
                                                     suffix=".jpg").name
                                                 )

    def test_room_created_with_0_vals(self):
        """Test default vals for all stats is 0"""
        room = RoomModel.objects.get(building="Test Building", name="testroom")
        self.assertEqual(room.number_of_lights, 0)
        self.assertEqual(room.number_lights_on, 0)
        self.assertEqual(room.number_of_windows, 0)
        self.assertEqual(room.number_windows_open, 0)
        self.assertEqual(room.number_plugs, 0)
        self.assertEqual(room.number_plugs_on, 0)
        self.assertEqual(room.litter_items, 0)
        self.assertEqual(room.number_submissions, 0)

    def test_get_statistics_deals_with_incorrect_room_name_error(self):
        """Tests the get statistics function returns None if no room model created"""
        stats = get_statistics("incorrect", "incorrect")
        self.assertIsNone(stats)

    def test_get_statistics_returns_stats_for_new_room(self):
        """Test correct stats returned for new room"""
        stats = get_statistics(room_name="testroom", building="Test Building")
        self.assertEqual(stats['lights'], 0)
        self.assertEqual(stats['windows'], 0)
        self.assertEqual(stats['plugs'], 0)
        self.assertEqual(stats['submissions'], 0)

    def test_get_statistics_returns_correct_stats_for_existing(self):
        """Test correct stats returned for existing room"""
        stats = get_statistics(room_name="existingroom",
                               building="Test Building")
        self.assertEqual(stats['lights'], 10)
        self.assertEqual(stats['windows'], 10)
        self.assertEqual(stats['plugs'], 10)
        self.assertEqual(stats['submissions'], 5)

    def test_statistics_valid_normalises_room_name(self):
        """Makes sure statistics_valid lowercases room name when searching"""
        existing_submission = ImageSubmission(building="Test Building", room="existingRoom",
                                              number_of_lights=10, number_lights_on=0, number_of_windows=10,
                                              number_windows_open=0, number_plugs=10, number_plugs_on=0,
                                              litter_items=0,
                                              image=tempfile.NamedTemporaryFile(
                                                  suffix=".jpg").name
                                              )
        res = statistics_valid(existing_submission, False)
        self.assertEquals(res, "valid")

    def test_statistics_valid_if_no_stats_for_room(self):
        """Makes sure is valid submission if no stats and adds to stats"""
        new_submission = ImageSubmission(building="Test Building", room="newroom1",
                                         number_of_lights=5, number_lights_on=5, number_of_windows=5,
                                         number_windows_open=5, number_plugs=5, number_plugs_on=5,
                                         litter_items=5,
                                         image=tempfile.NamedTemporaryFile(
                                                  suffix=".jpg").name
                                         )
        res = statistics_valid(new_submission, False)
        self.assertEquals(res, "valid")

    def test_statistics_valid_if_stats_same_as_enetered(self):
        """Tests valid if expected stats and added to room"""
        existing_submission = ImageSubmission(building="Test Building", room="existingroom",
                                              number_of_lights=10, number_lights_on=5, number_of_windows=10,
                                              number_windows_open=5, number_plugs=10, number_plugs_on=5,
                                              litter_items=5,
                                              image=tempfile.NamedTemporaryFile(
                                                  suffix=".jpg").name
                                              )
        res = statistics_valid(existing_submission, False)
        self.assertEquals(res, "valid")

    def test_invalid_stats_if_multiple_submissions_and_incorrect(self):
        """Tests statistics not valid if different data to multiple correct entries"""
        existing_submission = ImageSubmission(building="Test Building", room="existingroom",
                                              number_of_lights=10, number_lights_on=0, number_of_windows=10,
                                              number_windows_open=0, number_plugs=9, number_plugs_on=0,
                                              litter_items=0,
                                              image=tempfile.NamedTemporaryFile(
                                                  suffix=".jpg").name
                                              )
        res = statistics_valid(existing_submission, False)
        self.assertEquals(res, "invalid")

    def test_tells_user_to_check_if_different(self):
        """Tests if a user should repeat their count"""
        existing_submission = ImageSubmission(building="Test Building", room="newroom",
                                              number_of_lights=10, number_lights_on=0, number_of_windows=10,
                                              number_windows_open=0, number_plugs=9, number_plugs_on=0,
                                              litter_items=0,
                                              image=tempfile.NamedTemporaryFile(
                                                  suffix=".jpg").name
                                              )
        res = statistics_valid(existing_submission, False)
        self.assertEquals(res, "check")

    def test_if_repeat_is_valid(self):
        """Tests if repeat has been valid and that stats are reset"""
        existing_submission = ImageSubmission(building="Test Building", room="newroom",
                                              number_of_lights=10, number_lights_on=5, number_of_windows=10,
                                              number_windows_open=5, number_plugs=9, number_plugs_on=5,
                                              litter_items=5,
                                              image=tempfile.NamedTemporaryFile(
                                                  suffix=".jpg").name
                                              )
        res = statistics_valid(existing_submission, True)
        self.assertEquals(res, "valid_repeat")

    def test_input_stats_changes_stats_if_valid_input(self):
        """Tests stats are change if is a valid entry to input_stats"""
        existing_submission = ImageSubmission(building="Test Building", room="existingroom",
                                              number_of_lights=10, number_lights_on=1, number_of_windows=10,
                                              number_windows_open=1, number_plugs=10, number_plugs_on=1,
                                              litter_items=1,
                                              image=tempfile.NamedTemporaryFile(
                                                  suffix=".jpg").name
                                              )
        res = input_stats(existing_submission, False)
        self.assertEquals(res, "complete")
        room = RoomModel.objects.get(
            name="existingroom", building="Test Building")
        self.assertEquals(room.litter_items, 2)
        self.assertEquals(room.number_lights_on, 2)
        self.assertEquals(room.number_windows_open, 2)
        self.assertEquals(room.number_plugs_on, 2)
        self.assertEquals(room.number_submissions, 6)

    def test_input_stats_asks_user_to_check(self):
        """Tests user is asked to check on stats if different"""
        existing_submission = ImageSubmission(building="Test Building", room="newroom",
                                              number_of_lights=10, number_lights_on=1, number_of_windows=10,
                                              number_windows_open=1, number_plugs=9, number_plugs_on=1,
                                              litter_items=1,
                                              image=tempfile.NamedTemporaryFile(
                                                  suffix=".jpg").name
                                              )
        res = input_stats(existing_submission, False)
        self.assertEquals(res, "check")

    def test_input_stats_returs_invalid_if_invalid_stats(self):
        """Tests user is asked to check on stats if different"""
        existing_submission = ImageSubmission(building="Test Building", room="existingroom",
                                              number_of_lights=10, number_lights_on=1, number_of_windows=10,
                                              number_windows_open=1, number_plugs=9, number_plugs_on=1,
                                              litter_items=1,
                                              image=tempfile.NamedTemporaryFile(
                                                  suffix=".jpg").name
                                              )
        res = input_stats(existing_submission, False)
        self.assertEquals(res, "invalid")

    def test_input_stats_resets_stats_if_incorrect(self):
        """Tests stats can be reset if incorrect"""
        existing_submission = ImageSubmission(building="Test Building", room="newroom",
                                              number_of_lights=2, number_lights_on=1, number_of_windows=2,
                                              number_windows_open=1, number_plugs=2, number_plugs_on=1,
                                              litter_items=1,
                                              image=tempfile.NamedTemporaryFile(
                                                  suffix=".jpg").name
                                              )
        res = input_stats(existing_submission, True)
        self.assertEquals(res, "complete")
        room = RoomModel.objects.get(
            name="newroom", building="Test Building")
        self.assertEquals(room.litter_items, 1)
        self.assertEquals(room.number_lights_on, 1)
        self.assertEquals(room.number_windows_open, 1)
        self.assertEquals(room.number_plugs_on, 1)
        self.assertEquals(room.number_submissions, 1)

        self.assertEquals(room.number_of_lights, 2)
        self.assertEquals(room.number_of_windows, 2)
        self.assertEquals(room.number_plugs, 2)
