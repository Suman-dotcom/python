def calculate_slope(x1,x2,y1,y2):
    if x1 == x2:
        return "invalid input"
    else:
        slope= (y2-y1)/(x2-x1)
        return slope


y1,y2 = 1,2
x1,x2 = 3,4
slope = calculate_slope(x1,x2,y1,y2)
print("slope is: ",slope)