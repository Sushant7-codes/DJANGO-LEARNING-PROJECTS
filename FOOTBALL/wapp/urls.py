from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('players/', views.Player, name='players'),
    path('Football/', views.Football, name='Football'),
    path('players/<int:player_id>/', views.Player, name='player_id'), # path('players/<player_name/view/', views.Player, name='player_name_view'),
]
