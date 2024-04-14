from django.contrib import admin
from .models import UserProfile
from django.contrib import admin
from .forms import UserProfileForm


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    form = UserProfileForm
