#!coding=utf-8

from utility import ActionHandler
from mvc import *
from logic import config
from mvc import mssql_util

def get_db_args():
    db_host = config.get('database', 'db_host')
    db_user = config.get('database', 'db_user')
    db_password = config.get('database', 'db_password')
    db_name = config.get('database', 'db_name')
    return dict(db_host = db_host, db_user = db_user, db_password = db_password, db_name = db_name)

@url(r"/")
class IndexHandler(ActionHandler):
    def get(self):
        self.redirect("/user")


@url(r"/user")
class UserHandler(ActionHandler):
    def get(self):
        db_args = get_db_args()
        users = mssql_util.m_query("select _id, opt_ID, nickname from passport", **db_args)
        self.render("action/user.html", users = users)

@url(r"/user/add")
class UserAdd(ActionHandler):
    def post(self):
        opt_ID = self.get_argument("opt_ID")
        nickname = self.get_argument("nickname")
        db_args = get_db_args()
        mssql_util.m_execute("insert into passport(opt_ID, nickname) values ('{}' ,'{}')".format(opt_ID, nickname), **db_args)

        self.write({'status': True})

@url(r"/user/del")
class UserDel(ActionHandler):
    def post(self):
        _id = self.get_argument("_id")
        db_args = get_db_args()
        mssql_util.m_execute("delete from passport where _id = '{}'".format(_id), **db_args)

        self.write({'status': True})

@url(r"/user/delall")
class UserDelall(ActionHandler):
    def post(self):
        _ids = self.get_argument("_id")
        _ids = _ids.split(',')

        db_args = get_db_args()
        for _id in _ids:
            mssql_util.m_execute("delete from passport where _id = '{}'".format(_id), **db_args)

        self.write({'status': True})        

@url(r"/user/find")
class UserFind(ActionHandler):
    def get(self):
        _id = self.get_argument("_id")
        
        db_args = get_db_args()
        users = mssql_util.m_query("select _id, opt_ID, nickname from passport where _id = '{}'".format(_id), **db_args)
        users = users[0]

        self.write({'status': True, 'users': users})

@url(r"/user/update")
class UserUpdate(ActionHandler):
    def post(self):
        _id = self.get_argument("_id")
        opt_ID = self.get_argument('opt_ID')
        nickname = self.get_argument('nickname')
        
        db_args = get_db_args()
        users = mssql_util.m_execute("update passport set opt_ID='{}',nickname='{}' where _id = '{}'".format(opt_ID,nickname, _id), **db_args)

        self.write({'status': True})









@url(r"/settings")
class SettingsHandler(ActionHandler):
    def get(self):
    	db_host = config.get('database', 'db_host')
    	db_user = config.get('database', 'db_user')
    	db_password = config.get('database', 'db_password')
        db_name = config.get('database', 'db_name')
    	
        self.render("action/settings.html", db_host = db_host, db_user = db_user, db_password = db_password, db_name = db_name)

    def post(self):
    	db_host = self.get_argument('db_host')
    	db_user = self.get_argument('db_user')
    	db_password = self.get_argument('db_password')
        db_name = self.get_argument('db_name')

    	config.set('database', 'db_host', db_host)
    	config.set('database', 'db_user', db_user)
    	config.set('database', 'db_password', db_password)
        config.set('database', 'db_name', db_name)

    	self.write(dict(status = True))
    	