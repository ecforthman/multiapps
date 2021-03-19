"""
from django.conf.urls import url

from hammingtests import views


urlpatterns = [
    url(r'^$', views.index, name='hammingtests_index'),
    url(r'^detail', views.detail, name='hammingtests_detail'),
    url('inform/', views.inform, name='hammingtests_inform'),
    url(r'^results', views.results, name='hammingtests_results'),
]
"""

from django.urls import path

# from django.conf.urls import url
from hammingtests import views

app_name = 'hammingtests'

urlpatterns = [
    path('', views.index, name='hammingtests_index'),
    path('detail', views.detail, name='hammingtests_detail'),
    path('inform/', views.inform, name='hammingtests_inform'),
    path('results', views.results, name='hammingtests_results'),
]
