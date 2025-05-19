# input = input('x:')
# y = int(input) + 1
# print(y)


# Falsy values
# ""
# 0
# None

# if elif else loop
temperature = 15
if (temperature > 30):
    print('hot')
elif temperature > 20:
    print('its a good weather')
else:
    print('its fucking cold')

print('anyway i m not going out😶')

# operators
# a nd or not


# for loop/for else
success = False
for number in range(1, 4):  # range(where it starts ,where it ends)
    print('attack', number)
    if success:
        print('success')
        break
else:
    print('nehi hoga tere se laude')

count = 0
for number in range(1, 10):

    if ((number % 2) == 0):
        print(number)
        count += 1
print(f"this item is called {count} times")
