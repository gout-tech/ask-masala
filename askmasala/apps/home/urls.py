from django.conf.urls import url
from django.views.generic.base import TemplateView
from . import views
from django.urls import path
app_name = 'home'

urlpatterns = [
                path('', views.Slider.as_view(), name='slider'),



]
