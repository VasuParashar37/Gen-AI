items = ["mango","banana","apple","orange","plum","apple"]

unique = set()

for item in items:
    if item in unique:
        print("Found Duplicate:",item)
        break
    else:
        unique.add(item)

