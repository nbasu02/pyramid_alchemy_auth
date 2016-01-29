Usage:

First you need to install virtualenv and create a virtualenv in your filesystem
- cd /path/to/my/virtualenv
- source ./bin/active #Optional, but sets your path to be that of the virtualenv
- easy_install pip #Optional again, but pip is generally more used
- pip install pyramid
- cd /path/to/this/directory
- python setup.py install # or pip install
- pcreate my_project_name -s alchemy_auth

What is in this project that the normal alchemy scaffold?

This is a very personalized scaffold so in the future I can skip a number of basic steps when starting up a new project.  Changes over the alchemy scaffold include:

- Installation and implementation of authentication with pyramid_beaker.  There are a few bare bones .html.mako templates showing the authentication working
- Installation of alembic (and changing revision filenames to be the create time rather than hexes)
- Default to postgres instead of sqlite.  initializedb script also simply creates the database for you, with no added fluff
- MyModel is removed.  The only models present are User and UserSession for beaker.  The base model also includes id as a UUID, and create/modify timestamps
- my_view is removed, and replaced with authentication views
- The dummy tests have been removed

TODO items:
- Include a requirements.txt file.  Ideally it should be generated from pip freeze after the project has been generated.
- Set up sqlalchemy session pooling
- Set up a testing suite with nosetests
