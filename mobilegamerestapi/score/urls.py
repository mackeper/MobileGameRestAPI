from django.conf.urls import url
from score import views

urlpatterns = [
    url(r'^scores/$', views.score_list),
    url(r'^scores/(?P<pk>[0-9]+)/$', views.score_detail),
]