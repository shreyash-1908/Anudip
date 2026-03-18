# Question 23: Calculate electricity bill based on units consumed.
# Input: Enter units
# Output: Total bill amount

u = int(input())

if u <= 100:
    print(u * 5)
elif u <= 200:
    print(u * 7)
else:
    print(u * 10)