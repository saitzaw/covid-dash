"""setuptools based setup module."""
from os import path 
from setuptools import setup, find_packages
from io import open

here = path.abspath(path.dirname(__file__)) 

with open(path.join(here,'README.md'), encoding='utf-8') as f: 
    app_description = f.open() 

setup(
    name="plotly_flask_covid_visiualization",
    version="1.0.0-rc",
    description="Data visualization for the COVID-19 Globally and locally", 
    long_description = app_description, 
    long_description_content_type = 'text/markdown', 
    url='https://github.com/saitzaw/math4all.git', 
    author="Sai Thiha Zaw a.k.a Alexander Htun", 
    classifiers = [
        'Development Status :: 1 - Alpha', 
        'Intended Audience :: Developers and Data Scientists', 
        'Topic :: softwate development and Data science :: Build Tools', 
        'Programming Language :: Python :: 3.7.5' 
    ], 
    keywords="Plotly Dash Flask", 
    packages=find_packages(), 
    install_requires=['flask',
                      'flask_assets',
                      'pandas',
                      'dash',
                      'dash_core_components',
                      'dash_html_components',
                      'dash_bootstrap_components',
                      'dash_table',
                      'dash_renderer',
                      'pathlib'
    ], 
    entry_points={
        'console_scripts' : [
            'run = wsgi:main',
        ],
    },
    project_urls={
        'Bug Reports' : 'https://github.com/saitzaw/math4all/issues', 
        'Source': 'https://github.com/saitzaw/math4all'
    }
)
