## BVN1 Session 3

colors = ['blue', 'red', 'black', 'pink', 'brown', 'yellow']

print("My colors list: ", colors)
print("color_list at index 3: ", colors[3])

i = int(input("Enter your number from 0-5: "))
print("Your color: ", colors[i])

print(colors)
for _ in range(5):
    print(colors[_])

while True:
    fav = input('What is your favorite color? ')
    found=False
    for i in range(len(colors)):
        x = colors[i]
        if fav == x:
            found=True
            break   
    if found:
        print('Your color is in index {0} in my list '.format(i))
    if not found:
        print('Sorry, I counld not find your color')


