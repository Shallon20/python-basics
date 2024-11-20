# loops
from zmq.backend import first

for number in range(1, 10, 2):
    print("Attempt", number, number * ".")

successful = True
for num in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break

else:
    print("Attempted 3 times and failed")


# nested loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

# lists
numbers = list(range(20))
# print(numbers)
# print(numbers[::2])
print(numbers[::-1])

# unpacking
m = [1, 2, 3, 4, 4, 4, 9]
first, *other, last = m
print(first, last)
print(other)

# list looping
letters = ["a", "b", "c"]
items = (0, "a")
index, letter = items
for index, letter in enumerate(letters):
    print(index, letter)


# add
letters.append("d")
letters.insert(0, "-")

# remove
letters.pop(0)
letters.remove("b")
# del letters[0:3] # removes a range of items
# letters.clear()
print(letters)

# find index
print(letters.count("c"))
if "c" in letters:
    print(letters.index("c"))