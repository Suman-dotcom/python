def check_season(month):
    if month in [1,2,3]:
        return "winter"
    elif month in [4,5,6]:
        return "spring"
    elif month in [7,8,9]:
        return "summer"
    elif month in [10,11,12]:
        return "autumn"
    else:
        return "invalid input"
        
        


month = int(input("enter month number: "))
print(check_season(month))