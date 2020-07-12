from rest_framework import serializers

from core.models import Tag, Ingredient, Recipie


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for the Ingredient Model"""
    
    class Meta:
        model = Ingredient
        fields = ('id', 'name',)
        read_only_fields = ('id',)


class RecipieSerializer(serializers.ModelSerializer):
    """Seriaze a recipie"""
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Ingredient.objects.all()
    )
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )
    
    class Meta:
        model = Recipie
        fields = ('id', 'title', 'ingredients', 'tags', 'time_miniutes',
                  'price', 'link')
        read_only_fields = ('id',)


class RecipieDetailSerializer(RecipieSerializer):
    """Serialize a recipie detail"""
    ingredients = IngredientSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    