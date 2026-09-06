# 3. Pattern with nested loops
for i in range(1, 6): # outer loop - rows
    for j in range(1, i+1): # inner loop - columns
        print("*", end=" ")
    print() # next line


# 4. Largest and Smallest
numbers = [12, 45, 2, 67, 23, 90, 11]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)


# 5. Sort using lambda key

# Example 1: Sort by length
names = ["Raju", "Siri", "Abhilash", "Kiran"]
names.sort(key=lambda x: len(x))
print("Sort by length:", names)

# Example 2: Sort list of tuples by second value
students = [("Ravi", 85), ("Siri", 92), ("Raju", 78)]
students.sort(key=lambda x: x[1]) # marks tho sort
print("Sort by marks:", students)

