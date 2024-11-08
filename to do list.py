tlist = []
def show():
    print("\nTo-Do List Menu:")
    print("a. View task")
    print("b. Add task")
    print("c. Remove task")
    print("d. Exit")

def view():
    if not tlist:
        print("Your to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tlist, start=1):
            print(f"{index}. {task}")

def add():
    task = input("Enter a new task: ")
    tlist.append(task)
    print(f"'{task}' has been added to your to-do list.")

def remove_task():
    try:
        view()
        task_num = int(input("Enter the task number to remove: "))
        removed_task = tlist.pop(task_num - 1)
        print(f"'{removed_task}' has been removed from your to-do list.")
    except (ValueError, IndexError):
        print("Invalid task number. Please try again.")

while True:
    show()
    choice = input("Choose an option (a/b/c/d): ")

    if choice == 'a':
        view()
    elif choice == 'b':
        add()
    elif choice == 'c':
        remove_task()
    elif choice == 'd':
        print("Thankyou")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
