from . import models
from . import api
from pyramid.decorator import reify

class ModelProxy(object):
    def __init__(self, model, query):
        self.model = model
        self.query = query

    def __getattr__(self, k):
        return getattr(self.model, k)
    
class DefaultResource(object):
    def __init__(self, request):
        self.request = request

    @property
    def login_group_name(self):
        return api.get_login_group_name(self.request)

    Group = models.Group
    @reify
    def Student(self):
        login_group_name = self.login_group_name
        query = models.Student.query.filter(models.Student.group_id==models.Group.id, 
                                            models.Group.short_name==login_group_name)
        return ModelProxy(models.Student, query)
