## BVN2 Sesson 3

ship = [5, 7, 300, 90, 24, 50, 75]

print('Hello, my name is Nam and these are my ship size:',ship)


for mo in range (1,5):

    print('Month {0}'.format(mo))
    ship = [ s+50 for s in ship]
    print('One month has passed, here is my floak', ship)
    m = max(ship)
    print("Now my biggest ship has size {0} let's share it".format(m))
    
    i = ship.index(max(ship))
    ship.insert(i, 8)
    ship.remove(m)
    
    print('After shearing, here is my floak:', ship)

s = 0
for _ in range(len(ship)):
    s+= ship[_]

print('My floak size now in total:', s)
money = s*2
print('I would get {0} * $2 = ${1}'.format(s,money))
