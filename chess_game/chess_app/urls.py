from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='chessboard'),  # '' means root path of this included URL
    path('chess/', views.index, name='chessboard'),  # optional if you want /chess too
]
