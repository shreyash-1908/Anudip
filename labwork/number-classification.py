def classify(num):
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

    if num != 0:
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")

arr = list(map(int, input("Enter numbers: ").split()))

for num in arr:
    classify(num)