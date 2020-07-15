from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^panel/$', views.panel, name='panel'),
    url(r'^login/$', views.mylogin, name='mylogin'),
    url(r'^logout/$', views.mylogout, name='mylogout'),
    url(r'^panel/site/setting/$', views.site_setting, name='site_setting'),
    url(r'^panel/about/setting/$', views.about_setting, name='about_setting'),
    url(r'^panel/change/password/$', views.change_pass, name='change_pass'),
    url(r'^register/$', views.myregister, name='myregister'),
    url(r'^answer/cm/(?P<pk>\d+)/$', views.answer_cm, name='answer_cm'),
    url(r'^show/data/$', views.show_data, name='show_data'),
]