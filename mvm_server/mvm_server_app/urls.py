from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from mvm_server.mvm_server_app import views

urlpatterns = [
    url(r'^minions/$', views.MinionList.as_view()),
    url(r'^minions/(?P<pk>[0-9]+)/$', views.MinionDetail.as_view()),
    url(r'^minions/(?P<pk>[0-9]+)/move/(?P<pMove>[0-9]+)/$', views.MinionMove.as_view()),

    url(r'^case_huiles/$', views.CaseHuileList.as_view()),
    url(r'^case_huiles/(?P<pk>[0-9]+)/$', views.CaseHuileDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
