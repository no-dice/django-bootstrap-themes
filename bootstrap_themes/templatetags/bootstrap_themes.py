from django import template
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage

register = template.Library()

@register.simple_tag
def bootstrap_script(use_minified=True):
    minified = ''
    if use_minified:
        minified = '.min'
    script_file = staticfiles_storage.url('bootstrap/js/bootstrap%(minified)s.js' % dict(minified=minified))
    return '<script type="text/javascript" src="%(script_file)s"></script>' % dict(script_file=script_file)

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
    if (not theme) or (theme == ''):
        theme = 'default'
    theme_file = staticfiles_storage.url('bootstrap/themes/%(theme)s/%(subdir)s/bootstrap.%(fileext)s' % dict(theme=theme))
    return '<link rel="stylesheet" href="%(theme_file)s" type="%(mimetype)s">' % dict(theme_file=theme_file, mimetype=mimetype)
