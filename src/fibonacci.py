def fibonacci(num):
    temp1 = 0
    temp2 = 0
 #   temp3 = 0
    temp3 = []

    for var in range(num):
        if var < 2:
            print var
            temp3.append(var)
            temp1 = var
        else:
            temp3.append(temp1 + temp2)
            print temp3[var]
            temp2 = temp1
            temp1 = temp3[var]
    return temp3
                   
print fibonacci(10)