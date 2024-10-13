'''CaesarV1'''
def ceasar(message:str, shift: int) -> str:
    '''ceasar chipher'''
    alpha = "abcdefghijklmnopqrstuvwxyz"
    coded = ''
    for char in message:
        if char.isalpha():
            coded_char = alpha[(alpha.find(char.lower())+shift)%26]
            if char.isupper():
                coded += coded_char.upper()
            else:
                coded += coded_char
        else:
            coded += char
    return coded
def main():
    '''Driver Code'''
    shift = int(input())
    message = input()
    print(ceasar(message,shift))
if __name__ == "__main__":
    main()
