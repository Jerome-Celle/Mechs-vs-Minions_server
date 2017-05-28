from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('mvm_server.mvm_server_app.urls')),
]