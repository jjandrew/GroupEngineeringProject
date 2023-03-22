""" Outlines the tests for the submission page. """
import tempfile
from datetime import datetime
from django.test import TestCase
from gkHomepage.crowd_source import input_stats
from submission.models import ImageSubmission, RoomModel


class ImageSubmissionTestCase(TestCase):
    """ Declares each of the tests for the submission section of the website.

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


class RoomSubmissionTestCase(TestCase):
    """ Declares each of the tests for the room submission section of the submission.

    Args:
        TestCase: The Django test object to be used to test the submission page.
    """
    existing_room: RoomModel

    def setUp(self):
        """ Create a room for use. """
        self.existing_room = RoomModel(building="Test Building", name="existingroom",
                                       number_lights_on=5, number_windows_open=5,
                                       litter_items=5, number_submissions=5)
        self.existing_room.save()

    def test_input_stats_changes_stats_if_on_and_open(self):
        """ Tests stats are changed if windows open and lights on. """
        existing_submission = ImageSubmission(building="Test Building",
                                              room="existingroom",
                                              lights_status="ON",
                                              windows_status="OPEN",
                                              litter_items=1,
                                              image=tempfile.NamedTemporaryFile(
                                                  suffix=".jpg").name
                                              )
        input_stats(existing_submission)
        room = RoomModel.objects.get(
            name="existingroom", building="Test Building")
        self.assertEqual(room.number_lights_on, 6)
        self.assertEqual(room.number_windows_open, 6)
        self.assertEqual(room.litter_items, 6)
        self.assertEqual(room.number_submissions, 6)

        # Reset existing room
        self.existing_room = RoomModel(building="Test Building", name="existingroom",
                                       number_lights_on=5, number_windows_open=5,
                                       litter_items=5, number_submissions=5)
        self.existing_room.save()

    def test_input_stats_dont_change_if_closed_and_off(self):
        """ Tests stats don't change if windows closed and lights off. """
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
        self.assertEqual(room.number_lights_on, 5)
        self.assertEqual(room.number_windows_open, 5)
        self.assertEqual(room.litter_items, 5)
        self.assertEqual(room.number_submissions, 6)

        # Reset existing room
        self.existing_room = RoomModel(building="Test Building", name="existingroom",
                                       number_lights_on=5, number_windows_open=5,
                                       litter_items=5, number_submissions=5)
        self.existing_room.save()

    def test_input_stats_dont_change_if_automatic(self):
        """ Tests stats don't change if windows and lights are automatic. """
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
        self.assertEqual(room.number_lights_on, 5)
        self.assertEqual(room.number_windows_open, 5)
        self.assertEqual(room.litter_items, 5)
        self.assertEqual(room.number_submissions, 6)

        # Reset existing room
        self.existing_room = RoomModel(building="Test Building", name="existingroom",
                                       number_lights_on=5, number_windows_open=5,
                                       litter_items=5, number_submissions=5)
        self.existing_room.save()
