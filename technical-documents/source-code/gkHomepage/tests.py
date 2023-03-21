from django.test import TestCase

# Create your tests here.


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
