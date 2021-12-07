from django.urls import path

from .views import Register, Success

urlpatterns = [
    path('register', Register.as_view(), name="register_user"),
    path('success', Success.as_view(), name="Success"),
]
