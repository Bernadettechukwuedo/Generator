from django.urls import path, include
from .views import PasswordGenerator, HealthCheckView

app_name = "password"
urlpatterns = [
    path("", PasswordGenerator.as_view(), name="Password_Generator"),
    path("health/", HealthCheckView.as_view(), name="health_check"),
]
