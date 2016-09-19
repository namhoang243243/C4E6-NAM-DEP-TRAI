buy = ["banana","orange", "apple"]

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
    }

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
    }

print('in Lulu store have: {0}'.format(stock))
print('all the prices is: {0}'.format(prices))
print('if you buy this: {0}'.format(buy))

def compute_bill(foods):
    total = 0
    for key in foods:
        if stock[key] > 0:
            print('you buyed {0}'.format(key))
            total = total + prices[key]
            stock[key] = stock[key] - 1
            
    return total

print('your total spend {0}'.format(compute_bill(buy)))
print('remain stuff in Lulu store is: {0}'.format(stock))
