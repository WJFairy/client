#!coding=utf-8

from mvc import *

class ActionHandler(BaseHandler):
    uid = property(lambda self: self.get_secure_cookie("__UID__"))

    def prepare(self):
        pass


