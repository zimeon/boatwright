# Updating boatwright on pypi

Notes to remind @zimeon...

  * code at <https://github.com/zimeon/boatwright>
  * PyPi at <https://pypi.org/project/boatwright>

Putting up a new version
------------------------

  1. Check version number working branch in `boatwright/__init__.py`
  2. Check all changes described in `CHANGES.md`
  3. Check code is up-to-date with `main` branch on github
  4. Check all tests good (`tox`)
  5. Upload new version to PyPI:

    ```
    pip install --upgrade setuptools wheel twine
    rm -r dist
    python setup.py sdist bdist_wheel; ls dist
    twine upload dist/*
    ```
    
  6. Check on PyPI at <https://pypi.org/project/boatwright>
  7. Update version number by editing `boatwright/__init__.py` and `CHANGES.md`
