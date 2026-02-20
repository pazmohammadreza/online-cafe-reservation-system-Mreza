from django.urls import path
from .views import MenuView


app_name = 'menu'

urlpatterns = [
    path("menu/", MenuView.as_view(template_name="menu/menu.html"), name="menu"),
]