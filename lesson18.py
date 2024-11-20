name = input("What is your name? ")
print("My name is " + name )

# type conversion
birth_year = input("Enter your birth year: ")
age = 2024 - int(birth_year)
print(age)

first = float( input("First: "))
second = float( input("Second: "))
add = first + second
print("Sum: ", add )

course = 'Python for Beginners'
print(course.find('y'))
print(course.replace('for', '4'))

#instead of this
print(course.find('Python'))
# use
print('Python' in course)

# numbers = range(5, 10)
numbers = range(5, 10, 2)
# numbers = range(5)
for number in numbers:
    print(number)
