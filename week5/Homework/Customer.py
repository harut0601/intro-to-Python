import ProductCheck as pc


def buy(product, num, price):
#     print(pc.check(product, num))
    if pc.check(product, num):
        print(f'You bought {product} and spent {num*price}')
    
buy(product="candy", num=9, price=25)