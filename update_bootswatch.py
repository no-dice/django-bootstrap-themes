#!/usr/bin/env python

import os
import json
import urllib2

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

theme_api = urllib2.urlopen('http://api.bootswatch.com/3/')
data = json.load(theme_api)
for theme in data['themes']:
    less_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'bootstrap_themes', 'static', 'bootstrap', 'themes', theme['name'].lower(), 'less'))
    if not os.access(less_path, os.F_OK):
        os.makedirs(less_path)
    if os.access(less_path, os.W_OK):
        try:
            request = urllib2.Request(theme['less'], None, { 'User-Agent' : user_agent })
            theme_less = urllib2.urlopen(request)
        except urllib2.URLError as error:
            print "Opening URL " + theme['less'] + " failed!"
            print "Error: " + error.reason
            continue;
        try:
            theme_less_file = open(os.path.join(less_path, 'bootswatch.less'), 'w')
            theme_less_file.write(theme_less.read())
            theme_less_file.close()
            theme_less.close()
        except IOError:
            print "Writing to file " + os.path.join(less_path, 'bootswatch.less') + " failed!"

        try:
            request = urllib2.Request(theme['lessVariables'], None, { 'User-Agent' : user_agent })
            theme_less = urllib2.urlopen(request)
        except urllib2.URLError as error:
            print "Opening URL " + theme['lessVariables'] + " failed!"
            print "Error: " + error.reason
            continue;
        try:
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
