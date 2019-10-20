i = 0
numbers = []

def counting_fcn(upperbound):
    for i in range (0, upperbound):
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    return numbers

print("What is the top number you want")
topnum = int(input("> "))
numbersout = counting_fcn(topnum)

print("The numbers")

for num in numbersout:
    print(num)