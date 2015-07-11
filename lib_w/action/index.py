#!coding=utf-8

from utility import ActionHandler
from mvc import *

@url(r"/")
class IndexHandler(ActionHandler):
    def get(self):
        self.render("action/user.html")


@url(r"/user")
class UserHandler(ActionHandler):
    def get(self):
        self.render("action/user.html")





