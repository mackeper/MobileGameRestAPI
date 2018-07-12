from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from score import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'score', views.ScoreViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]