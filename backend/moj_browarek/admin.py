from django.contrib import admin
from django.contrib import admin

from user.models import UserProfile
from user.forms import UserProfileForm

from beers.models import BeerModel


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    form = UserProfileForm


@admin.register(BeerModel)
class BeerModelAdmin(admin.ModelAdmin):
    pass