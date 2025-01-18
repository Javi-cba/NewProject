from rest_framework import routers
from .api import ClientViewSet

routers= routers.DefaultRouter()
routers.register('api',ClientViewSet,basename='client')

urlpatterns = routers.urls