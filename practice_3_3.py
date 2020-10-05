calendar_years = int(input("Enter calendar years: "))
if calendar_years < 0:
    raise Exception("Please enter positive value")
if calendar_years <= 2:
    dog_years = calendar_years * 10.5
elif calendar_years > 2:
    dog_years = 10.5 * 2 + (calendar_years - 2) * 4
print("Dog years =", dog_years)
