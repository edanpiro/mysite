# -*- coding: utf-8 *-*
__prj__ = '1.0.0'
__version__ = ''
__license__ = 'GNU General Public License v3'
__author__ = 'marcelo martinovic'
__email__ = 'marcelo.martinovic@gmail.com'
__url__ = ''
__date__ = "2013-10-20"
__updated__ = "2013-10-27"

from django.conf.urls import patterns, url

from polls import views
from django.views.generic import DetailView, ListView
from polls.models import Poll

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
#     url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
#     url(r'^(?P<poll_id>\d+)/verPost/$', views.verPost, name='verPost'),
)
