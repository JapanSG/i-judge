'''MissingCard_No_Set'''
def get_deck() -> list:
    '''Get all card in deck'''
    deck = {}
    for sym in "CDHS":
        for num in list(map(str,range(2,11))) + ["A","K","Q","J"]:
            deck[f"{num}{sym}"] = 1
    return deck
def main():
    '''Driver Code'''
    deck = get_deck()
    for _ in range(51):
        deck.pop(input())
    for card in deck:
        print(card)
if __name__ == "__main__":
    main()
