'''Turnstile'''
def main():
    '''Driver Code'''
    action = ""
    locked = True
    people = 0
    while action != "END":
        action = input()
        if locked:
            if action == "C":
                locked = False
        else:
            if action =="P":
                locked = True
                people += 1
    print(people)
main()
