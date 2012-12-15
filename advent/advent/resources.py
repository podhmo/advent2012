class DefaultResource(object):
    def __init__(self, request):
        self.request = request

    @property
    def login_group_id(self):
        return 1
