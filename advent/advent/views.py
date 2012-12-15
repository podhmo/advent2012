from pyramid.view import view_config
from .models import Student

@view_config(route_name="index", renderer="advent:templates/index.mako")
def index_view(context, request):
    students = Student.query
    return {"students": students}
