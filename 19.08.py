# 3digit armstrong number
num = int(input("Enter a 3-digit number: "))

temp = num
sum_val = 0

while temp > 0:
    digit = temp % 10
    sum_val += digit ** 3 
    temp //= 10

if sum_val == num:
    print(num, "is a 3-digit Armstrong number")
else:
    print(num, "is not a 3-digit Armstrong number")


# 4digit armstrong number
num1 = int(input("Enter a 4-digit number: "))
temp = num1
sum_val = 0

while temp > 0:
    digit = temp % 10
    sum_val += digit ** 4   
    temp //= 10

if sum_val == num1:
    print(num1, "is a 4-digit Armstrong number")
else:
    print(num1, "is not a 4-digit Armstrong number")
