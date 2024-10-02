'''VerticalHistogram'''
def main():
    '''Driver Code'''
    freq = {}
    message = input()
    most = -1
    for char in message:
        if char.isalpha():
            val  = freq.get(char,0) + 1
            freq[char] = val
            most = max(val,most)
    keys = sorted(freq)
    for i in range(most,0,-1):
        print(f"{i:2d} ",end = "")
        for key in keys:
            if freq[key] >= i:
                print(" *",end = "")
            else:
                print("  ",end = "")
        print("")
    print("   ",end = "")
    for key in keys:
        print(f" {key}",end = "")
if __name__ == "__main__":
    main()
