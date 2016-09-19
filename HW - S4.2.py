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

for key in prices:
    print(key)
    print(prices[key])
    print(stock[key])
    
total = 0

for key in prices:
    value = prices[key] * stock[key]
    total = total + value

print('if we sold all of them, we can earn totally is {0}'.format(total))
