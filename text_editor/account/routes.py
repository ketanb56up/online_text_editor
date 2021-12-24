from django.urls import path

from .views import Register, Success, UsersByUsername

urlpatterns = [
    path("register", Register.as_view(), name="register_user"),
    path("success", Success.as_view(), name="Success"),
    path("user_list/<username>", UsersByUsername.as_view(), name="user_list"),
]
