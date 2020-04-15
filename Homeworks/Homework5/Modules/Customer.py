from Productcheck import check


def buy(product:str, num:int, price:float):
    if not check(product,num):
        print("Sorry! We are out of this product.")
    else:
        print("You bought %s and spend %s" %(product,num*price))



def main():
    buy("candy",8,1850)
    
    
if __name__ == "__main__":
    
    main()










