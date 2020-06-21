from rest_framework import routers
from garage_manager.api import TruckViewSet

router = routers.DefaultRouter()
router.register('api/trucks', TruckViewSet, 'trucks' )

urlpatterns = router.urls