from rest_framework.routers import DefaultRouter
from users.api.views import CustomerApiViewSet, ComidaApiViewSet, BebidaApiViewSet, PedidoApiViewSet

router_users = DefaultRouter()


router_users.register(prefix='users', basename='users', viewset=CustomerApiViewSet)
router_users.register(prefix='comida', basename='comida', viewset=ComidaApiViewSet)
router_users.register(prefix='bebidas', basename='bebidas', viewset=BebidaApiViewSet)
router_users.register(prefix='pedido', basename='pedido', viewset=PedidoApiViewSet)
