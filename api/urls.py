from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlimentoViewSet, RegistroComidaViewSet

router = DefaultRouter()
router.register(r'alimentos', AlimentoViewSet)
router.register(r'registros', RegistroComidaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]