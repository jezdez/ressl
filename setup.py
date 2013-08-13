import os
import re
import codecs
from setuptools import setup


def read(*parts):
    return codecs.open(os.path.join(os.path.dirname(__file__), *parts)).read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='ressl',
    version=find_version('ressl.py'),
    description='A SSL redirector for shared hosting environments, e.g. Webfaction',
    long_description=read('README.rst'),
    author='Jannis Leidel',
    author_email='jannis@leidel.info',
    url='http://github.com/jezdez/ressl/',
    py_modules=['ressl'],
    zip_safe=False,
    install_requires=['importd>=0.2.1', 'django-secure'],
    entry_points=dict(console_scripts=['ressl=ressl:d.main']),
)
