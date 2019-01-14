first=int(input('enter 1st number:'))
print(type(first))
second=int(input("enter second number:"))
operator=input("enter the operator:")
print(type(operator))
if operator == '+':
    sum=first + second
    print('the sum is',sum)
elif operator=='-':
    diff=first - second
    print('the diff is',diff)
elif operator=='*':
    mul=first * second
    print('the multiplication is',mul)

else:
    division=float(first / second)
    print('the division is',division)

print('please give valid input')