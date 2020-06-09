from django.conf.urls import url
from .views import hello, index, search_form, search, login,login_pages,login_pages2,login2

urlpatterns = [
    url(r'^hello/$', hello),
    url(r'^index/$', index),
    url(r'^search_form/$', search_form),
    url(r'^search/$', search),
    url(r'^login.html/$', login_pages),
    url(r'^login.html2/$', login_pages2),
    url(r'^login/$', login),
    url(r'^login2/$', login2),
]
