"""Sphinx configuration for the InterpretableMLWorkflow documentation."""

from __future__ import annotations

import os
import sys


PROJECT_ROOT = os.path.abspath("..")
sys.path.insert(0, PROJECT_ROOT)

project = "InterpretableMLWorkflow"
author = "Marcus Buckmann and Andreas Joseph"
copyright = "2026, Marcus Buckmann and Andreas Joseph"
release = "latest"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.githubpages",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx_autodoc_typehints",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

autosummary_generate = True
autodoc_member_order = "bysource"
autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "show-inheritance": False,
}

autodoc_mock_imports = [
    "lightgbm",
    "matplotlib",
    "monthdelta",
    "pathos",
    "patsy",
    "scipy",
    "shap",
    "sklearn",
    "statsmodels",
    "tscv",
]

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
}

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 4,
    "sticky_navigation": True,
}
html_title = "InterpretableMLWorkflow documentation"
