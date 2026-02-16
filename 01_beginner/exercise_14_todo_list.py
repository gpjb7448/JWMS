"""
Exercise 14: Simple Todo List
Create a basic task management system

STEP-BY-STEP GUIDE:
===================
1. Create a list to store tasks
2. Each task is a dictionary with: title, completed status, priority
3. Implement CRUD operations (Create, Read, Update, Delete)
4. Add features: mark complete, set priority, filter tasks
5. Display tasks in a formatted way

LEARNING OBJECTIVES:
- Working with lists and dictionaries
- Data structure design
- User input validation
- String formatting
- Conditional logic
"""


def create_task(title, priority="Medium"):
    """
    Create a new task dictionary
    
    STEP 1: Create dictionary structure
    STEP 2: Set initial values
    STEP 3: Return the task object
    
    Args:
        title (str): Task title
        priority (str): Priority level (High/Medium/Low)
        
    Returns:
        dict: Task dictionary
    """
    return {
        'title': title,
        'completed': False,
        'priority': priority
    }


def display_tasks(tasks, filter_by=None):
    """
    Display all tasks ina formatted table
    
    STEP 1: Check if tasks list is empty
    STEP 2: Filter tasks if needed
    STEP 3: Format and print each task
    
    Args:
        tasks (list): List of task dictionaries
        filter_by (str): Filter option ('completed', 'pending', 'high', 'medium', 'low')
    """
    if not tasks:
        print("\n📝 No tasks yet! Add your first task.")
        return
    
    # STEP 1: Apply filter if specified
    filtered_tasks = tasks
    if filter_by == 'completed':
        filtered_tasks = [t for t in tasks if t['completed']]
    elif filter_by == 'pending':
        filtered_tasks = [t for t in tasks if not t['completed']]
    elif filter_by in ['high', 'medium', 'low']:
        filtered_tasks = [t for t in tasks if t['priority'].lower() == filter_by]
    
    if not filtered_tasks:
        print(f"\n📝 No tasks found for filter: {filter_by}")
        return
    
    # STEP 2: Display header
    print("\n" + "=" * 80)
    print("TODO LIST".center(80))
    print("=" * 80)
    print(f"{'#':<4} {'Status':<10} {'Priority':<10} {'Task':<50}")
    print("-" * 80)
    
    # STEP 3: Display each task
    for idx, task in enumerate(filtered_tasks, 1):
        # Determine status icon
        status = "✓ Done" if task['completed'] else "○ Pending"
        
        # Determine priority icon
        priority_icons = {
            'High': '🔴 High',
            'Medium': '🟡 Medium',
            'Low': '🟢 Low'
        }
        priority = priority_icons.get(task['priority'], task['priority'])
        
        # Print task row
        print(f"{idx:<4} {status:<10} {priority:<10} {task['title']:<50}")
    
    print("=" * 80)
    print(f"Total: {len(filtered_tasks)} task(s)")
    
    # STEP 4: Display summary statistics
    completed = sum(1 for t in tasks if t['completed'])
    pending = len(tasks) - completed
    print(f"Completed: {completed} | Pending: {pending}")
    print("=" * 80)


def add_task(tasks):
    """
    Add a new task to the list
    
    STEP 1: Get task title from user
    STEP 2: Get priority level
    STEP 3: Create task object
    STEP 4: Add to tasks list
    STEP 5: Confirm to user
    """
    print("\n" + "=" * 60)
    print("Add New Task".center(60))
    print("=" * 60)
    
    # STEP 1: Get task title
    title = input("\nEnter task title: ").strip()
    
    if not title:
        print("❌ Task title cannot be empty!")
        return
    
    # STEP 2: Get priority
    print("\nPriority:")
    print("1. High")
    print("2. Medium (default)")
    print("3. Low")
    
    priority_choice = input("Select priority (1-3, Enter for default): ").strip()
    
    # STEP 3: Map choice to priority level
    priority_map = {
        '1': 'High',
        '2': 'Medium',
        '3': 'Low'
    }
    priority = priority_map.get(priority_choice, 'Medium')
    
    # STEP 4: Create and add task
    task = create_task(title, priority)
    tasks.append(task)
    
    # STEP 5: Confirm
    print(f"\n✅ Task added: '{title}' (Priority: {priority})")


def mark_complete(tasks):
    """
    Mark a task as complete
    
    STEP 1: Display all tasks
    STEP 2: Get task number from user
    STEP 3: Validate input
    STEP 4: Toggle completion status
    STEP 5: Confirm to user
    """
    if not tasks:
        print("\n📝 No tasks to complete!")
        return
    
    # STEP 1: Show tasks
    display_tasks(tasks, filter_by='pending')
    
    try:
        # STEP 2: Get task number
        task_num = int(input("\nEnter task number to mark complete: "))
        
        # STEP 3: Validate
        if 1 <= task_num <= len(tasks):
            # STEP 4: Toggle completion
            task = tasks[task_num - 1]
            task['completed'] = not task['completed']
            
            # STEP 5: Confirm
            status = "completed" if task['completed'] else "marked as pending"
            print(f"✅ Task {status}: '{task['title']}'")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number!")


