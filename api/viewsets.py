from rest_framework import viewsets
from .models import Foods, Users, Meals, DetailsMeals, Favorites, DailyGoals, Planes, ImagenAnalisis, ProveedoresAuth
from .serializers import (
    FoodsSerializer, UserSerializer, MealsSerializer, DetailsMealsSerializer,
    FavoritesSerializer, DailyGoalsSerializer, PlanesSerializer,
    ImagenAnalisisSerializer, ProveedoresAuthSerializer
)

class FoodsViewSet(viewsets.ModelViewSet):
    queryset = Foods.objects.all()
    serializer_class = FoodsSerializer

    def get_queryset(self):
        queryset = Foods.objects.all()
        nombre = self.request.query_params.get('nombre')
        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)
        return queryset

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = Users.objects.all()
        nombre = self.request.query_params.get('nombre')
        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)
        return queryset



class MealsViewSet(viewsets.ModelViewSet):
    queryset = Meals.objects.all()
    serializer_class = MealsSerializer

    def get_queryset(self):
        queryset = Meals.objects.all()
        id_user = self.request.query_params.get('id_user')
        if id_user:
            queryset = queryset.filter(id_user=id_user)
        return queryset


class DetailsMealsViewSet(viewsets.ModelViewSet):
    queryset = DetailsMeals.objects.all()
    serializer_class = DetailsMealsSerializer

    def get_queryset(self):
        queryset = DetailsMeals.objects.all()
        id_meal = self.request.query_params.get('id_meal')
        if id_meal:
            queryset = queryset.filter(id_meal=id_meal)
        return queryset


class FavoritesViewSet(viewsets.ModelViewSet):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer

    def get_queryset(self):
        queryset = Favorites.objects.all()
        id_user = self.request.query_params.get('id_user')
        if id_user:
            queryset = queryset.filter(id_user=id_user)
        return queryset

class DailyGoalsViewSet(viewsets.ModelViewSet):
    queryset = DailyGoals.objects.all()
    serializer_class = DailyGoalsSerializer

    def get_queryset(self):
        queryset = DailyGoals.objects.all()
        id_user = self.request.query_params.get('id_user')
        if id_user:
            queryset = queryset.filter(id_user=id_user)
        return queryset


class PlanesViewSet(viewsets.ModelViewSet):
    queryset = Planes.objects.all()
    serializer_class = PlanesSerializer


class ImagenAnalisisViewSet(viewsets.ModelViewSet):
    queryset = ImagenAnalisis.objects.all()
    serializer_class = ImagenAnalisisSerializer

    def get_queryset(self):
        queryset = ImagenAnalisis.objects.all()
        id_user = self.request.query_params.get('id_user')
        if id_user:
            queryset = queryset.filter(id_user=id_user)
        return queryset


class ProveedoresAuthViewSet(viewsets.ModelViewSet):
    queryset = ProveedoresAuth.objects.all()
    serializer_class = ProveedoresAuthSerializer

    def get_queryset(self):
        queryset = ProveedoresAuth.objects.all()
        nombre = self.request.query_params.get('nombre')
        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)
        return queryset
