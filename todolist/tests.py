import datetime as dt

from django.test import TestCase
from users.models import Profile
from django.test.utils import setup_test_environment

# Create your tests here.


class TDitemModelTests(TestCase):
    def test_that_duedate_set_is_present_and_onwards(self):
        """ Test that the due date can't be set itno the past """
        today = dt.datetime.today()
        tomorow = today + dt.timedelta(days=1)
