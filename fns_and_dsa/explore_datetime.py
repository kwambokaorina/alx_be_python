
from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in the format 'YYYY-MM-DD HH:MM:SS'.
    """
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format the date
    return f"Current Date and Time: {formatted_date}"

def calculate_future_date(days):
    """
    Calculate and display the future date after adding the specified number of days to the current date.
    
    Parameters:
    days (int): The number of days to add to the current date.
    """
    current_date = datetime.now()  # Get the current date and time
    future_date = current_date + timedelta(days=days)  # Calculate the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format the future date
    return f"Future Date (after {days} days): {formatted_future_date}"

def main():
    # Part 1: Display the current date and time
    display_current_datetime()

    # Part 2: Calculate a future date
    try:
        days = int(input("\nEnter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        return "Invalid input. Please enter an integer value for the number of days."

if __name__ == "__main__":
    main()
