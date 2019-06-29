from apps.subscription.views import SubscribersForm
from django import template
register = template.Library()


@register.simple_tag()
def subscription_email():
    return SubscribersForm