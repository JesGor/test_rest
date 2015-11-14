from django.conf.urls import url
from apprest import views

urlpatterns = [
    url(r'^$', views.lista_empresas),
    url(r'^empresas/(?P<pk>[0-9]+)/$', views.empresa),
]
