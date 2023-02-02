from django.views.generic import TemplateView, ListView, DetailView, RedirectView
from .models import Room, RoomUser
from django.shortcuts import resolve_url
from django.contrib.auth.models import User
from django.db.models import Q


class HomePage(TemplateView):
    template_name = 'chat/homepage.html'


class RoomList(ListView):
    model = Room
    ordering = '-title'
    template_name = 'chat/room_list.html'
    context_object_name = 'room_list'
    queryset = Room.objects.all()
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user
        queryset = Room.objects.filter(users__id=user.id)

        return queryset


class RoomSearch(RedirectView):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_redirect_url(self, **kwargs):
        user = self.request.user
        room_title = self.request.GET['title']

        room = Room.objects.filter(title=room_title).first()

        if not room:
            room = Room.objects.create(title=room_title)
            room.save()

        return resolve_url('room_detail', slug=room.slug)


class RoomDetail(DetailView):
    model = Room
    template_name = 'chat/room.html'
    context_object_name = 'room'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        room = context['room']

        room_user = RoomUser.objects.filter(room=room.id, user=user.id)

        if not room_user:
            room_user = RoomUser.objects.create(room=room, user=user)
            room_user.save()

        context['room_users'] = RoomUser.objects.filter(room=room.id).exclude(user=user.id)
        context['sender'] = user

        receiver_username = self.kwargs.get('username')

        if receiver_username:
            context['receiver'] = User.objects.get(username=receiver_username)

        return context

    def get_object(self, *args, **kwargs):
        return super().get_object(queryset=self.queryset)


class UserList(ListView):
    model = User
    ordering = '-username'
    template_name = 'chat/user_list.html'
    context_object_name = 'user_list'
    queryset = User.objects.filter(groups__name='common')
    paginate_by = 10


class UserDetail(DetailView):
    model = User
    template_name = 'chat/user.html'
    context_object_name = 'user'
