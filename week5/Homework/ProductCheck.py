products = {"candy": 10, "juice": 5, "pen": 50}

def check(product, num):
    if product in products.keys():
        new_products = product
        if products.get(new_products) >= num:
            return True
        else:
            return False
        
    
    
new = check("candy", 9)
