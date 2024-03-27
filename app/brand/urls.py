from rest_framework import routers
from .views import BrandViewSet

router = routers.DefaultRouter()
router.register(r'brands', BrandViewSet)

urlpatterns = router.urls