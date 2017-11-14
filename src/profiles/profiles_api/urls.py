from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
"""
Register a model viewset, don't need to specify the base name because
Django REST framework can automatically figure this out by looking at the
model that's registered with the serializer that's registered on our viewsets.
"""
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
    url(r'', include(router.urls))
]