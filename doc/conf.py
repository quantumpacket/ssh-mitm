# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import datetime
import xml.etree.ElementTree as ET

# -- Project information -----------------------------------------------------

project = 'SSH-MITM'
author = 'SSH-MITM Dev-Team'
copyright = '{}, {}'.format(datetime.datetime.now().year, author)  # pylint: disable=redefined-builtin

extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx_sitemap',
    'sphinx_reredirects',
]

master_doc = 'index'
html_permalinks = False
html_baseurl = 'https://docs.ssh-mitm.at/'
autosectionlabel_maxdepth = 1
html_extra_path = ['robots.txt']

# -- General configuration ---------------------------------------------------

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

redirects = {
     "puttydos": "CVE-2021-33500.html"
}

header = {
    'title': 'SSH MITM SERVER & content inspection',
    'summary': 'man in the middle (mitm) server for security audits supporting public key authentication, session hijacking and file manipulation'
}

footer = {
    'title': 'SSH-MITM proxy server is open source',
    'summary': 'and developed by the community. Be a part of this community and...',
    'linktext': 'contribute to SSH-MITM'
}

page_descriptions = {
    'install.html': 'SSH-MITM server is easy to install with Python and PIP',
    'quickstart.html': 'Short guide to setup an intercepting ssh-mitm server with a single command',
    'advanced-usage.html': 'Guide how to setup a man in the middle server for advanced security audits in large networks and special use cases',
    'ssh_vulnerabilities.html': 'Explanation of vulnerabilities related to the ssh protocol',
    'jumphosts.html': 'SSH-MITM should not be used as jump host. This page describes alternatives and security considerations when operating a jump host',
    'portforwarding.html': 'Introduction to port forwarding features of ssh-mitm'
}

html_context = {
    'author': author,
    'page_descriptions': page_descriptions,
    'intro_text': 'SSH MITM SERVER & content inspection',
    'footer': footer,
    'social': {
        'githubfork_ribbon': True,
        'githubrepo': 'https://github.com/ssh-mitm/ssh-mitm',
        'pypiurl': 'https://pypi.org/project/ssh-mitm/',
        'linkedinurl': 'https://www.linkedin.com/in/manfred-kaiser'
    }
}


def create_sitemap(app, exception):
    """Generates the sitemap.xml from the collected HTML page links"""
    filename = app.outdir + "/sitemap-docs.xml"
    print("Generating sitemap-docs.xml in %s" % filename)

    root = ET.Element("urlset")
    root.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")

    for link in app.sitemap_links:
        url = ET.SubElement(root, "url")
        ET.SubElement(url, "loc").text = html_baseurl + link

    ET.ElementTree(root).write(filename)


def setup(app):
    app.connect('build-finished', create_sitemap)
