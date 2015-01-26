#!/usr/local/bin/python3
import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
#from sms import SMSHandler
from sms import SMSHandler

from tornado.options import define, options
define("port", default=8880, help="run on the given port", type=int)



class PoemPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class IndexHandler(tornado.web.RequestHandler):
    import MySQLdb
    import json
    dbuser = ''
    dbpass = ''
    dbname = ''
    dbhost = ''
    conn = MySQLdb.connect(host=dbhost,user=dbuser,passwd=dbpass,db=dbname,charset="utf8")
    cursor = conn.cursor()

    def getdata(self, basid, bw):
        time = []
        key = "%sM" %bw
        sql = '''select timelength/3600 from tt as t where basid=%s and bwid in (select bwid from bw_def where realbw=%s) order by time;'''
        param = (basid,bw)
        self.cursor.execute(sql,param)
        r = self.cursor.fetchall()
        for line in r:
            time.append(int(line[0]))
        res = {'name':key, 'data':time}
        return res

    def get_data(self, basname):
        data = []
        sql = "select basid from basinfo where basname='%s'" %basname
        self.cursor.execute(sql)
        basid = self.cursor.fetchone()[0]
        for bw in [1,2,4,8,10,20]:
             f=self.getdata(basid, bw)
             data.append(f)
        return data

    def get_lenth(self):
        sql = 'select count(distinct time) from tt'
        self.cursor.execute(sql)
        l = self.cursor.fetchone()[0]
        return list(range(1,l+1))

    def show_name(self):
        l = []
        sql = "select basname from basinfo order by basname"
        self.cursor.execute(sql)
        r = self.cursor.fetchall()
        for line in r:
            l.append(line[0])
        #print(l)
        #return l


    def post(self):
        try:
            basname = self.get_argument('basname')
            fdata = self.get_data(basname)
            lenth = self.get_lenth()
            self.render('baspost.html', basname = basname, fdata = fdata, lenth = lenth)
#        self.conn.close()
        except TypeError:
            raise tornado.web.HTTPError(404)

    def get(self):
        self.render('index.html')

class stock1(tornado.web.RequestHandler):
    def get(self):
        self.render('stock1.html')


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
					(r'/', IndexHandler),
					(r'/stock1',stock1),
					(r'/sms', SMSHandler),
		],



        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
		#debug=True
		debug=False
    )

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
