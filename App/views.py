from flask import Blueprint, render_template

from App.models import HomeWheel, HomeNav, HomeMustBuy, HomeShop, HomeMainShow, FoodType, Goods

blue = Blueprint('first_blue',__name__)

def init_first_blue(app):
    app.register_blueprint(blueprint=blue)

@blue.route('/')
def axf():
    return 'axf'

@blue.route('/home/')
def home():
    data =[[{'title':'首页'}],[],[],[],[],[]]
    wheels = HomeWheel.query.all()
    for wheel in wheels:
        data[1].append(wheel.model_to_dict())

    navs = HomeNav.query.all()
    for nav in navs:
        data[2].append(nav.model_to_dict())

    mustbuys =  HomeMustBuy.query.all()
    for mustbuy in mustbuys:
        data[3].append(mustbuy.model_to_dict())

    shops = HomeShop.query.all()
    for shop in shops:
        data[4].append(shop.model_to_dict())

    mainshows = HomeMainShow.query.all()
    for mainshow in mainshows:
        data[5].append(mainshow.model_to_dict())



    # wheels = wheels, navs = navs, mustbuys = mustbuys
    return render_template('home/home.html',data = data)

@blue.route('/market/')
def market():

    data = [[{'title':'闪购超市'}],[],[],[],[],[]]

    foodtypes = FoodType.query.all()
    goods = Goods.query.all()

    for foodtype  in foodtypes:
        data[1].append(foodtype.model_to_dict())

    for good in goods:
        data[2].append(good.model_to_dict())

        # print(data[2])
    return render_template('market/market.html',data = data)





@blue.route('/cart/')
def cart():
    return render_template('cart/cart.html')

@blue.route('/mine/')
def mine():
    return render_template('mine/mine.html')
