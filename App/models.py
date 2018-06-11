from App.ext import db

class Home(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    img = db.Column(db.String(200))
    name = db.Column(db.String(32))
    trackid = db.Column(db.Integer, default=1)
    def model_to_dict(self):
        return {'id': self.id, 'img': self.img, 'name': self.name,'trackid':self.trackid}

class HomeWheel(Home):
    __tablename__ = 'axf_wheel'



class HomeNav(Home):
    __tablename__ = 'axf_nav'



class HomeMustBuy(Home):
    __tablename__ = 'axf_mustbuy'


class HomeShop(Home):
    __tablename__ = "axf_shop"

class HomeMainShow(Home):
    __tablename__ = "axf_mainshow"

    categoryid = db.Column(db.Integer,default=1)
    brandname = db.Column(db.String(32))

    img1 = db.Column(db.String(200))
    childcid1 = db.Column(db.Integer,default=1)
    productid1 = db.Column(db.Integer,default=1)
    longname1 = db.Column(db.String(200))
    price1 = db.Column(db.Float,default=0)
    marketprice1 = db.Column(db.Float,default=0)

    img2 = db.Column(db.String(200))
    childcid2 = db.Column(db.Integer,default=1)
    productid2 = db.Column(db.Integer,default=1)
    longname2 = db.Column(db.String(200))
    price2 = db.Column(db.Float,default=0)
    marketprice2 = db.Column(db.Float,default=0)

    img3 = db.Column(db.String(200))
    childcid3 = db.Column(db.Integer,default=1)
    productid3 = db.Column(db.Integer,default=1)
    longname3 = db.Column(db.String(200))
    price3 = db.Column(db.Float,default=0)
    marketprice3 = db.Column(db.Float,default=0)

    def model_to_dict(self):
        return {'id': self.id,
                'img': self.img,
                'name': self.name,
                'trackid': self.trackid,
                'img1':self.img1,
                'childcid1': self.childcid1,
                'productid1':self.productid1,
                'longname1':self.longname1,
                'price1':self.price1,
                'marketprice1': self.marketprice1,
                'img2': self.img2,
                'childcid2': self.childcid2,
                'productid2': self.productid2,
                'longname2': self.longname2,
                'price2': self.price2,
                'marketprice2': self.marketprice2,
                'img3': self.img3,
                'childcid3': self.childcid3,
                'productid3': self.productid3,
                'longname3': self.longname3,
                'price3': self.price3,
                'marketprice3': self.marketprice3,
                }



class FoodType(db.Model):
    __tablename__ = 'axf_foodtypes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    typeid = db.Column(db.Integer,default=1)
    typename = db.Column(db.String(16))
    childtypenames = db.Column(db.String(200))
    typesort = db.Column(db.Integer,default=1)

    def model_to_dict(self):
        return {
            'id':self.id,
            'typeid':self.typeid,
            'typename':self.typename,
            'childtypenames':self.childtypenames,
            'typesort':self.typename
        }

class Goods(db.Model):

    __tablename__ = "axf_goods"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    productid = db.Column(db.Integer,default=1)
    productimg = db.Column(db.String(200))
    productname = db.Column(db.String(128))
    productlongname = db.Column(db.String(128))
    isxf = db.Column(db.Boolean,default=False)
    pmdesc = db.Column(db.Boolean,default=False)
    specifics = db.Column(db.String(16))
    price = db.Column(db.Float,default=0)
    marketprice = db.Column(db.Float,default=1)
    categoryid = db.Column(db.Float,default=1)
    childcid = db.Column(db.Integer,default=1)
    childcidname = db.Column(db.String(128))
    dealerid = db.Column(db.Integer,default=1)
    storenums = db.Column(db.Integer,default=1)
    productnum = db.Column(db.Integer,default=1)

    def model_to_dict(self):
        return {
            'id':self.id,
            'productid':self.productid,
            'productimg':self.productimg,
            'productname':self.productname,
            'productlongname':self.productlongname,
            'isxf':self.isxf,
            'pmdesc':self.pmdesc,
            'specifics':self.specifics,
            'price':self.price,
            'marketprice':self.marketprice,
            'categoryid':self.categoryid,
            'childcid':self.childcid,
            'childcidname':self.childcidname,
            'dealerid':self.dealerid,
            'storenums':self.storenums,
            'productnum':self.productnum
        }
