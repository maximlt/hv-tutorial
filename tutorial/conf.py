# -*- coding: utf-8 -*-
from datetime import date
from pathlib import Path

from nbsite.shared_conf import *

project = "HoloViz Tutorial"
authors = author = 'HoloViz authors'
copyright_years['start_year'] = '2017'
copyright = copyright_fmt.format(**copyright_years)
description = 'The HoloViz Tutorial.'

# version = release  = base_version(ret.stdout.strip()[1:])
version = release = date.today().strftime("%Y.%m.%d")

extensions += [
    'nbsite.analytics',
    'nbsite.nb_interactivity_warning',
]

# Dont inherit from nbsite's shared static folder as it contains
# some CSS files that mess with Sphinx book theme's CSS
html_static_path = ['_static']

templates_path += [
    '_templates'
]

html_theme = "sphinx_book_theme"
html_logo = '_static/holoviz-logo-unstacked.svg'
html_favicon = "_static/favicon.ico"

gh_org = 'holoviz'
gh_repo = 'tutorial'
gh_branch = 'main'
doc_path = 'tutorial'

html_theme_options.update({
    "github_url": "https://github.com/holoviz/tutorial",
    "icon_links": [
        {
            "name": "Twitter",
            "url": "https://twitter.com/HoloViz_Org",
            "icon": "fab fa-twitter-square",
        },
        {
            "name": "Discourse",
            "url": "https://discourse.holoviz.org/",
            "icon": "fab fa-discourse",
        },
    ],
    "use_download_button": True,
    "use_source_button": True,
    "use_edit_page_button": True,
    "use_repository_button": True,
    "use_issues_button": True,
    "repository_url": "https://github.com/holoviz/tutorial",
    "repository_branch": "main",
    "path_to_docs": "tutorial",
    "launch_buttons": {
        "notebook_interface": "jupyterlab",
        "binderhub_url": f"https://mybinder.org/v2/gh/{gh_org}/{gh_repo}/{gh_branch}?filepath={doc_path}/"
    },
})

# nbsite overrides that
html_sidebars = {
    "**": [
        "navbar-logo.html",
        "icon-links.html",
        "search-button-field.html",
        "sbt-sidebar-nav.html",
        "hv-sidebar-dropdown",
    ]
}

# cell execution timeout in seconds (-1 to ignore, 30 by default)
nb_execution_timeout = 240

# Uncomment to turn off notebook execution.
nb_execution_mode = "off"

nbsite_analytics = {
    'goatcounter_holoviz': True,
}
