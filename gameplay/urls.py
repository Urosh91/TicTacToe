from django.urls import path

from .views import game_detail, make_move


urlpatterns = [
    path(r'detail/<int:id>/', game_detail, name="gameplay_detail"),
    path(r'make_move/<int:id>', make_move, name="gameplay_make_move")
]
