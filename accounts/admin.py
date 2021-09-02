from django.contrib import admin
from .models import Membership_Profile
from django.contrib.auth.models import Group
# Register your models here.

admin.site.register(Membership_Profile)
admin.site.unregister(Group)