from rest_framework import routers
from .views import BrandViewSet

router = routers.DefaultRouter()
router.register(r'brand', BrandViewSet)

urlpatterns = router.urls