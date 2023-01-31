from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from .forms import BaseProfileForm
from django.contrib import messages
from django.urls import reverse_lazy


class UserProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = BaseProfileForm
    template_name = 'user/profile.html'

    def form_valid(self, form):
        messages.success(self.request, "Your profile was successfully updated.")

        return super().form_valid(form)

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('profile')
