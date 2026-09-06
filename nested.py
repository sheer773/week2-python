# 3. Pattern with nested loops
for i in range(1, 6): # outer loop - rows
    for j in range(1, i+1): # inner loop - columns
        print("*", end=" ")
    print() # next line
