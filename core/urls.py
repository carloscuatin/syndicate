from rest_framework.routers import DefaultRouter
from core.views import ProductViewSet, PurchaseViewSet, InvestorViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, base_name='products')
router.register(r'investors', InvestorViewSet, base_name='investors')
router.register(r'purchases', PurchaseViewSet, base_name='purchases')

urlpatterns = router.urls
