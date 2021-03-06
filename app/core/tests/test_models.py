from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@closinbrace.com', password='testpass'):
    """Create a simple user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@closinbrace.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@CLOSINGBRACE.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'pass1234')

    def test_create_new_superuser(self):
        """Test Creating a new super user"""
        user = get_user_model().objects.create_superuser(
            'test@closingbrace.com',
            'test12345'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string """
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)
        
    def test_ingredient_str(self):
        """Test the ingredient string"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name="Carrots"
        )
        
        self.assertEqual(str(ingredient), ingredient.name)
    
    def test_recipie_str(self):
        """Test the Recipie String"""
        recipie = models.Recipie.objects.create(
            user=sample_user(),
            title="Meat Loaf",
            time_minutes=5,
            price=2.50
        )
        
        self.assertEqual(str(recipie), recipie.title)
