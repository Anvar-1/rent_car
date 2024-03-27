from rest_framework import routers
from .views import CarViewSet

router = routers.DefaultRouter()
router.register(r'cars', CarViewSet)

urlpatterns = router.urls