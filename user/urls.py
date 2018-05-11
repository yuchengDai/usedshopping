from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^register/',views.register),
    url(r'^handle_register/',views.handle_register),
    url(r'^login/',views.my_login),
    url(r'^userinfo/',views.Userinfo),
    url(r'^update/',views.update),
]