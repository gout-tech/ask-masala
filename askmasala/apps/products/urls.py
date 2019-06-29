from django.conf.urls import url
from django.views.generic.base import TemplateView
from . import views
from django.urls import path
app_name = 'products'

urlpatterns = [
                path('product-list/', views.ProductListView.as_view(), name='products'),
                path('product-details/<int:pk>', views.ProductDetailView.as_view(), name="product_details"),
                path('product-list/<int:pk>', views.ProductFilterView.as_view(), name='product_filter_list'),


]
