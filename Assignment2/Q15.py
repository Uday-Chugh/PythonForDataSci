import math

n = int(input("Enter the value of n upto which sum of series is required: "))
sum = (2/81) * ((10*math.pow(10, n) - 1 )- (9 * n))
print("The sum of series is:" , sum)
