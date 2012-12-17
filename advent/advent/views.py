from pyramid.view import view_config
from pyramid_layout.config import LayoutPredicate

layout_predicate = lambda v : LayoutPredicate(v, None)
def group_predicates(group_name):
    def _group_predicates(context, request):
        return context.login_group_name == group_name
    return _group_predicates

@view_config(custom_predicates=(group_predicates("red"), layout_predicate("red")), route_name="index", renderer="advent:templates/index.mako")
@view_config(custom_predicates=(group_predicates("blue"), layout_predicate("blue")), route_name="index", renderer="advent:templates/index.mako")
@view_config(custom_predicates=(group_predicates("green"), layout_predicate("green")), route_name="index", renderer="advent:templates/index.mako")
@view_config(custom_predicates=(group_predicates("yellow"), layout_predicate("yellow")), route_name="index", renderer="advent:templates/index.mako")
def index_view(context, request):
    students = context.Student.query
    return {"students": students}

