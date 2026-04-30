import os
import sys

# Add repo root to Python path
sys.path.insert(0, os.path.abspath(".."))

project = "UFS-DA-diagnostics"
author = "Jong Kim"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
]

autosummary_generate = True
html_theme = "sphinx_rtd_theme"
