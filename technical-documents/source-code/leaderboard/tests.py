""" Outlines the tests classes and methods to be used for the leaderboard
app.
"""
import tempfile
from django.test import Client, TestCase
from django.test.client import RequestFactory
from django.urls import reverse
from accounts.models import CustomUser
from submission.models import ImageSubmission
from leaderboard.models import BuildingModel
from leaderboard.views import leaderboard
from leaderboard.co2_calcs import get_co2


class LeaderboardTestCase(TestCase):
    """ The test cases to make sure the leaderboard doesn't crash

    Args:
        TestCase (TestCase): The test case object to test the submission
        models with.
    """

    def setUp(self):
        self.client = Client()

    def test_leaderboard_can_handle_no_users(self) -> None:
        """ Tests the leaderboard loads with no users on it. """
        # Creates somewhere to request the leaderboard
        rf = RequestFactory()
        url = reverse('leaderboard')
        request = rf.get(url)
        request.user = CustomUser(username="testUser",
                                  email="test@exeter.ac.uk", password="password")
        res = leaderboard(request)
        # Check page loaded correctly
        self.assertEqual(res.status_code, 200)

    def test_leaderboard_can_handle_one_user(self) -> None:
        """ Tests the leaderboard loads with one user on it. """
        # Create one user
        user = CustomUser(username="testUser",
                          email="test@exeter.ac.uk", password="password", points=1)
        user.save()
        # Creates somewhere to request the leaderboard
        rf = RequestFactory()
        url = reverse('leaderboard')
        request = rf.get(url)
        request.user = CustomUser(username="testUser",
                                  email="test@exeter.ac.uk", password="password")
        res = leaderboard(request)
        # Check page loaded correctly
        self.assertEqual(res.status_code, 200)

    def test_leaderboard_can_handle_two_users(self) -> None:
        """ Tests the leaderboard loads with two users on it. """
        # Create two users
        user1 = CustomUser(username="testUser1",
                           email="test1@exeter.ac.uk", password="password", points=1)
        user1.save()
        user2 = CustomUser(username="testUser2",
                           email="test2@exeter.ac.uk", password="password", points=1)
        user2.save()
        # Creates somewhere to request the leaderboard
        rf = RequestFactory()
        url = reverse('leaderboard')
        request = rf.get(url)
        request.user = CustomUser(username="testUser",
                                  email="test@exeter.ac.uk", password="password")
        res = leaderboard(request)
        # Check page loaded correctly
        self.assertEqual(res.status_code, 200)

    def test_leaderboard_can_handle_three_users(self) -> None:
        """ Tests the leaderboard loads with three users on it. """
        # Create three users
        user1 = CustomUser(username="testUser1",
                           email="test1@exeter.ac.uk", password="password", points=1)
        user1.save()
        user2 = CustomUser(username="testUser2",
                           email="test2@exeter.ac.uk", password="password", points=2)
        user2.save()
        user3 = CustomUser(username="testUser3",
                           email="test3@exeter.ac.uk", password="password", points=3)
        user3.save()
        # Creates somewhere to request the leaderboard
        rf = RequestFactory()
        url = reverse('leaderboard')
        request = rf.get(url)
        request.user = CustomUser(username="testUser",
                                  email="test@exeter.ac.uk", password="password")
        res = leaderboard(request)
        # Check page loaded correctly
        self.assertEqual(res.status_code, 200)

    def test_leaderboard_can_handle_many_users(self) -> None:
        """ Tests the leaderboard loads with three users on it. """
        # Create five users
        user1 = CustomUser(username="testUser1",
                           email="test1@exeter.ac.uk", password="password", points=1)
        user1.save()
        user2 = CustomUser(username="testUser2",
                           email="test2@exeter.ac.uk", password="password", points=1)
        user2.save()
        user3 = CustomUser(username="testUser3",
                           email="test3@exeter.ac.uk", password="password", points=1)
        user3.save()
        user4 = CustomUser(username="testUser4",
                           email="test4@exeter.ac.uk", password="password", points=1)
        user4.save()
        user5 = CustomUser(username="testUser5",
                           email="test5@exeter.ac.uk", password="password", points=1)
        user5.save()
        # Creates somewhere to request the leaderboard
        rf = RequestFactory()
        url = reverse('leaderboard')
        request = rf.get(url)
        request.user = CustomUser(username="testUser",
                                  email="test@exeter.ac.uk", password="password")
        res = leaderboard(request)
        # Check page loaded correctly
        self.assertEqual(res.status_code, 200)


class Co2CalculationsTestCase(TestCase):
    """ The test cases to ensure the CO2 calculations work as intended

    Args:
        TestCase (TestCase): The test case object to test the submission
        models with.
    """
    all_sub: ImageSubmission  # A submission with open windows and lights on
    windows_sub: ImageSubmission  # A submissiong with the windows open
    lights_sub: ImageSubmission  # A submission with the lights on
    no_sub: ImageSubmission  # An image submission with light off and windows closed

    def setUp(self):
        # Sets up all the objects required for the test functions
        self.all_sub = ImageSubmission(building="AMORY", room="existingroom",
                                       lights_status="ON",
                                       windows_status="OPEN",
                                       litter_items=0,
                                       image=tempfile.NamedTemporaryFile(
                                           suffix=".jpg").name
                                       )
        self.windows_sub = ImageSubmission(building="AMORY", room="existingroom",
                                           lights_status="OFF",
                                           windows_status="OPEN",
                                           litter_items=0,
                                           image=tempfile.NamedTemporaryFile(
                                               suffix=".jpg").name
                                           )

        self.lights_sub = ImageSubmission(building="AMORY", room="existingroom",
                                          lights_status="ON",
                                          windows_status="CLOSE",
                                          litter_items=0,
                                          image=tempfile.NamedTemporaryFile(
                                              suffix=".jpg").name
                                          )

        self.no_sub = ImageSubmission(building="AMORY", room="existingroom",
                                      lights_status="OFF",
                                      windows_status="CLOSE",
                                      litter_items=0,
                                      image=tempfile.NamedTemporaryFile(
                                          suffix=".jpg").name
                                      )

    def test_can_calculate_for_existing_building_with_lights_on_and_windows_open(self) -> None:
        """ Tests stats can be computed for a room with the windows open and lights on. """
        # Creates a test building
        building = BuildingModel(name="AMORY")
        building.save()

        co2 = get_co2(self.all_sub, "AMORY")
        self.assertAlmostEqual(co2, 0.1225406)

    def test_can_calculate_for_existing_building_with_lights_on(self) -> None:
        """ Tests stats can be computed for a room with the lights on. """
        # Creates a test building
        building = BuildingModel(name="AMORY")
        building.co2 = 0
        building.save()

        co2 = get_co2(self.lights_sub, "AMORY")
        self.assertAlmostEqual(co2, 0.03287675)

    def test_can_calculate_for_existing_building_with_windows_open(self) -> None:
        """ Tests stats can be computed for a room with the windows open. """
        # Creates a test building
        building = BuildingModel(name="AMORY")
        building.co2 = 0
        building.save()

        co2 = get_co2(self.windows_sub, "AMORY")
        self.assertAlmostEqual(co2, 0.08966387)

    def test_can_calculate_for_existing_building_with_lights_off_and_windows_closed(self) -> None:
        """ Tests stats can be computed for a room with windows closed and lights off. """
        # Creates a test building
        building = BuildingModel(name="AMORY")
        building.co2 = 0
        building.save()

        co2 = get_co2(self.no_sub, "AMORY")
        self.assertEqual(co2, 0)
