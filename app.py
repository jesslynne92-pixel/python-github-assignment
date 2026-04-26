# Study Hours Tracker
# This program estimates weekly study hours

print("Welcome to my Python program!")

# user input section
hours = input("How many hours did you study today? ")

#calculation section
try:
    # Convert input to number
    hours = float(hours)

    # Calculate weekly hours
    weekly_hours = hours * 7

    # Display result
    print(f"You are on track to study {weekly_hours} hours this week.")

#output section
#error handling
except ValueError:
    print("Please enter a valid number.")