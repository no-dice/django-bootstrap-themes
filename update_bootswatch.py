import os
import json
import urllib2

theme_api = urllib2.urlopen('http://api.bootswatch.com/3/')
data = json.load(theme_api)
for theme in data['themes']:
    less_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'bootstrap_themes', 'static', 'bootstrap', 'themes', theme['name'].lower(), 'less'))
    if not os.access(less_path, os.F_OK):
        os.makedirs(less_path)
    if os.access(less_path, os.W_OK):
        try:
            theme_less = urllib2.urlopen(theme['less'])
            theme_less_file = open(os.path.join(less_path, 'bootswatch.less'), 'w')
            theme_less_file.write(theme_less.read())
            theme_less_file.close()
            theme_less.close()
        except IOError:
            print "Writing to file " + os.path.join(less_path, 'bootswatch.less') + " failed!"
        try:
            theme_less = urllib2.urlopen(theme['lessVariables'])
            theme_less_file = open(os.path.join(less_path, 'variables.less'), 'w')
            theme_less_file.write(theme_less.read())
            theme_less_file.close()
            theme_less.close()
        except IOError:
            print "Writing to file " + os.path.join(less_path, 'variables.less') + " failed!"
theme_list_file = open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'bootstrap_themes', 'themes.py')), 'w')
theme_list_file.write('theme_data = ')
theme_list_file.write(json.dumps(data))
theme_list_file.close()
theme_api.close()
