

def find_min_coins(sum):
    coins = [1, 2, 5, 10, 25, 50]
    
    K = [float('inf')] * (sum + 1)
    last_coin = [-1] * (sum + 1)
    
    K[0] = 0

    for i in range(1, sum + 1):
        for coin in coins:
            if i - coin >= 0 and K[i - coin] + 1 < K[i]:
                K[i] = K[i - coin] + 1
                last_coin[i] = coin

    result = {}
    if K[sum] == float('inf'):
        return {}
    
    current_amount = sum
    while current_amount > 0:
        coin = last_coin[current_amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_amount -= coin
    
    return result

print(find_min_coins(113))
