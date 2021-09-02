
from django.db import models
import uuid
from django.dispatch import receiver
from django.contrib.auth.models import PermissionsMixin
from django.db.models.signals import post_save,pre_save
from django.utils.translation import gettext_lazy as _


class Membership_Profile(models.Model):
    first_name = models.CharField(max_length=250, null=False, help_text= 'Enter your first name ')
    last_name = models.CharField(max_length=250, null=False, help_text= 'Enter your last name ')
    email = models.EmailField(max_length=250, null= False, help_text= 'Enter your email to receive product updates, discounts and promo')
    gender_choice = (
        ("default","Default"),
        ( "M","Male"),
        ("F","Female"),
        ("O", "Others")

        )
    gender = models.CharField(max_length=7, choices= gender_choice)
    local_address = models.CharField(max_length=250, null=False, help_text= 'Enter your local address')
    state = models.CharField(max_length=250, null=False, help_text= 'Enter your state')