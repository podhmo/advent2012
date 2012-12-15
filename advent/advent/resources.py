from . import models
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
    def login_group_id(self):
        return 1

    Group = models.Group
    @reify
    def Student(self):
        login_group_id = self.login_group_id
        query = models.Student.query.filter_by(group_id=login_group_id)
        return ModelProxy(models.Student, query)
