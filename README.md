django-bootstrap-themes
=======================

Bootstrap theme support for Django, includes themes from Bootswatch.

  * Bootstrap (http://getbootstrap.com/)
  * Bootswatch (http://bootswatch.com/)

Installation
------------

django-bootstrap-themes can be installed via pip:

```shell
pip install django-bootstrap-themes
```

or by copying the `bootstrap_themes` directory into your Django project.

Configuration
-------------

To configure django-bootstrap-themes in your project, first add it to
the installed apps in your Django settings:

```python
INSTALLED_APPS = (
    # Django apps
    'bootstrap_themes',
    # Other apps
)
```

Once you've added it to your installed apps, you can use the template
tags to get the CSS and JS files for Bootstrap:

  * Loading the templatetags

```django
{% load bootstrap_themes %}
```

  * Getting the CSS files (use the `theme` parameter to select the theme
    and the `type` parameter to choose between CSS, minified CSS, or LESS
    format for the stylesheets)

```django
{% bootstrap_styles theme='default' type='min.css' %}
{% bootstrap_styles theme='cosmo' type='css' %}
{% bootstrap_styles theme='united' type='less' %}
```

  * Getting the Javascript files (select minified or not with the
    `use_min` parameter)

```django
{% bootstrap_script use_min=True %}
```

As with any Django templatetags, you can use variables for the
parameters, thus making it easy to switch themes, and even make the
theme user-configurable.

If you want to make the theme user configurable, there is a handy
function to return the list of included themes as a `choices` list for
a `CharField`, like this:

```python
from django.db import models
from bootstrap_themes import list_themes

class MyModel(models.Model):
    theme = models.CharField(max_length=255, default='default', choices=list_themes())
```

Then in your templates, you can use the value of the `theme` field as the
theme parameter to `bootstrap_styles`.
