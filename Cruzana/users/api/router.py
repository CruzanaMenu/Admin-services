from rest_framework.routers import DefaultRouter
from users.api.views import CustomerApiViewSet

router_users = DefaultRouter()


router_users.register(prefix='users', basename='users', viewset=CustomerApiViewSet)