from apps.subscription.models import Subscribers
from django import forms
from django.core.validators import validate_email


class SubscribersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = "__all__"

    def __init__(self, request=None, *args, **kwargs):
        super(SubscribersForm, self).__init__(*args, **kwargs)
        for field_name,field in self.fields.items():
            field.widget.attrs['class'] = 'spr-form-input spr-form-input-text form-control'
            field.widget.attrs['placeholder'] = field_name

    def clean(self):
        super(SubscribersForm, self).clean()
        return self.cleaned_data