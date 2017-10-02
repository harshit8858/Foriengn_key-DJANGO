from django.conf.urls import url
from django.contrib import admin
from vapp.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^pub_form/', pub_form, name='pub_form'),
    url(r'^book_form/', book_form, name='book_form'),
]
