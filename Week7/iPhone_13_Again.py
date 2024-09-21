'''iPhone 13 Again'''
def iphone_13_mini_price(capacity:str)->str:
    '''Return iphone 13 mini price based on the capacity'''
    if capacity == "128 GB":
        return "25900"
    if capacity == "256 GB":
        return "29900"
    if capacity == "512 GB":
        return "37900"
    return "Not Available"
def iphone_13_price(capacity:str)->str:
    '''Return iphone 13 price based on the capacity'''
    if capacity == "128 GB":
        return "29900"
    if capacity == "256 GB":
        return "33900"
    if capacity == "512 GB":
        return "41900"
    return "Not Available"
def iphone_13_pro_price(capacity:str)->str:
    '''Return iphone 13 pro price based on the capacity'''
    if capacity == "128 GB":
        return "38900"
    if capacity == "256 GB":
        return "42900"
    if capacity == "512 GB":
        return "50900"
    if capacity == "1 TB":
        return "58900"
    return "Not Available"
def iphone_13_pro_max_price(capacity:str)->str:
    '''Return iphone 13 pro max price based on the capacity'''
    if capacity == "128 GB":
        return "42900"
    if capacity == "256 GB":
        return "46900"
    if capacity == "512 GB":
        return "54900"
    if capacity == "1 TB":
        return "62900"
    return "Not Available"
def main():
    '''Driver Code'''
    gen = input()
    capacity = input()
    if gen == "iPhone 13 mini":
        print(iphone_13_mini_price(capacity))
    elif gen == "iPhone 13":
        print(iphone_13_price(capacity))
    elif gen == "iPhone 13 Pro":
        print(iphone_13_pro_price(capacity))
    elif gen == "iPhone 13 Pro Max":
        print(iphone_13_pro_max_price(capacity))
    else:
        print("Not Available")
if __name__ == "__main__":
    main()
