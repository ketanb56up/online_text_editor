from account.forms import UserForms
from django.test import TestCase


class TestUserForm(TestCase):
    """
        TestUserForm
            Test class for testing account's forms module
    """

    def test_user_create_form_valid(self):
        """
            testing User Form with a valid payload
        """
        data = {
            "username": "buntu",
            "first_name": "anand",
            "last_name": "prapti",
            "email": "as@gmail.com",
            "user_agent": "User_agent",
            "contact": 1236547890,
            "password1": "jldsjfl@?/13",
            "password2": "jldsjfl@?/13",

        }
        form = UserForms(data=data)
        self.assertTrue(form.is_valid())

    def test_user_create_form_invalid(self):
        """
            testing User Form with an invalid payload
        """
        data = {
            "username": "buntu",
            "first_name": "anand",
            "last_name": "prapti",
            "email": "as@gmail.com",
            "contact": 1236547890,
            "password2": "one234",
            "password1": "one234",

        }
        form = UserForms(data=data)
        self.assertFalse(form.is_valid())
