from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuteurViewSet, LivreViewSet, EmpruntViewSet

router = DefaultRouter()
router.register('auteurs', AuteurViewSet)
router.register('livres', LivreViewSet)
router.register('emprunts', EmpruntViewSet)

urlpatterns = [
    path('', include(router.urls)),
]