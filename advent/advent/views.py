from pyramid.view import view_config
from pyramid_layout.config import LayoutPredicate

layout_predicate = lambda v : LayoutPredicate(v, None)
def group_predicates(group_id):
    def _group_predicates(context, request):
        return context.login_group_id == group_id
    return _group_predicates

@view_config(custom_predicates=(group_predicates(1), layout_predicate("red")), route_name="index", renderer="advent:templates/index.mako")
@view_config(custom_predicates=(group_predicates(2), layout_predicate("blue")), route_name="index", renderer="advent:templates/index.mako")
@view_config(custom_predicates=(group_predicates(3), layout_predicate("green")), route_name="index", renderer="advent:templates/index.mako")
@view_config(custom_predicates=(group_predicates(4), layout_predicate("yellow")), route_name="index", renderer="advent:templates/index.mako")
def index_view(context, request):
    students = context.Student.query
    return {"students": students}

