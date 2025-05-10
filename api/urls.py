from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet

from api.views import UserModelViewSet, HotelModelViewSet, RoomModelViewSet, BookingModelViewSet

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('hotels', HotelModelViewSet)
router.register('rooms', RoomModelViewSet)
router.register('bookings', BookingModelViewSet)

urlpatterns = [

]

urlpatterns.extend(router.urls)