import logging
log = logging.getLogger(__name__)
from django.views.generic import ListView
from apps.about_us.models import About


class AboutUs(ListView):

    template_name = 'about-us/about-us.html'
    context_object_name = 'about_us'

    def get_queryset(self):

       return About.objects.filter(is_published=True)

log.debug("Hey there it works!!")
log.info("Hey there it works!!")
log.warn("Hey there it works!!")
log.error("Hey there it works!!")