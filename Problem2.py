# Sum of fibonacci series less than 40000000

a = 1
b = 1
i = 0
sum = 0
while i < 50:
    a, b = b, a+b
    if a%2 == 0:
        print(a)
        sum += a
    if a > 4000000:
        break
    i += 1
print("sum is ", sum)
