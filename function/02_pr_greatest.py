def maximum(num1, num2, num3):
    if(num1>num2):
        if((num1>num3)):
            return num1
        else:
            return num2
    else:
        if(num2>num3):
            return num2
        else:
            return num3
m = maximum(34,700,79)
print("max. of number is " + str(m))