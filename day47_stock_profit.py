# Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

# For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars


def stock_strategy(alist):
    r_max = [max(alist[i+1:]) if alist[i+1:] else alist[i] for i in range(len(alist))]
    return max([r_max[i] - alist[i] for i in range(len(alist))])


# print(stock_strategy([9, 20, 8, 5, 7, 10]))


def stock_strategy_multiple_transaction(alist):
    n = len(alist)
    if n <= 1:
        return None

    loc_min = []
    loc_max = []

    i = 0
    while (i < n - 1):
        if (i == n - 1):
            return None

        # local minima
        while (i < n - 1) and alist[i + 1] < alist[i]:
            i += 1
        buy = i
        loc_min.append(i)

        # local maxima
        i += 1
        while (i < n - 1) and alist[i + 1] > alist[i]:
            i += 1
        sell = i
        loc_max.append(i)

    for i in range(len(loc_min)):
        if alist[loc_min[i]] < alist[loc_max[i]]:
            print(f'buy on day {loc_min[i] + 1} at price {alist[loc_min[i]]}')
            print(f'sell on day {loc_max[i] + 1} at price {alist[loc_max[i]]}')

    return 0


# print(stock_strategy_multiple_transaction([9, 20, 8, 5, 7, 10]))
print(stock_strategy_multiple_transaction([100, 180, 260, 310, 40, 535, 535]))


