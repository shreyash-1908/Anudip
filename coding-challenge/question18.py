# Question 18: Calculate electricity bill based on units consumed.
# Input: Enter units
# Output: Total bill amount

units = int(input("Enter units: "))
i = 0
bill = 0

while i < units:
    if i < 100:
        bill += 5
    elif i < 200:
        bill += 7
    else:
        bill += 10
    i += 1

print("Total Bill:", bill)