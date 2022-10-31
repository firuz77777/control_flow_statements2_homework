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
    elif temp <= 10:
        a = "Very Cold"
    elif temp > 10 and temp <= 20:
        a = "Cold"
    elif temp > 20 and temp <= 30:
        a = "Normal" 
    elif temp > 30 and temp <= 40:
        a = "Hot"
    elif temp > 40:
        a = "Very Hot"
    return a