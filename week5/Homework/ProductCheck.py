products = {"candy": 10, "juice": 5, "pen": 50}

def check(product, num):
    if product in products.keys():
        if products.get(product) >= num:
            return True
    
    return False
    
    
# a = check("candy", 9)
# print(a)
