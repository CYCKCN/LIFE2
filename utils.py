from flask_login import UserMixin

time = ["0800", "0815", "0830", "0845", "0900", "0915", "0930", "0945", "1000", "1015", "1030", "1045", \
        "1100", "1115", "1130", "1145", "1200", "1215", "1230", "1245", "1300", "1315", "1330", "1345", \
        "1400", "1415", "1430", "1445", "1500", "1515", "1530", "1545", "1600", "1615", "1630", "1645", \
        "1700", "1715", "1730", "1745", "1800"]

class User(UserMixin):
    def __init__(self, id, name, auth):
        self.id = str(id)
        self.name = name
        self.auth = auth

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False

    def get_id(self):
        return self.name + ";" + self.id
    
class Account(object):
    def __init__(self, name, password, id, auth="USER", QRcode=None):
        self.accountName = name # "example@example.com"
        self.accountPw = password # "examplePW"
        self.accountID = id # 00310
        self.accountAuth = auth # "USER" / "ADMIN"
        self.accountQRcode = QRcode

class Order(object):
    def __init__(self, id, stime, etime, orderType="SELL", itemid=None, orderStatus="R"):
        self.orderID = id # "3387220221217"
        self.orderItemID = itemid # None / "3387220221217003"
        self.orderType = orderType # "SELL" / "BUY"
        self.orderStartTime = stime # "202212171000"
        self.orderEndTime = etime # "202212171030"
        self.orderStatus = orderStatus # "R" -> Reserved / "S" -> Solved