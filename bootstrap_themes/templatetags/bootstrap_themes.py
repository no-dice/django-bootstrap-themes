from django import template
from django.contrib.staticfiles.storage import staticfiles_storage
from .. import get_script, get_styles

register = template.Library()

@register.simple_tag
def bootstrap_script(use_min=True):
    return '<script type="text/javascript" src="%(script_file)s"></script>' % dict(script_file=get_script(use_min))

@register.simple_tag
def bootstrap_styles(theme='default', type='min.css'):
    if type == 'min.css' or type == 'css':
        subdir = 'css'
        fileext = type
        mimetype = 'text/css'
    elif type == 'less':
        subdir = type
        fileext = type
        mimetype = 'text/less'
    return '<link rel="stylesheet" href="%(theme_file)s" type="%(mimetype)s">' % dict(theme_file=get_styles(theme, subdir, fileext), mimetype=mimetype)
