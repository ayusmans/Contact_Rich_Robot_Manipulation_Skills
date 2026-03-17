# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


import importlib.metadata

from sphinx.application import Sphinx


project = 'Train and Deploy Contact-Rich Robot Manipulation Skills With Isaac Lab and Isaac ROS'
copyright = '2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved'
author = 'NVIDIA'
release = importlib.metadata.version("learning_path")
print(release)

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.intersphinx',
    'myst_parser',
    'sphinx_design',
    'sphinx_copybutton',
    'sphinx_nvlearning',
]

templates_path = ['_templates']
exclude_patterns = ['_includes/**']
myst_enable_extensions = ['colon_fence', 'html_image', 'attrs_inline', 'attrs_block']
myst_title_to_header = True
myst_number_code_blocks = ['python', 'py', 'usda', 'usd']
myst_links_external_new_tab = True
myst_heading_anchors = 3


# TODO: Remove the two following parameters when the theme is fixed
toc_object_entries_show_parents = 'hide'
maximum_signature_line_length = 70



html_theme = 'nvidia_sphinx_theme'
html_static_path = ['_static']
html_css_files = []
html_theme_options = {
    "extra_head": {
        """
    <script src="https://assets.adobedtm.com/5d4962a43b79/c1061d2c5e7b/launch-191c2462b890.min.js" ></script>
    """
    },
    "extra_footer": {
        """
    <script type="text/javascript">if (typeof _satellite !== "undefined") {_satellite.pageBottom();}</script>
    """
    },
}


    