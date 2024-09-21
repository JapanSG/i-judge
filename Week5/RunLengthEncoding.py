'''Run Length Encoding'''
def main():
    '''Driver Code'''
    data = input()
    length = len(data)
    key = ""
    i = 0
    while i < length:
        j = i+1
        if j >= length:
            key += str(j-i)+data[i]
            break
        while j < length and data[j] == data[i]:
            j += 1
        key += str(j-i)+data[i]
        i = j
    print(key)
main()
