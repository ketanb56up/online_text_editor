from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def finger_print_token():
    """
     add a custom template tag finger_print_token with decorators "@register.simple_tag"
    :return: fingerprints js token value form settings
    """
    return settings.FINGER_PRINT_JS
