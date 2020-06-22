from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .api import CarViewSet
from .api import TruckViewSet
from .api import BoatViewSet


router = routers.DefaultRouter()
router.register(r'api/cars', CarViewSet)
router.register(r'api/trucks', TruckViewSet)
router.register(r'api/boats', BoatViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]