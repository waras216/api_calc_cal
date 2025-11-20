from rest_framework import serializers
from .models import *

class FoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foods
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class MealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meals
        fields = '__all__'


class DetailsMealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailsMeals
        fields = '__all__'


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = '__all__'


class DailyGoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyGoals
        fields = '__all__'


class PlanesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planes
        fields = '__all__'


class ImagenAnalisisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenAnalisis
        fields = '__all__'


class ProveedoresAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProveedoresAuth
        fields = '__all__'