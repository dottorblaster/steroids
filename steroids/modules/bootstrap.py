#!/usr/bin/python
# -*- coding=utf-8 -*-

import os
import urllib2
import zipfile

__help__ = """This module will install Twitter bootstrap. If you use examples, the module will generate bootstrap-ready html files in templates directory! """


requirements = [ ]

directories = [
    "[base]",
    "[base]/[name]",
    "[base]/[name]/static",
    "[base]/[name]/static/bootstrap",
    "[base]/[name]/templates",
]

files = [ ]

def install(basepath, name):
    """
        Download Install Bootstrap files 
    """
    # http://twitter.github.io/bootstrap/assets/bootstrap.zip
    
    static_files_path = os.path.join(basepath, name, "static/")
    bootstrap_file_path = os.path.join(static_files_path, "bootstrap.zip")
    
    
    remote_file = urllib2.urlopen('http://twitter.github.io/bootstrap/assets/bootstrap.zip').read()
    localfile = open(bootstrap_file_path, 'w')
    localfile.write(remote_file)
    localfile.close()
    
    current_dir = os.getcwd()
    bootstrap_zip = zipfile.ZipFile(bootstrap_file_path)
    for f in bootstrap_zip.namelist():
        if f.endswith('/'):
            new_directory = os.path.join(static_files_path,f)
            if not os.path.exists(new_directory):
                os.makedirs(new_directory)
            
            os.chdir(current_dir)
            os.chdir(new_directory)
        else:
            bootstrap_zip.extract(f)
    os.chdir(current_dir)
    os.remove(bootstrap_file_path)
    
    return
    
def install_examples(basepath, name):
    """
        Install Bootstrap Templates files. ( examples )
    """
    bootstrap_layout_file = open(os.path.join(basepath,name,"templates/bootstrap.html"), "w")
    bootstrap_layout_file.write("""<html>
    <head>
        <title>%s - {% block title %}{% endblock %}</title>

        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                
        <script src="http://code.jquery.com/jquery.min.js"></script>
        <script src="/static/bootstrap/js/bootstrap.js"></script>
        <link href="/static/bootstrap/css/bootstrap.css" rel="stylesheet">
        <link href="/static/bootstrap/css/bootstrap-responsive.css" rel="stylesheet">
    
        <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
        <!--[if lt IE 9]>
          <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
        <![endif]-->
        {% block head %}{% endblock %}
    </head>
    <body>
        {% block header %}{% endblock %}
        <div class="container">
            {% block container %}{% endblock %}
        </div>
        {% block footer %}<hr>{% endblock %}
    </body>    
</html>""")
    bootstrap_layout_file.close()
    return