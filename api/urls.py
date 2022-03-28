from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JourneyViewSet, PostViewSet, UserViewSet

router = DefaultRouter()

router.register(r'users', UserViewSet, basename="users")
router.register(r'posts', PostViewSet, basename="posts")
router.register(r'journeys', JourneyViewSet, basename="journeys")


urlpatterns = [
    path('', include(router.urls)),
]
