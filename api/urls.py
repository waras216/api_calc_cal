from rest_framework.routers import DefaultRouter
from .viewsets import (
    FoodsViewSet,
    UsersViewSet,
    MealsViewSet,
    DetailsMealsViewSet,
    FavoritesViewSet,
    DailyGoalsViewSet,
    PlanesViewSet,
    ImagenAnalisisViewSet,
    ProveedoresAuthViewSet
)

router = DefaultRouter()
router.register(r'foods', FoodsViewSet)
router.register(r'users', UsersViewSet)
router.register(r'meals', MealsViewSet)
router.register(r'details-meals', DetailsMealsViewSet)
router.register(r'favorites', FavoritesViewSet)
router.register(r'daily-goals', DailyGoalsViewSet)
router.register(r'planes', PlanesViewSet)
router.register(r'imagen-analisis', ImagenAnalisisViewSet)
router.register(r'proveedores-auth', ProveedoresAuthViewSet)

urlpatterns = router.urls
