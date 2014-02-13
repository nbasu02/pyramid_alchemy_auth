from pyramid.scaffolds import PyramidTemplate

class AlchemyAuthTemplate(PyramidTemplate):
	_template_dir = 'alchemy_auth'
	summary = '''Pyramid scaffold with SQLAlchemy, Pyramid Beaker, Alembic,
	and a few other personalized settings.'''