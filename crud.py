# 1. CRUD Operations on List
fruits = ["apple", "banana", "mango"]

# C - Create / Add
fruits.append("orange")
print("After Create:", fruits)

# R - Read
print("Reading:")
for item in fruits:
    print(item)

# U - Update
fruits[1] = "grapes" 
print("After Update:", fruits)

# D - Delete
fruits.remove("mango")
print("After Delete:", fruits)

fruits.pop() 
print("After pop:", fruits)
