from django.conf.urls import url
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^$', views.apiOverview, name='apioverview'),
    url(r'^all-movie/$', views.AllMovie, name='all-movie'),
    url(r'^get-movie/(?P<pk>\d+)/$', views.GetMovie, name='get-movie'),
    url(r'^post-movie/$', views.PostMovie, name='post-movie'),
    url(r'^update-movie/(?P<pk>\d+)/$', views.UpdateMovie, name='update-movie'),
    url(r'^delete-movie/(?P<pk>\d+)/$', views.DeleteMovie, name='delete-movie'),
    url(r'^user-login/$', obtain_auth_token, name='user-login'),
]