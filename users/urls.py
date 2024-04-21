from django.urls import path
from . import views

urlpatterns = [
  path('register/', views.registry, name='registry'),
  path("login/", views.login_view, name="login")
]