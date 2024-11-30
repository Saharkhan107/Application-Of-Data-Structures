# Initialize the to-do list as an empty list
to_do_list = []

# Function to add a task with a given priority
def add_task(priority, task):
    to_do_list.append((priority, task))

# Function to display all tasks, sorted by priority
def show_tasks():
    if not to_do_list:
        print("No tasks available.")
        return
    print("\nTo-Do List:")
    # Sort tasks by priority and display them
    for priority, task in sorted(to_do_list):
        print(f"Priority: {priority}, Task: {task}")

# Function to mark a task as completed by removing it from the list
def complete_task(task):
    global to_do_list
    # Filter out the task that matches the given task description
    to_do_list = [t for t in to_do_list if t[1] != task]

# Example usage:

# Adding tasks with different priorities
add_task(1, "Finish lab report")  # High priority
add_task(3, "Go grocery shopping")  # Low priority
add_task(2, "Call mom")  # Medium priority

# Displaying tasks before marking any as completed
show_tasks()

# Completing the "Call mom" task
complete_task("Call mom")

# Displaying tasks after completing one
show_tasks()

