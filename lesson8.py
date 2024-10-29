# Dictionary
# list[], tuple (), dictionary {}
student = {"name": "Jane Sarah", "id": 1234, "age": 21, "gender": "F"}

print(student)
print(student["name"]) # key

student["weight"] = 61
print(student)

# set -- only one existence per item, unordered--order keeps changing
people = {"Jane", "Bill", "Kevo", "Said", "Jane"}
print(people)
people.add("Willy")
print(people)
print(len(people))
people.discard("Kevo")
print(people)