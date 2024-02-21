# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
# #https://gitlab.com/pages/sphinx

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'ISIR template with documentation for gitlab'
copyright = '2024, ISIR, Sorbonne Universite, CNRS' 
author = 'Author'
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = ['myst_parser', 'sphinx_rtd_theme', 'sphinxcontrib.mermaid']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

myst_enable_extensions=['html_image',"html_admonition"]


# -- Options for mermaid output -------------------------------------------------

# mermaid_output_format = 'png'
mermaid_params = ['--theme', 'forest', '--width', '600', '--backgroundColor', 'transparent']
#mermaid_version = "" # use of local file _static/js/mermaid.js


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_logo = 'theme/logoIsir.png'

html_theme_options = {
    'vcs_pageview_mode': 'display_gitlab',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_css_files = [
    'css/isir.css',
]

#html_js_files = [
#   'js/mermaid_isir.js',
#]