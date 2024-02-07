def day_of_week(day, month, year):
    # Months' codes from Zeller's Congruence
    month_codes = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    # Days of the week
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    if month < 3:
        year -= 1
    # Calculate the day of the week
    day_of_week = (year + year // 4 - year // 100 + year // 400 + month_codes[month - 1] + day) % 7
    
    return days[day_of_week]

# Example usage:
day = 9
month = 2
year = 2024

print(day_of_week(day, month, year))
