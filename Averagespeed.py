speed1 = int(input("Enter speed1:"))
speed2 = int(input("Enter speed2:"))
speed3 = int(input("Enter speed3:"))
average = (speed1+speed2+speed3)/3
print("The average speed of the car is:",average)
if(average>speed1 and average>speed2 and average>speed3):
    print("%d is higher then %d,%d,%d"%(average,speed1,speed2,speed3))
elif(average>speed1 and average>speed2):
    print("%d is higher then %d,%d"%(average,speed1,speed2))
elif(average>speed1 and average>speed3):
    print("%d is higher then %d,%d"%(average,speed1,speed3))
elif(average>speed2 and average>speed3):
    print("%d is higher then %d,%d"%(average,speed2,speed3))
elif(average>speed1):
    print("%d is higher then %d"%(average,speed1))
elif(average>speed2):
    print("%d is higher then %d"%(average,speed2))
elif(average>speed3):
    print("%d is higher then %d"%(average,speed3))
else:
    print("Invalid input")