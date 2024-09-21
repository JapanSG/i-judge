'''DNA'''
def dna_is_valid(dna:str)->bool:
    '''Return true if string is a valid DNA sequence'''
    for i in dna:
        if not i in "ACGT":
            return False
    return True

def longest_substr(str1:str,str2:str)->str:
    '''Return the longest common sub string between 2 string'''
    i = 0
    ans = ""
    while i < len(str1):
        j = i+1
        while j <= len(str1):
            string = str1[i:j]
            if string in str2 and len(string) > len(ans):
                ans = string
            j += 1
        i += 1
    if not ans:
        return None
    return ans

def main():
    '''Driver Code'''
    dna1 = input()
    dna2 = input()
    if len(dna2) < len(dna1):
        dna1,dna2 = dna2,dna1
    if not dna_is_valid(dna1) or not dna_is_valid(dna2):
        print("Error")
    else:
        print(longest_substr(dna1,dna2))
if __name__ == "__main__":
    main()
