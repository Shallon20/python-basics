# multiple key values using dictionary
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total
print(multiply(2, 3, 4, 5))

# **args
def save_user(**user):
    print(user)
save_user(id=1, name='John', age=22)

# global variables are not good as they can create bugs

# scope
def greet():
    message = "a"
# not in scope
# print(message)

# greet("Mosh")

def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input

print(fizz_buzz(3))


