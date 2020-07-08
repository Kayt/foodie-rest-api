from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Ingedient

from recipie.serializers import IngredientSerializer


INGREDIENTS_URL = reverse('recipie:ingredient-list')


class PublicIngredientsAPITests(TestCase):
    """Test the publicly available ingredients"""
    
    def setUp(self):
        self.client = APIClient()