# daily_reminder.py

# Prompt the user to input a task description
task = input("Enter a task: ")

# Prompt for the task’s priority
priority = input("Enter the task's priority (high, medium, low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Provide a customized reminder based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"Your task: '{task}' is a high-priority task."
    case "medium":
        reminder = f"Your task: '{task}' is a medium-priority task."
    case "low":
        reminder = f"Your task: '{task}' is a low-priority task."
    case _:
        reminder = f"Your task: '{task}' has an unknown priority."

# Modify the reminder if the task is time-sensitive
if time_bound == "yes":
    reminder += " This requires immediate attention today!"

# Print the final reminder
print(reminder)
