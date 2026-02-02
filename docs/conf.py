# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'aula 115'
copyright = '2026, Julian Camilo Fonseca Romero, IE John F. Kennedy, Puerto Boyacá (Boyacá), Colombia.'
author = 'Julian Camilo Fonseca Romero'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser","sphinx_design","sphinxcontrib.mermaid"]

myst_enable_extensions = [
    "dollarmath", #ecuaciones matematicas con $
    "tasklist", # listas con casillas de verificacion
    "colon_fence", #bloques con ::: en vez de ```
    "attrs_inline", # para agregar atributos en linea ejemplo: IMAGENES
    "smartquotes", #comillas inteligentes
    #"linkify", # convierte URLs en enlaces automaticamente
    "fieldlist" # listas de campos
]

myst_number_code_blocks = ["python", "c++"] # Numera bloques de código en los lenguajes especificados
myst_links_external_new_tab = True # Abre enlaces externos en una nueva pestaña
myst_enable_checkboxes = True # Habilita casillas de verificación en las listas de tareas
myst_heading_anchors = 3 # Genera enlaces ancla para los encabezados (niveles 1 a 3)


templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_title = "EVA - aula 115 (pruebas)"

pygments_style = "sphinx"
pygments_dark_style = "monokai"

html_theme_options = {
    "light_logo": "logo_light.png",
    "dark_logo": "logo_light.png",
    "sidebar_hide_name": True,
    "light_css_variables": {
        "color-guilabel-text": "#FF0000",
        "color-brand-primary": "#265787",
        "sidebar-caption-font-size": "var(--font-size--normal)",
        "toc-font-size": "var(--font-size--small)",
        "admonition-font-size": "0.858rem"
    },
}