"""Setup for Boatwright."""
from setuptools import setup, Command
import os

import re
VERSIONFILE = "boatwright/__init__.py"
verfilestr = open(VERSIONFILE, "rt").read()
match = re.search(r"^__version__ = '(\d\.\d.\d+(\.\d+)?)'", verfilestr, re.MULTILINE)
if match:
    version = match.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE))


class Coverage(Command):
    """Class to allow coverage run from setup."""

    description = "run coverage"
    user_options = []

    def initialize_options(self):
        """Empty initialize_options."""
        pass

    def finalize_options(self):
        """Empty finalize_options."""
        pass

    def run(self):
        """Run coverage program."""
        os.system("coverage run --source=boatwright setup.py test")
        os.system("coverage report")
        os.system("coverage html")
        print("See htmlcov/index.html for details.")


setup(
    name='boatwright',
    version=version,
    author='Simeon Warner',
    author_email='simeon.warner@cornell.edu',
    packages=['boatwright'],
    package_data={},
    scripts=['loft.py'],
    classifiers=["Development Status :: 5 - Production/Stable",
                 "Intended Audience :: Developers",
                 "License :: OSI Approved :: "
                 "GNU General Public License v3 (GPLv3)",
                 "Operating System :: OS Independent",
                 "Programming Language :: Python",
                 "Programming Language :: Python :: 3",
                 "Programming Language :: Python :: 3.6",
                 "Programming Language :: Python :: 3.7",
                 "Programming Language :: Python :: 3.8",
                 "Libraries :: Python Modules"],
    url='https://github.com/zimeon/boatwright',
    license='LICENSE.txt',
    description='Boatwright boat design code',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'numpy>=1.19.4',
        'scipy>=1.5.4',
        'matplotlib>=1.15.0'
    ],
    test_suite="tests",
    tests_require=[
    ],
    cmdclass={
        'coverage': Coverage,
    },
)
