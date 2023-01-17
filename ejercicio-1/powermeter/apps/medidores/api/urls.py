from rest_framework import routers
from .views import MeasurerViewSet,MeasurementViewSet

router=routers.DefaultRouter()

router.register('api/measurer',MeasurerViewSet,'measurer')
router.register('api/measurement',MeasurementViewSet,'measurement')

urlpatterns = router.urls