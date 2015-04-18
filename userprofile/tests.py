from django.test import TestCase
from userprofile.models import UserProfile
from django.contrib.auth.models import User

# Create your tests here.


class UserProfileTestCase(TestCase):
    # the User id matches with the corresponding UserProfile id
    def test_profile_belongs_to_user(self):
        test_user = User.objects.create(username="test_user", password="1234", email="test_user@internet.com")
        test_profile = UserProfile.objects.create(user=test_user, first_name="test", last_name="user",
                                                  gender='F', age=22, weight=120)
        self.assertEqual(test_profile.user_id, test_user.id)