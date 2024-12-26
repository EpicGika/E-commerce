from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProductViewSet, CategoryViewSet, OrderViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter()

router.register('users', UserViewSet)
router.register('products', ProductViewSet)
router.register('Categories', CategoryViewSet)
router.register('orders', OrderViewSet)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
] 

urlpatterns += router.urls
