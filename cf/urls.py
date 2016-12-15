from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views

app_name = 'cf'
urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^download/$', views.download, name='download'),
    url(r'^safe_box/(?P<pk>[0-9]+)/$', views.SafeBoxDetail.as_view(), name='safe_box'),
    url(r'^safe_box_list/$', views.SafeBoxList.as_view(), name='safe_box_list'),
    url(r'^key/(?P<pk>[0-9]+)/$', views.KeyDetail.as_view(), name='key'),
    url(r'^key_list/$', views.KeyList.as_view(), name='key_list'),
    url(r'^upload/$', views.model_form_upload, name='upload'),
    url(r'^new_safe_box/$', views.safe_box_form, name='new_safe_box'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
