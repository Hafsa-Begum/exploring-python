print(f"""
Most countries use the metric system for recipe measurement, 
but American bakers use a different system. For example, they use 
fluid ounces to measure liquids instead of milliliters (ml).
    
So you need to convert recipe units to your local measuring system!
    
For example, 8 fluid ounces of milk is {8*29.5735:.2f} ml.
And 100ml of water is {100/29.5735} fluid ounces.""")
print(f"The temperature 75F in degrees Celsius is {((75 - 32) * 5 / 9):.2f}C")
# f""== used for fomated strings
# :.2f used for value taken after decimal point is two
print(f"Isabel is {28/7} dog years old.")
print(f"Isabel is {28/7:.0f} dog years old.")
print(f"I am {60} years old.")
print(f"There are {365/7:.3f} weeks in a year")
print(f"The area of a square with side 5 cm is {5**2} cm squared.")
print(f"The house was a good size: 1200 square feet, or {1200 * 0.092903:.2f} meters squared!")