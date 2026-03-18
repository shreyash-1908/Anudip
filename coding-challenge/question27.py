# Question 27: Check whether a person is eligible to vote.
# Input: Enter age
# Output: Eligible / Not Eligible

def is_eligible(age):
    if age >= 18:
        return "Eligible"
    return "Not Eligible"

age = int(input("Enter age: "))
print(is_eligible(age))
