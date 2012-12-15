from pyramid.view import view_config

@view_config(route_name="index", renderer="advent:templates/index.mako")
def index_view(context, request):
    students = context.Student.query
    return {"students": students}

