from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from authenticate.forms import EditForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
from django.shortcuts import render


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/account/login/"
    template_name = 'authenticate/signup.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "authenticate/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    success_url = "/"
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


def upload_file(request):
    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = EditForm()
    return render(request, 'authenticate/profile.html', {'form': form})
