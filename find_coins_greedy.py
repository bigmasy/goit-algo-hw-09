

def find_coins_greedy(sum):
    coins = [50, 25, 10, 5, 2, 1]
    change = {}
    for coin in coins:
        if sum >= coin:
            num_coins = sum // coin
            sum -= num_coins * coin
            change[coin] = num_coins
    return change

print(find_coins_greedy(113))
