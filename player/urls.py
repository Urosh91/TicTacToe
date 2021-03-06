from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import home, new_invitation, accept_invitation, register_view

urlpatterns = [
    path(r'home', home, name="player_home"),
    path(r'register', register_view,  name="player_registration"),
    path(r'login', LoginView.as_view(template_name="player/login_form.html"), name="player_login"),
    path(r'logout', LogoutView.as_view(), name="player_logout"),
    path(r'new_invitation', new_invitation, name="player_new_invitation"),
    path(r'accept_invitation/<int:id>/', accept_invitation, name="player_accept_invitation")
]