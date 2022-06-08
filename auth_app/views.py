from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Users
from django.contrib.auth.views import LoginView

from .forms import UserRegisterForm, UserLoginForm


class AuthenticationUser(CreateView):
    template_name = "user_auth.html"
    form_class = UserRegisterForm

    def get_context_data(self, **kwargs):
        context = super(AuthenticationUser, self).get_context_data(**kwargs)
        context["login_form"] = UserLoginForm()
        return context

class UserLoginView(LoginView):
    form_class = UserLoginForm

    def render_to_response(self, context, **response_kwargs):
        messages.error(self.request, "Error Authorisation !")
        print(self.get_form().errors)
        return redirect("user_auth")

    def get_success_url(self):
        messages.success(self.request, "Authorisation has been successfull !")
        print(self.get_form().errors)
        return reverse_lazy("doctors")


class UserRegisterView(CreateView):
    form_class = UserRegisterForm

    def render_to_response(self, context, **response_kwargs):
        messages.error(self.request, "Error Register !")
        return redirect("register")

    def get_success_url(self):
        messages.success(self.request, "Registration has been successfull !")
        return reverse_lazy("user_auth")

class ProfileView(DetailView):
    model = Users
    template_name = "profile.html"
    context_object_name = "profile"


def user_logout(request):
    messages.success(request, "You have been successfully logout")
    logout(request)
    return redirect("user_auth")

class ProfileEditView(UpdateView):
    model = Users
    # , 'first_name', 'last_name', "username", 'email', "phone", "country", "city", "address"
    fields = ("image", )
    template_name = "profile_edit.html"
    context_object_name = "profile"

    def dispatch(self, *args, **kwargs):
        if self.request.user.pk != self.kwargs["pk"]:
            messages.error(self.request, "Permission Denied")
            return redirect("home")
        return super(ProfileEditView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        user = self.request.user
        return reverse_lazy("profile", kwargs={"pk": user.pk})
