import ProductCheck as pc


def buy(product, num, price):
    if buy(product) == pc.check(product):
        if buy(num) <= pc.check(num):
            print(f'You bought {product} and spent {num*price}')
    
    
buy(product="candy", num=9, price=25)