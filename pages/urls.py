from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('bgpict', views.PicturePageView.as_view(), name='bgpict'),
]