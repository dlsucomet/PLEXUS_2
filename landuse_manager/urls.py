from django.conf.urls import url
from . import views

app_name = 'landuse_manager'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^manage/(?P<filename>.+.(geojson|json))/$', views.manage, name='manage'),
    url(r'^manage/(?P<filename>.+.(geojson|json))/save/$', views.manageSave, name="manageSave"),
    url(r'^choose/$', views.choose, name='choose'),
]