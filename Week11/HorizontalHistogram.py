'''HorizontalHistogram'''
def main():
    '''Driver Code'''
    message = input()
    histogram = {}
    for char in message:
        if not (len(histogram.get(char,""))+1)%6:
            histogram[char] += "|"
        histogram[char] = histogram.get(char,"") + "-"
    for key in sorted(histogram,key = lambda key:key.swapcase()):
        print(f"{key} : {histogram[key]}")
if __name__ == "__main__":
    main()
