from django.shortcuts import render
from apps.home.models import Images
from apps.testimonial.models import Testimonial
from apps.clients.models import Clients
from apps.about_us.models import About
from apps.products.models import Products, Categories
from django.views.generic import ListView


# Create your views here.
class Slider(ListView):
    template_name = 'home/home.html'
    context_object_name = 'product_list'
    paginate_by = 8

    def get_queryset(self):
        queryset = Products.objects.filter(availability=True)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(Slider, self).get_context_data(*args, **kwargs)
        context['home_slider'] = Images.objects.all()
        context['category'] = Categories.objects.all()
        context['testimonial'] = Testimonial.objects.filter(is_published=True)
        context['clients'] = Clients.objects.filter(is_published=True)
        context['about_us'] = About.objects.filter(is_published=True)
        return context






