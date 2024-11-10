# maths functionality
import math

x = 99

square_root = math.sqrt(x)
print("Root is ", square_root)

rounded = round(square_root, 2)
print("Rounded to two decimal places", rounded)

# functions (args)
print(rounded)

# call a function
y = round(8.3436363, 3)
print(y)

print(round(4.44444, 1))

print(math.pow(2, 3))

print("----------------------------------")
name = "Shallon mAria"
print(len(name))
print(name.lower())
print(name.upper())
print(name.title())
print(name.capitalize())

post = "This thing is so easy and fluent"
new_post = post.replace("fluent", "flowing")
print(new_post)
