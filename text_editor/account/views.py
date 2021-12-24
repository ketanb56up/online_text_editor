from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, TemplateView

from .forms import UserForms
from .models import User


class Register(CreateView):
    """
    Register
        class based view for user register/Signup form with help of CreateView,
        and for validating fields used UserForm class of account app.
    """

    form_class = UserForms
    success_url = "/account/success"
    template_name = "account/register.html"


class Success(TemplateView):
    """
    Success
        just rendering a template after creation of user
    """

    template_name = "account/success.html"


class UsersByUsername(View):
    """
    UsersByUsername:
        Get User list username and its fingerprint
        :param username
    """

    def get(self, request, username):
        # here we fetch requested user's information
        user = User.objects.filter(username=username)
        # here we fetch the list of accounts opened by the same person(user).
        user_list = (
            User.objects.filter(user_agent=user.first().user_agent) if user else None
        )
        if user_list:
            return render(
                request, "account/all_user.html", context={"users": user_list}
            )
        else:
            return redirect("/")