def delete_task(tasks):
    """
    Delete a task from the list
    
    STEP 1: Display all tasks
    STEP 2: Get task number to delete
    STEP 3: Confirm deletion
    STEP 4: Remove task
    STEP 5: Confirm to user
    """
    if not tasks:
        print("\n📝 No tasks to delete!")
        return
    
    # STEP 1: Show tasks
    display_tasks(tasks)
    
    try:
        # STEP 2: Get task number
        task_num = int(input("\nEnter task number to delete: "))
        
        # STEP 3: Validate
        if 1 <= task_num <= len(tasks):
            task = tasks[task_num - 1]
            
            # STEP 4: Confirm deletion
            confirm = input(f"Delete '{task['title']}'? (y/n): ").lower()
            
            if confirm == 'y':
                # STEP 5: Remove and confirm
                deleted_task = tasks.pop(task_num - 1)
                print(f"✅ Deleted: '{deleted_task['title']}'")
            else:
                print("Cancelled.")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number!")


def edit_task(tasks):
    """
    Edit an existing task
    
    STEP 1: Display all tasks
    STEP 2: Select task to edit
    STEP 3: Choose what to edit (title or priority)
    STEP 4: Update the task
    STEP 5: Confirm changes
    """
    if not tasks:
        print("\n📝 No tasks to edit!")
        return
    
    display_tasks(tasks)
    
    try:
        task_num = int(input("\nEnter task number to edit: "))
        
        if 1 <= task_num <= len(tasks):
            task = tasks[task_num - 1]
            
            print("\nWhat to edit?")
            print("1. Title")
            print("2. Priority")
            
            choice = input("Enter choice: ")
            
            if choice == '1':
                new_title = input(f"Current: '{task['title']}'\nNew title: ").strip()
                if new_title:
                    task['title'] = new_title
                    print("✅ Title updated!")
            elif choice == '2':
                print("\n1. High")
                print("2. Medium")
                print("3. Low")
                priority_choice = input("Select new priority: ")
                priority_map = {'1': 'High', '2': 'Medium', '3': 'Low'}
                if priority_choice in priority_map:
                    task['priority'] = priority_map[priority_choice]
                    print("✅ Priority updated!")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number!")


def main():
    """
    MAIN PROGRAM FLOW:
    ==================
    1. Initialize empty task list
    2. Display menu
    3. Process user choice
    4. Repeat until user exits
    
    PROGRAM STRUCTURE:
    - tasks list: stores all task dictionaries
    - Each iteration: show menu, get choice, execute action
    - Continues until user selects exit
    """
    # STEP 1: Initialize data structure
    tasks = []
    
    # STEP 2: Main program loop
    while True:
        # Display menu
        print("\n" + "=" * 60)
        print("TODO LIST MANAGER".center(60))
        print("=" * 60)
        print("1. View All Tasks")
        print("2. View Pending Tasks")
        print("3. View Completed Tasks")
        print("4. Add Task")
        print("5. Mark Complete/Incomplete")
        print("6. Edit Task")
        print("7. Delete Task")
        print("8. Clear All Completed Tasks")
        print("9. Exit")
        print("=" * 60)
        
        # STEP 3: Get user choice
        choice = input("\nEnter your choice (1-9): ")
        
        # STEP 4: Process choice
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            display_tasks(tasks, filter_by='pending')
        elif choice == "3":
            display_tasks(tasks, filter_by='completed')
        elif choice == "4":
            add_task(tasks)
        elif choice == "5":
            mark_complete(tasks)
        elif choice == "6":
            edit_task(tasks)
        elif choice == "7":
            delete_task(tasks)
        elif choice == "8":
            completed_tasks = [t for t in tasks if t['completed']]
            if completed_tasks:
                confirm = input(f"Delete {len(completed_tasks)} completed task(s)? (y/n): ")
                if confirm.lower() == 'y':
                    tasks[:] = [t for t in tasks if not t['completed']]
                    print(f"✅ Deleted {len(completed_tasks)} completed task(s)")
            else:
                print("No completed tasks to delete!")
        elif choice == "9":
            print("\n👋 Goodbye! Stay productive!")
            break
        else:
            print("\n❌ Invalid choice! Please select 1-9.")


if __name__ == "__main__":
    """
    ENTRY POINT
    
    This block only executes when running the script directly.
    Allows the module to be imported without auto-running.
    """
    main()
