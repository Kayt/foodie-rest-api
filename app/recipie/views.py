from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag, Ingredient, Recipie
from recipie import serializers


class BaseRecipieAttrViewSet(viewsets.GenericViewSet,
                             mixins.ListModelMixin,
                             mixins.CreateModelMixin):
    """Base viewset for recipie attributes"""
    authentication_classes = (TokenAuthentication,)
    permisson_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        """Return objects for the current authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-name')
    
    def perform_create(self, serializer):
        """Create a new ingredient"""
        serializer.save(user=self.request.user)


class TagViewSet(BaseRecipieAttrViewSet):
    """Manage tags in the database"""

    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer


class IngredientViewSet(BaseRecipieAttrViewSet):
    """Manage ingredients in the databse"""
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer


class RecipieViewSet(viewsets.ModelViewSet):
    """Manage recipies in the databse"""
    queryset = Recipie.objects.all()
    seializer_class = serializers.RecipieSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        """Retrieve recipies for authenticated user"""
        return self.queryset.filter(user=self.request.user)
    
    def get_serializer_class(self):
        """Return appropriate serializer class"""
        if self.action == 'retrieve':
            return serializers.RecipieDetailSerializer
        return self.serializer_class
    
    def perform_create(self, serializer):
        """Create a new recipie"""
        serializer.save(user=self.request.user)