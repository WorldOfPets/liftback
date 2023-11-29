import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

from lifts_app import models as lifts_app_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_lifts_app_frequently_used_lifts(**kwargs):
    defaults = {}
    if "lift" not in kwargs:
        defaults["lift"] = create_lifts_app_lift()
    defaults.update(**kwargs)
    return lifts_app_models.frequently_used_lifts.objects.create(**defaults)
def create_lifts_app_lift(**kwargs):
    defaults = {}
    defaults["vendor_code"] = ""
    defaults["is_booked"] = ""
    defaults["state"] = ""
    defaults["price"] = ""
    defaults.update(**kwargs)
    return lifts_app_models.lift.objects.create(**defaults)
def create_lifts_app_lift_images(**kwargs):
    defaults = {}
    defaults["image"] = ""
    if "lift" not in kwargs:
        defaults["lift"] = create_lifts_app_lift()
    defaults.update(**kwargs)
    return lifts_app_models.lift_images.objects.create(**defaults)
def create_lifts_app_lift_info(**kwargs):
    defaults = {}
    defaults["description"] = ""
    if "lift" not in kwargs:
        defaults["lift"] = create_lifts_app_lift()
    defaults.update(**kwargs)
    return lifts_app_models.lift_info.objects.create(**defaults)
def create_lifts_app_report(**kwargs):
    defaults = {}
    defaults["date"] = datetime.now()
    defaults["sales_amount"] = ""
    defaults["expenses"] = ""
    if "manager" not in kwargs:
        defaults["manager"] = create_lifts_app_CustomUser()
    if "requests" not in kwargs:
        defaults["requests"] = create_lifts_app_requests()
    if "frequently_used_lifts" not in kwargs:
        defaults["frequently_used_lifts"] = create_lifts_app_frequently_used_lifts()
    defaults.update(**kwargs)
    return lifts_app_models.report.objects.create(**defaults)
def create_lifts_app_requests(**kwargs):
    defaults = {}
    defaults["date_closed"] = datetime.now()
    defaults["price"] = ""
    defaults["date_booking"] = datetime.now()
    if "customer" not in kwargs:
        defaults["customer"] = create_lifts_app_CustomUser()
    if "manager" not in kwargs:
        defaults["manager"] = create_lifts_app_CustomUser()
    if "status" not in kwargs:
        defaults["status"] = create_lifts_app_status_request()
    if "reports" not in kwargs:
        defaults["reports"] = create_lifts_app_report()
    defaults.update(**kwargs)
    return lifts_app_models.requests.objects.create(**defaults)
def create_lifts_app_status_request(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults.update(**kwargs)
    return lifts_app_models.status_request.objects.create(**defaults)
def create_lifts_app_CustomUser(**kwargs):
    defaults = {}
    defaults["phone_number"] = ""
    defaults["second_name"] = ""
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    if "favorite_lifts" not in kwargs:
        defaults["favorite_lifts"] = create_lifts_app_lift()
    defaults.update(**kwargs)
    return lifts_app_models.CustomUser.objects.create(**defaults)
