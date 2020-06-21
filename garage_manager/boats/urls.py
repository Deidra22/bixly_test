from rest_framework import routers
from garage_manager.api import BoatViewSet

router = routers.DefaultRouter()
router.register('api/boats', BoatViewSet, 'boats' )

urlpatterns = router.urls