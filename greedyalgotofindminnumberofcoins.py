denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]


def findMinimumCoins(amount):
    coins = denominations
    coins.sort(reverse=True)

    i = 0
    c = 0
    while amount > 0:
        if i >= len(coins):
            return (-1)
            break
        if (amount-coins[i] >= 0) and (coins[i] < amount or coins[i] == amount):
            amount -= coins[i]
            c += 1
        else:
            i += 1
        # amount -= 1
    return (c)
    # Write your code here
    pass
