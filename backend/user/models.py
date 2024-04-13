from django.db import models
from django.contrib.auth.models import User
from django.core import validators, exceptions
import datetime


def validate_birth_date(birth_date):
    today = datetime.date.today()
    age = (today - birth_date).days / 365
    if age < 18:
        raise exceptions.ValidationError("Użytkownik musi być pełnoletni")


class UserProfile(models.Model):
    """
    Default User model contain: username, password, email, first_name, last_name.
    Extended by:
        - weight
        - height
        - birthdate
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weight = models.FloatField(blank=True, null=True, validators=[validators.MinValueValidator(0), validators.MaxValueValidator(610)])
    height = models.FloatField(blank=True, null=True, validators=[validators.MinValueValidator(0), validators.MaxValueValidator(251)])
    birthDate = models.DateField(default=datetime.date.today(), blank=False, validators=[validate_birth_date])

    def __str__(self):
        return {UserProfile.user}
