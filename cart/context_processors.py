__author__ = 'Hernan Y.Ke'
from .cart import Cart

def cart(request):
    return {'cart':Cart(request)}

