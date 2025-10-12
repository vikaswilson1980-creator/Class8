print("Enter a number numerator")
num=int(input())
print("Enter a number denominator")
num2=int(input())
if(num%num2==0):
    print("\n"+str(num)+"Is divisible by"+str(num2))
else:
    print("\n"+str(num)+"Is not divisible by"+str(num2))