from django.views.generic import ListView
from apps.about_us.models import About


class AboutUs(ListView):

    template_name = 'about-us/about-us.html'
    context_object_name = 'about_us'

    def get_queryset(self):

        return About.objects.filter(is_published=True)
