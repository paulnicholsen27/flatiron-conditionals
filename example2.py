x = 10

if x > 20:
    x -= 10
elif x == 20:
    x += 3
else:
    x *= 5

print("The first value of x is: {}".format(x))  # what is the value of x here?

if x < 30:
    x += 5
elif x == 30:
    x -= 10
else:
    x = 42


print("The second value of x is: {}".format(x))  # what is the value of x here?
