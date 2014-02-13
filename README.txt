Usage:

First you need to install virtualenv and create a virtualenv in your filesystem
- cd /path/to/my/virtualenv
- source ./bin/active #Optional, but sets your path to be that of the virtualenv
- easy_install pip #Optional again, but pip is generally more used
- pip install pyramid
- python /path/to/this/directory/setup.py install
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
- Get the installation working
Stack trace looks like this at the pcreate step:

Traceback (most recent call last):
  File "/home/username/Projects/auth_test/bin/pcreate", line 9, in <module>
    load_entry_point('pyramid==1.4.5', 'console_scripts', 'pcreate')()
  File "/home/username/Projects/auth_test/local/lib/python2.7/site-packages/pyramid/scripts/pcreate.py", line 16, in main
    return command.run()
  File "/home/username/Projects/auth_test/local/lib/python2.7/site-packages/pyramid/scripts/pcreate.py", line 75, in run
    return self.render_scaffolds()
  File "/home/username/Projects/auth_test/local/lib/python2.7/site-packages/pyramid/scripts/pcreate.py", line 93, in render_scaffolds
    scaffold.run(self, output_dir, vars)
  File "/home/username/Projects/auth_test/local/lib/python2.7/site-packages/pyramid/scaffolds/template.py", line 64, in run
    self.write_files(command, output_dir, vars)
  File "/home/username/Projects/auth_test/local/lib/python2.7/site-packages/pyramid/scaffolds/template.py", line 96, in write_files
    template_renderer=self.render_template,
  File "/home/username/Projects/auth_test/local/lib/python2.7/site-packages/pyramid/scaffolds/copydir.py", line 63, in copy_dir
    names = sorted(os.listdir(source))
OSError: [Errno 2] No such file or directory: '/home/username/Projects/auth_test/local/lib/python2.7/site-packages/pyramid_alchemy_auth-0.1.0-py2.7.egg/pyramid_alchemy_auth/scaffolds/alchemy_auth'

- Include a requirements.txt file.  Ideally it should be generated from pip freeze after the project has been generated.
- Set up sqlalchemy session pooling
- Set up a testing suite with nosetests