from django.urls import path, include
from .views import PasswordGenerator

app_name = "password"
urlpatterns = [path("pass_gen/", PasswordGenerator.as_view(), name="PasswordGenerator")]
