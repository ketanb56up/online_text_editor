from django.views.generic import CreateView, TemplateView

from .forms import UserForms


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
