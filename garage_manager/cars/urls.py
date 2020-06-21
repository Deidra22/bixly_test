from rest_framework import routers
from garage_manager.api import CarViewSet

router = routers.DefaultRouter()
router.register('api/cars', CarViewSet, 'cars' )

urlpatterns = router.urls