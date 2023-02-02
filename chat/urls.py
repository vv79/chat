from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import (
    HomePage,
    UserList,
    UserDetail,
    RoomList,
    RoomSearch,
    RoomDetail
)


urlpatterns = [
   path('', HomePage.as_view(), name='homepage'),
   path('users/', UserList.as_view(), name='user_list'),
   path('users/<pk>/', UserDetail.as_view(), name='user_detail'),
   path('rooms/', RoomList.as_view(), name='room_list'),
   path('rooms/search/', login_required(RoomSearch.as_view()), name='room_search'),
   path('rooms/<slug:slug>/', login_required(RoomDetail.as_view()), name='room_detail'),
   path('rooms/<slug:slug>/<str:username>/', login_required(RoomDetail.as_view()), name='room_detail_user')
]
