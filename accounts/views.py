from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from .models import CustomUser

class SignUpView(CreateView):
    model = CustomUser
    template_name = 'signup.html'
    fields = ['username', 'email', 'password', 'role', 'team']
    success_url = reverse_lazy('home')

class UserProfileView(DetailView):
    model = CustomUser
    template_name = 'profile.html'
    context_object_name = 'user'

    def get_object(self):
        return self.request.user