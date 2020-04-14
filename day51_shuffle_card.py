# Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

# It should run in O(N) time.

# Hint: Make sure each one of the 52! permutations of the deck is equally likely.
import random

def card_shuffle(alist):
    tot = len(alist)
    i = tot - 2

    while i > 0:
        candidate = random.randint(0, i)
        alist[candidate], alist[i + 1] = alist[i + 1], alist[candidate]
        i -= 1
    return 1

cards = list(range(1, 52))
# card_shuffle(cards)
# print(cards)


def card_shuffle_geek(arr):
    n = len(arr)
    for i in range(n-1,0,-1):
        # Pick a random index from 0 to i
        j = random.randint(0,i+1)

        # Swap arr[i] with the element at random index
        arr[i],arr[j] = arr[j],arr[i]
    return arr

print(card_shuffle_geek(cards))
