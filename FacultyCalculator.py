# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result

print("Enter the operator you want want to solve" + ' +,-,/,*,%')
ope1= input()
print("Enter the 1st number")
num1 = int(input())
print("Enter the 2nd number")
num2 = int(input())
if num1==45 and num2==3 and ope1=='*':
    print("555")
elif num1==56 and num2==9 and ope1=='+':
    print("77")
elif num1==56 and num2==6 and ope1=='/':
    print("4")
elif ope1== '+':
    add= num1 + num2
    print(add)
elif ope1== '-':
    sub= num1 - num2
    print(sub)
elif ope1== '/':
    div= num1 / num2
    print(div)
elif ope1== '*':
    mul= num1 * num2
    print(mul)
elif ope1== '%':
    mod= num1 % num2
    print(mod)
else:
    print("Error, Check your number again")
