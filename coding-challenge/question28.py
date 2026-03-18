# Question 28: Calculate electricity bill based on units consumed.
# Input: Enter unitsOutput: Total bill amount

def bill(u):
    if u <= 100:
        return u * 5
    elif u <= 200:
        return u * 7
    return u * 10

print(bill(int(input())))