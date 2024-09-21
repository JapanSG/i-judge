'''iPhone 13 Again'''
mini_price = {
    "128 GB": "25900",
    "256 GB": "29900",
    "512 GB": "37900"
}
normal_price = {
    "128 GB": "29900",
    "256 GB": "33900",
    "512 GB": "41900"
}
pro_price = {
    "128 GB": "38900",
    "256 GB": "42900",
    "512 GB": "50900",
    "1 TB": "58900"
}
pro_max_price= {
    "128 GB": "42900",
    "256 GB": "46900",
    "512 GB": "54900",
    "1 TB": "62900"
}
gendict = {
    "iPhone 13 mini": mini_price,
    "iPhone 13": normal_price,
    "iPhone 13 Pro": pro_price,
    "iPhone 13 Pro Max": pro_max_price
}
def main():
    '''Driver Code'''
    try:
        gen = input()
        cap = input()
        print(gendict[gen][cap])
    except KeyError:
        print("Not Available")
if __name__ == "__main__":
    main()
