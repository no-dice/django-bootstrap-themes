from django import template
from django.contrib.staticfiles.storage import staticfiles_storage

register = template.Library()

@register.simple_tag
def bootstrap_theme(theme):
    if not theme:
        return staticfiles_storage.url('bootstrap/css/bootstrap.min.css')
    return staticfiles_storage.url('bootstrap/themes/%(theme)s/css/%(theme)s.min.css' % dict(theme=theme))
