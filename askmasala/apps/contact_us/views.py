from apps.contact_us.forms import ContactUsForm
from django.contrib import messages
from django.views.generic.edit import FormView
from apps.contact_us.models import ContactUs
from django.http import HttpResponsePermanentRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render


class ContactUsView(FormView):

    model = ContactUs
    form_class = ContactUsForm
    template_name = 'contact_us/contact_us.html'
    success_url = '/contact-us/'

    def post(self,request, *args, **kwargs):

        self.form = self.get_form(self.form_class)
        if self.form.is_valid():
            self.object = self.form.save()
            messages.success(request, 'Your form has been submitted successfully')
        else:
            return render(request, 'contact_us/contact_us.html', {'form': self.form})
            # return HttpResponse(({'result': {'status': 'form_error', 'errors': self.form.errors}}),
            #                     content_type='application/json')

        return HttpResponsePermanentRedirect('/contact-us/')

