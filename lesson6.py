# list
scores = [90, 65, 34, 71, 55, 77, 89]

# access a value
print(scores[0]) # first
print(scores[2]) # third

#add
scores.append(61)
print(scores)

# remove
scores.pop(3)
print(scores)

scores.sort()
print(scores)

scores.sort(reverse=True)
print(scores)
print(len(scores))

print(scores[0:3])
scores.insert(0,10)
scores.remove(2)
print(10 in scores)