.. 

pastebin
======================

Quickstart
----------

To bootstrap the project::

    virtualenv pastebin
    source pastebin/bin/activate
    cd path/to/pastebin/repository
    pip install -r requirements.pip
    pip install -e .
    cp pastebin/settings/local.py.example pastebin/settings/local.py
    manage.py syncdb --migrate

Documentation
-------------

Developer documentation is available in Sphinx format in the docs directory.

Initial installation instructions (including how to build the documentation as
HTML) can be found in docs/install.rst.
