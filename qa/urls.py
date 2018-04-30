from django.conf.urls import url
from . import views

app_name = 'qa'


urlpatterns = [
    #/home/
    url(r'^question/$', views.home),
    url(r'^answer/$', views.answer),
]