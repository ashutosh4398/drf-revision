from rest_framework.routers import DefaultRouter

from .viewsets import ProductViewSet

router = DefaultRouter()
router.register('products-abc', ProductViewSet, basename="produ")

urlpatterns = router.urls
print(urlpatterns)