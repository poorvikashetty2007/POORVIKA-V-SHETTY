cities = {
    "Mumbai": "India",
    "Chennai": "India",
    "Delhi": "India",
    "Sydney": "Australia",
    "Dubai": "UAE"
}
city1 = input("Enter the first city: ").title()
city2 = input("Enter the second city: ").title()
if city1 in cities and city2 in cities:
    if cities[city1] == cities[city2]:
        print("Both cities are in", cities[city1])
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities are not in the list")
    