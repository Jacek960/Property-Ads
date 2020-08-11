from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views import View
from django.views.generic import UpdateView

from accounts.forms import UserUpdateForm


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class UserProfile(LoginRequiredMixin, View):
    def get(self, request):
        user = User.objects.get(username=request.user)
        return render(request, 'accounts/user_profile.html', {'user': user})

class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'accounts/user_update_form.html'
    success_url = '/accounts/profil/'

    def get_object(self, queryset=None):
        return self.request.user