from django.conf.urls import url, include
from rest_framework import routers

from .viewsets import RestaurantViewSet


router = routers.DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
