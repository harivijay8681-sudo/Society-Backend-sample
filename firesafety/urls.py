from rest_framework.routers import DefaultRouter
from .views import FireSafetyViewSet

router = DefaultRouter()
router.register('', FireSafetyViewSet)

urlpatterns = router.urls
