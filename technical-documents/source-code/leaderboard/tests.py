from django.test import Client, TestCase
from django.test.client import RequestFactory
from django.urls import reverse
from .views import leaderboard
from accounts.models import CustomUser


class LeaderboardTestCase(TestCase):
    """The test cases to make sure the leaderboard doesn't crash """

    def setUp(self):
        self.client = Client()

    def test_leaderboard_can_handle_no_users(self):
        """Tests the leaderboard loads with no users on it"""
        # Creates somewhere to request the leaderboard
        rf = RequestFactory()
        url = reverse('leaderboard')
        request = rf.get(url)
        request.user = CustomUser(username="testUser",
                                  email="test@exeter.ac.uk", password="password")
        res = leaderboard(request)
        # Check page loaded correctly
        self.assertEqual(res.status_code, 200)

    def test_leaderboard_can_handle_one_user(self):
        """Tests the leaderboard loads with one user on it"""
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

    def test_leaderboard_can_handle_two_users(self):
        """Tests the leaderboard loads with two users on it"""
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

    def test_leaderboard_can_handle_three_users(self):
        """Tests the leaderboard loads with three users on it"""
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

    def test_leaderboard_can_handle_many_users(self):
        """Tests the leaderboard loads with three users on it"""
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
