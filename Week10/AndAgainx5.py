'''AndAgain*5'''
import re
def count_vowel(word:str) -> int:
    '''Return the number of vowels in a word'''
    count = 0
    for character in word:
        if character in "aeiouAEIOU":
            count += 1
    return count

def main():
    '''Driver Code'''
    paragraph = input()
    paragraph = re.sub(r"[\W\s]"," ",paragraph)
    words = paragraph.split()
    words_copy = words.copy()
    for word in words_copy:
        if count_vowel(word) < 2:
            words.remove(word)
    words.sort()
    if not words:
        print("Nope")
        return
    for word in words:
        print(word)
if __name__ == "__main__":
    main()
