from . import views
from django.conf.urls import url
from django.urls import path


app_name = 'subscription'

urlpatterns = [
                path('base/', views.SubscriptionView.as_view(), name='subs'),
]
