def caught_speeding(speed, is_birthday):
    # Define the speed limits
    if is_birthday:
        speed -= 5  # Adjust the speed limit if it's your birthday

    if speed <= 60:
        return "No Challan"
    elif 61 <= speed <= 80:
        return "Small Challan"
    else:
        return "Heavy Challan"

# Test cases
print(caught_speeding(81, True))  # Output: "Small Challan" (birthday, so speed limit is 81 - 5 = 76)
print(caught_speeding(81, False)) # Output: "Heavy Challan" (no birthday, so speed limit is 81)
