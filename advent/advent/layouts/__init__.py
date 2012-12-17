class IndexLayout(object):
    css = ""
    description = "<description>"

    def __init__(self, context, request):
        self.context = context
        self.request = request

class RedIndex(IndexLayout):
    css = u"""td {background-color: #ffaaaa;}"""
    description = u"red"

class GreenIndex(IndexLayout):
    css = u"""td {background-color: #aaffaa;}"""
    description = u"green"

class BlueIndex(IndexLayout):
    css = u"""td {background-color: #aaaaff;}"""
    description = u"blue"

class YellowIndex(IndexLayout):
    css = u"""td {background-color: #ffffaa;}"""
    description = u"yellow"    
