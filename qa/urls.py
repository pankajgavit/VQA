from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'qa'


urlpatterns = [
    #/home/
    url(r'^question/$', views.home),
    url(r'^answer/$', views.answer),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)