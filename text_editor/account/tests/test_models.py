from account.models import User, UserCredit, MachineInformation
from django.test import TestCase


class TestAccountModels(TestCase):
    """
    TestAccountModels
        A test class for testing account app models
    """

    @classmethod
    def setUpTestData(cls):
        """
            Set up non-modified objects used by all test methods
        """
        User.objects.create(
            first_name='Big',
            last_name='Bob',
            email="one@gmail.com",
            username="bobby",
            password="one234five",
            contact=6897564123,
            user_agent="test_user_agent"
        )

    def test_contact_name_label(self):
        """
            Testing contact label name of user model
        """
        user = User.objects.all().first()
        field_label = user._meta.get_field('contact').verbose_name
        self.assertEqual(field_label, 'Mobile Number')

    def test_get_user(self):
        """
            Testing User object created in setup method or its First name
        """
        user = User.objects.all().first()
        self.assertEqual(user.first_name, "Big")

    def test_get_user_credit_by_user(self):
        """
             Testing user`s credits by new user's instance and also
             matching value of credit
        """
        user = User.objects.all().first()
        user_credit = UserCredit.objects.get(user=user)
        self.assertNotEqual(user_credit, None)
        self.assertEqual(user_credit.total_credit, 5)

    def test_get_machine_information_by_user_agent(self):
        """
            Testing Machine Information`s object by
            the user agent information
        """
        user = User.objects.all().first()
        machine_information = MachineInformation.objects.get(
            user_agent=user.user_agent
        )
        self.assertNotEqual(machine_information, None)
