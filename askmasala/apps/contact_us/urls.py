from . import views
from django.urls import path

app_name = 'contact_us'

urlpatterns = [
                path('', views.ContactUsView.as_view(), name='contact_us'),
]
