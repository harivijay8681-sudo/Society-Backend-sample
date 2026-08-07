from rest_framework.routers import DefaultRouter
from .views import ParkingViewSet

router = DefaultRouter()
router.register('', ParkingViewSet)

urlpatterns = router.urls
