from rest_framework import routers
from .views import RoomViewSet, UserViewSet, MessageViewSet

router = routers.SimpleRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'users', UserViewSet)

urlpatterns = router.urls
