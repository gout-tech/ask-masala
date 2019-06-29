from django.shortcuts import render
from apps.subscription.forms import SubscribersForm
from django.contrib import messages
from django.views.generic.edit import FormView
from apps.subscription.models import Subscribers
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
from django.shortcuts import render


class SubscriptionView(FormView):

    form_class = SubscribersForm
    model = Subscribers
    template_name = 'base.html'
    def post(self,request, *args, **kwargs):
        self.form2 = self.get_form(self.form_class)
        if self.form2.is_valid():
            self.object = self.form2.save()
        else:
            return render(request, 'base.html', {'form2': self.form2})
        return HttpResponsePermanentRedirect('#')
