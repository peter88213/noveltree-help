# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'noveltree-help'
copyright = '2024, peter88213'
author = 'peter88213'
release = '0.2'
# html_logo = '_images/nLogo64.png'
html_title = 'noveltree help'
html_favicon = '_images/nLogo32.ico'
'''
html_theme_options = {
    "logo": {
        "link": "https://peter88213.github.io/noveltree/",
    }
}
'''
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
