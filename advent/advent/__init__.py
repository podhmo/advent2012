from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import DBSession

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    config = Configurator(settings=settings, root_factory=".resources.DefaultResource")
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('index', '/')
    config.scan()
    return config.make_wsgi_app()

