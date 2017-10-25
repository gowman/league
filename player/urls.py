from django.conf.urls import url
from player import views

urlpatterns = [
    url(r'^player/$', views.player_list)
]
