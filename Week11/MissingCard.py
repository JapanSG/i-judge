'''MissingCard'''
def get_deck() -> set:
    '''Get all card in deck'''
    deck = {}
    for sym in "CDHS":
        for num in list(map(str,range(2,11))) + ["A","K","Q","J"]:
            deck[f"{num}{sym}"] = 1
    return set(deck.keys())
def main():
    '''Driver Code'''
    cards = set()
    for _ in range(51):
        cards.add(input())
    for card in get_deck().difference(cards):
        print(card)
if __name__ == "__main__":
    main()
