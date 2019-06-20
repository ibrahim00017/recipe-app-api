from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_email(self):
        email = "ibres@gmail.com"
        password = "test12345"
        user = get_user_model().objects.create_user(
            email = email, 
            password = password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """ Test the email for a new user is normalize"""
        email = 'ibres@GMAIL.com'
        user = get_user_model().objects.create_user(email, 'test12345')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating email with no email raise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test12345")

    def test_create_new_super_user(self):
        """ Test creating a new super user"""
        user = get_user_model().objects.create_superuser(
            "ibre@gmail.com",
            "test12345"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
