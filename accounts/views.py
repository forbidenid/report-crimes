from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from . models import User
from django.views.generic import CreateView, UpdateView, FormView, DetailView, View
from . forms import RegisterForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class Register(FormView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('accounts:dashboard'))



def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))

            else:
                return HttpResponse('<h2> Account Not Active </h2>')

        else:
            print('Someone tried to login failed on our site.')
            return HttpResponse('<h2>Invalid login credentials applied </h2>')

    else:
        return render(request, 'accounts/login.html', {})


class AccountSettings(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'bio', 'location', 'phone_no', 'profile_image']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, 'Your Account Settings were updated successfully!')
        return reverse('accounts:dashboard')


class Dashboard(LoginRequiredMixin, View):
    template_name = 'accounts/dashboard.html'

    def get(self, request, *args, **kwargs):
        user_object = User.objects.get(pk=request.user.id)
        return render(request, self.template_name, {'object': user_object})










