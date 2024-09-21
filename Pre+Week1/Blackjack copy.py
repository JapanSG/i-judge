"""BlackJack"""
n = int(input())
cards = []
SCORE = 0
NUMA = 0
for _ in range(n) :
    _ += 1
    _ -= 1
    cards.append((input()))
for j in range(n) :
    if cards[j] == "A" :
        SCORE += 11
        NUMA = NUMA+1
    elif cards[j] == "Q" or cards[j] == "K" or cards[j] == "J" :
        SCORE += 10
    else :
        SCORE = int(cards[j]) + SCORE
if SCORE > 21 and NUMA > 0:
    currScore = SCORE
    for _ in range(NUMA) :
        _ += 1
        _ -= 1
        currScore -= 10
        if SCORE > 21 :
            SCORE = currScore
        else :
            break
print(SCORE)
