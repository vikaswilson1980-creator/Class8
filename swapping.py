print("Value before Swapping:")
value1 = int(input("\nEnter a Value1: "))
value2 = int(input("Enter a Value2: "))
value3 = int(input("Enter a Value3: "))

# Perform actual swapping (circular shift)
value1, value2, value3 = value2, value3, value1

print("\nValues after Swapping:")
print("Value1 =", value1)
print("Value2 =", value2)
print("Value3 =", value3)
