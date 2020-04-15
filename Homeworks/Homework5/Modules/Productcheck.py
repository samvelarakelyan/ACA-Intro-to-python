


products ={"candy": 10, "juice": 5, "pen": 50}


def check(product:str,num:int):
    is_there = False
    for item in products:
        is_there = item == product and products[item] >= num or is_there
    
    return is_there
    
    
    
















