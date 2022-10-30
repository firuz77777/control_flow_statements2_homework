def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Use the elif statments.
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"
    Args:
        temp: Temperature in Celsius.
    Returns:
        str: return answer.
    """
    a = 0
    if temp == 0:
        a = "Freezing"
    elif temp == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10:
        a = "Very Cold"
    elif temp == 11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20:
        a = "Cold"
    elif temp == 21 or 22 or 23 or 24 or 25 or 26 or 27 or 28 or 29 or 30:
        a = "Normal"
    elif temp == 31 or 32 or 33 or 34 or 35 or 36 or 37 or 38 or 39 or 40:
        a = "Hot"
    elif temp > 40:
        a = "Very Hot"
    return a