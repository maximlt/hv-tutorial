# -*- coding: utf-8 -*-
from datetime import date

import pydata_sphinx_theme

from nbsite.shared_conf import *

project = "HoloViz Tutorial"
authors = 'HoloViz authors'
copyright_years['start_year'] = '2017'
copyright = copyright_fmt.format(**copyright_years)
description = 'The HoloViz Tutorial.'

# version = release  = base_version(ret.stdout.strip()[1:])
version = release = date.today().strftime("%Y.%m.%d")

extensions += [
    'nbsite.analytics',
    'nbsite.nb_interactivity_warning',
]

html_static_path += ['_static']

if pydata_sphinx_theme.__version__ == '0.16.1':
    # See https://github.com/pydata/pydata-sphinx-theme/issues/2088
    templates_path.append('_static/patch_templates')  # noqa

templates_path += [
    '_templates'
]

# Without this .txt is appended to the files
html_sourcelink_suffix = ''

html_theme = "pydata_sphinx_theme"
html_logo = '_static/holoviz-logo-unstacked.svg'
html_favicon = "_static/favicon.ico"

html_theme_options.update({
    'use_edit_page_button': True,
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
    'secondary_sidebar_items': [
        "page-toc",
        "edit-this-page",
        "sourcelink",
        "binderlink",
    ],
})

gh_org = 'holoviz'
gh_repo = 'tutorial'
gh_branch = 'main'
doc_path = 'tutorial'

html_context.update({
    'last_release': f'v{release}',
    'default_mode': 'light',
    'github_user': gh_org,
    'github_repo': gh_repo,
    'github_version': gh_branch,
    'doc_path': doc_path,
    'binder_url': f'https://mybinder.org/v2/gh/{gh_org}/{gh_repo}/{gh_branch}?filepath={doc_path}/'  # {relpath}
})

# cell execution timeout in seconds (-1 to ignore, 30 by default)
nb_execution_timeout = 240

# Uncomment to turn off notebook execution.
# nb_execution_mode = "off"

nbsite_analytics = {
    'goatcounter_holoviz': True,
}
