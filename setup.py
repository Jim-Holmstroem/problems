try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'problems',
    'description': 'My Project',
    'author': 'Jim Holmström',
    'author_email': 'jim.holmstroem@gmail.com / jimho@kth.se',
    'url': 'github.com:Jim-Holmstroem/problems.git',
    'download_url': 'github.com:Jim-Holmstroem/problems.git',
    'version': '0.1',
    'install_requires': [],
    'packages': ['problems'],
    'scripts': [],
}

setup(**config)
