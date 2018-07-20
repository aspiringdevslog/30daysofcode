def is_leap(year):
    leap = False
    
    # Write your logic here, I feel like this is terrible code
    if year%4==0:
        leap = True
        if year%100==0:
            leap = False
            if year%400==0:
                leap = True
            
    return leap