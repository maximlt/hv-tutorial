# -*- coding: utf-8 -*-
from datetime import date

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
]

html_static_path += ['_static']

html_theme = "pydata_sphinx_theme"
html_logo = '_static/holoviz-logo-unstacked.svg'
html_favicon = "_static/favicon.ico"

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
    "secondary_sidebar_items": [
        "github-stars-button",
        "page-toc",
    ],
})

html_context.update({
    # Used to add binder links to the latest released tag.
    'last_release': f'v{release}',
    'github_user': 'holoviz',
    'github_repo': 'tutorial',
})

# Uncomment to turn off notebook execution.
# nb_execution_mode = "off"

nbsite_analytics = {
    'goatcounter_holoviz': True,
}
