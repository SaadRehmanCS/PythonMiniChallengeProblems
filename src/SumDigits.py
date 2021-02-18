def sumDigits(n):
    sum = 0
    for i in range(len(n)):
        sum += eval(n[i])
    return sum


print(sumDigits("22222"))