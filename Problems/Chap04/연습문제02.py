def operate (*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum / len(numbers)

print(operate(1,2,3,4,5))