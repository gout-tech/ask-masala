from apps.contact_us.models import ContactUs
from django import forms
import re
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class ContactUsForm(forms.ModelForm):

    Message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5,}))

    class Meta:
        model = ContactUs
        fields = ["Name", "Email", "Phone", "Subject","Message"]

    def __init__(self, request=None, *args, **kwargs):
        super(ContactUsForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'spr-form-input spr-form-input-text form-control'
            self.fields[field].widget.attrs['placeholder'] = field

    def clean(self):
        super(ContactUsForm, self).clean()
        return self.cleaned_data



