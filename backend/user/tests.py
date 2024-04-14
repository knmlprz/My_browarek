from django.test import TestCase
from .models import UserProfile
from django.contrib.auth.models import User
from datetime import date
from django.core.exceptions import ValidationError


class UserProfileTest(TestCase):
    """
    UserProfile Model Tests:
    - Testing valid data
    - Testing invalid birthday
        - age of majority as minimum
        - future date
    - Testing invalid Weight
        - negative, 0
        - abnormaly high
    - Testing invalid Height
        - negative, 0
        - abnormally* high

    *abnormally means that there was never a person
    who's variable of data was at this extremum (Check Guissness Records etc.)
    """

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="T35t123!")
        self.valid_profile_data = {
            "user": self.user,
            "birthDate": date(2001, 6, 3),
            "height": 180.1,
            "weight": 80.5,
        }

    def test_valid_profile(self):
        valid_profile = UserProfile(**self.valid_profile_data)
        valid_profile.full_clean()

    def test_invalid_birthDate(self):
        invalid_profile_data = self.valid_profile_data.copy()

        # Age of majority Test
        invalid_profile_data["birthDate"] = date(2021, 4, 13)
        with self.assertRaises(ValidationError):
            profile = UserProfile(**invalid_profile_data)
            profile.full_clean()

        # Future date Test
        invalid_profile_data["birthDate"] = date(2058, 4, 13)
        with self.assertRaises(ValidationError):
            profile = UserProfile(**invalid_profile_data)
            profile.full_clean()

    def test_invalid_weight(self):
        invalid_profile_data = self.valid_profile_data.copy()

        # Abnormally negative weight Test
        invalid_profile_data["weight"] = -1.0
        with self.assertRaises(ValidationError):
            profile = UserProfile(**invalid_profile_data)
            profile.full_clean()

        # Abnormally zero weight Test
        invalid_profile_data["weight"] = 0.0
        with self.assertRaises(ValidationError):
            profile = UserProfile(**invalid_profile_data)
            profile.full_clean()

        # Abnormally high weight Test
        invalid_profile_data["weight"] = 1000.5
        with self.assertRaises(ValidationError):
            profile = UserProfile(**invalid_profile_data)
            profile.full_clean()

    def test_invalid_height(self):
        invalid_profile_data = self.valid_profile_data.copy()

        # Abnormally negative height Test
        invalid_profile_data["height"] = -1.0
        with self.assertRaises(ValidationError):
            profile = UserProfile(**invalid_profile_data)
            profile.full_clean()

        # Abnormally zero height Test
        invalid_profile_data["height"] = 0.0
        with self.assertRaises(ValidationError):
            profile = UserProfile(**invalid_profile_data)
            profile.full_clean()

        # Abnormally high height Test
        invalid_profile_data["height"] = 1000.5
        with self.assertRaises(ValidationError):
            profile = UserProfile(**invalid_profile_data)
            profile.full_clean()
