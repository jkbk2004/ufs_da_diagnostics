import os
import sys

# ---------------------------------------------------------------------------
# Ensure Sphinx imports the real package
# ---------------------------------------------------------------------------
sys.path.insert(0, os.path.abspath('../ufs_da_diagnostics'))

# ---------------------------------------------------------------------------
# Project information
# ---------------------------------------------------------------------------
project = "UFS-DA Diagnostics"
author = "Jong Kim"
release = "0.1.0"

# ---------------------------------------------------------------------------
# General configuration
# ---------------------------------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinxcontrib.mermaid",
]

# ⭐ IMPORTANT ⭐
# Sphinx 7.x autosummary recursion bug fix:
# Disable global autosummary generation.
autosummary_generate = False

napoleon_google_docstring = True
napoleon_numpy_docstring = False
autodoc_typehints = "description"
default_role = "code"

templates_path = ["_templates"]

# Prevent autosummary from scanning its own output
exclude_patterns = [
    "api/generated",
    "api/generated/**",
]

# ---------------------------------------------------------------------------
# HTML output
# ---------------------------------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

# ---------------------------------------------------------------------------
# Sphinx 7.x-compatible autosummary generation
# ---------------------------------------------------------------------------
def setup(app):
    """
    Sphinx 7.x-compatible autosummary generation:
    - We DO NOT call autosummary.generate_autosummary_docs()
    - Instead, we let autosummary run normally ONLY on pages that explicitly
      contain autosummary blocks.
    - This avoids the builder-inited crash and the concatenation bug.
    """
    pass

latex_elements = {
    'tableofcontents': r'''
        \pagenumbering{roman}
        \tableofcontents
        \clearpage
        \pagenumbering{arabic}
    ''',
}

latex_engine = 'xelatex'

latex_elements = {
    'inputenc': '',
    'fontenc': '',
}

latex_elements = {
    'fontpkg': r'''
\setmainfont{TeX Gyre Pagella}
\setsansfont{TeX Gyre Heros}
\setmonofont{TeX Gyre Cursor}
''',
}


