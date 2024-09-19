# daily_reminder.py

# Prompt the user to input a task description
task = input("Enter your task: ")

# Prompt for the task's priority
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Provide a customized reminder based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"'{task}' is a high-priority task."
    case "medium":
        reminder = f"'{task}' is a medium-priority task."
    case "low":
        reminder = f"'{task}' is a low-priority task."
    case _:
        reminder = f"'{task}' has an unknown priority."

# Modify the reminder if the task is time-sensitive
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."

# Print the final reminder
print(f"Reminder: {reminder}")
