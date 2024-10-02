'''LetterFrequency'''
def main():
    '''Driver Code'''
    freq = {}
    sentence = input().lower()
    for char in sentence:
        if char.isalpha():
            freq[char] = freq.get(char,0) + 1
    most = -1
    most_char = ""
    for item in freq.items():
        if item[1] > most:
            most_char = item[0]
            most = item[1]
    print(most_char)
if __name__ == "__main__":
    main()
