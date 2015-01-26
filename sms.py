import tornado.web
class SMSHandler(tornado.web.RequestHandler):
    import MySQLdb
    dbuser = ''
    dbpass = ''
    dbname = ''
    dbhost = ''
    #cursor = conn.cursor()
    def get_sms(self, phone):
        data = {}
        conn = self.MySQLdb.connect(host=self.dbhost,user=self.dbuser,passwd=self.dbpass,db=self.dbname,charset="utf8")
        cursor = conn.cursor()
        phoneinfo = "SELECT time,password FROM sms WHERE phone=%s ORDER BY time DESC LIMIT 10" %phone
        cursor.execute(phoneinfo)
        phonedata = cursor.fetchall()
        basinfo = """ SELECT areaname,basname FROM wo_user, basinfo, location WHERE ( wo_user.phone=%s AND wo_user.basid=basinfo.basid AND basinfo.areaid=location.areaid) """ %phone
        status = cursor.execute(basinfo)
        basdata = cursor.fetchone()
        try :
            len(basdata)
        except TypeError:
            basdata = ('未知','未知')
        conn.close()
        data['sms']=phonedata
        data['bas']=basdata
        return data

    def post(self):
        try:
            phone = self.get_argument('phone')
            smsdata = self.get_sms(phone)
            self.render('sms.html', phone = phone ,smsdata = smsdata)
        except TypeError:
            raise tornado.web.HTTPError(404)

    def get(self):
        self.render('sms_get.html')
