from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

from score import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^scores/$', 
        views.ScoreList.as_view(),
        name='score-list'),
    url(r'^scores/(?P<pk>[0-9]+)/$', 
        views.ScoreDetail.as_view(),
        name='score-detail'),
    url(r'^users/$', 
        views.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', 
        views.UserDetail.as_view(),
        name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')),
]