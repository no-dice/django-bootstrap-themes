from django.contrib.staticfiles.storage import staticfiles_storage

available_themes = [
    'default',
    'amelia',
    'cerulean',
    'cosmo',
    'cyborg',
    'flatly',
    'journal',
    'readable',
    'simplex',
    'slate',
    'spacelab',
    'united',
]

def list_themes():
    return available_themes

def get_script(use_min=True):
    minified = ''
    if use_min:
        minified = '.min'
    return staticfiles_storage.url('bootstrap/js/bootstrap%(minified)s.js' % dict(minified=minified))

def get_styles(theme='default', subdir='css', fileext='min.css'):
    if (not theme) or (theme == ''):
        theme = 'default'
    return staticfiles_storage.url('bootstrap/themes/%(theme)s/%(subdir)s/bootstrap.%(fileext)s' % dict(theme=theme, subdir=subdir, fileext=fileext))
