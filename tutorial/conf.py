# -*- coding: utf-8 -*-
import subprocess

from nbsite.shared_conf import *


project = "HoloViz"
authors = 'HoloViz authors'
copyright_years['start_year'] = '2017'
copyright = copyright_fmt.format(**copyright_years)
description = 'High-level tools to simplify visualization in Python.'

# version = release  = base_version(ret.stdout.strip()[1:])
version = release = "0.0.1"

extensions += [
    'nbsite.analytics',
]

html_static_path += ['_static', 'assets']
templates_path += ['_templates']

html_theme = "pydata_sphinx_theme"
html_logo = '_static/holoviz-logo-unstacked.svg'
html_favicon = "_static/favicon.ico"

html_theme_options.update({
    "github_url": "https://github.com/holoviz/holoviz",
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
    "header_links_before_dropdown": 6,
    "secondary_sidebar_items": [
        "github-stars-button",
        "page-toc",
    ],
})

html_context.update({
    # Used to add binder links to the latest released tag.
    'last_release': f'v{release}',
    'github_user': 'holoviz',
    'github_repo': 'holoviz',
})

# Uncomment to turn off notebook execution.
# nb_execution_mode = "off"

nbsite_analytics = {
    'goatcounter_holoviz': True,
}

# Customize as its default is for all the other HoloViz sites.
nbsite_hv_sidebar_dropdown['dropdown_value'] = {'text': 'HoloViz Sites'}
del nbsite_hv_sidebar_dropdown['others']


# myst_enable_extensions = [
#     # MySt-Parser will attempt to convert any isolated img tags (i.e. not
#     # wrapped in any other HTML) to the internal representation used in sphinx.
#     'html_image',
# ]

nb_execution_mode = "off"
