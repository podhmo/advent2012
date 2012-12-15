from pyramid.view import view_config
from .models import Student

@view_config(route_name="index", renderer="advent:templates/index.mako")
def index_view(context, request):
    students = Student.query.filter_by(group_id=context.login_user.group_id)
    return {"students": students}
