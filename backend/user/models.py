from django.db import models
from django.contrib.auth.models import User
from django.core import validators, exceptions
from django.utils import timezone


def validate_birth_date(birth_date):
    """
    Validates if the user is at least 18 years old based on the birthdate.

    :param birth_date: The birthdate of the user.
    :raises ValidationError: If the user is not at least 18 years old.
    """
    today = timezone.now().date()
    age = (today - birth_date).days / 365
    if age < 18:
        raise exceptions.ValidationError("Użytkownik musi być pełnoletni")


class UserProfile(models.Model):
    """
    Extended user profile containing additional information.

    Attributes:
        user (User): The corresponding User object.
        weight (float): The weight of the user.
        height (float): The height of the user.
        birthDate (date): The birthdate of the user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weight = models.FloatField(blank=True, null=True, validators=[validators.MinValueValidator(0), validators.MaxValueValidator(610)])
    height = models.FloatField(blank=True, null=True, validators=[validators.MinValueValidator(0), validators.MaxValueValidator(251)])
    birthDate = models.DateField(default=timezone.now, blank=False, validators=[validate_birth_date])

    def __str__(self):
        return f"{self.user}"
