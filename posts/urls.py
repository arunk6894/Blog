from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.allposts, name = 'allposts'),
    path('<int:post_id>/',views.detail, name = 'detail'),
]