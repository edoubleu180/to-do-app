from todo import TodoManager
from storage import Storage

def menu():
    print("\n=== TO‑DO APP ===")
    print("1. Add task")
    print("2. List tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")

def main():
    manager = TodoManager(Storage())

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            desc = input("Task description: ")
            task = manager.add_task(desc)
            print(f"Added: {task}")

        elif choice == "2":
            tasks = manager.list_tasks()
            print("\nYour Tasks:")
            for t in tasks:
                status = "✔" if t["done"] else "✘"
                print(f"{t['id']}. {t['description']} [{status}]")

        elif choice == "3":
            task_id = int(input("Task ID to complete: "))
            task = manager.complete_task(task_id)
            print("Task completed!" if task else "Task not found.")

        elif choice == "4":
            task_id = int(input("Task ID to delete: "))
            manager.delete_task(task_id)
            print("Task deleted.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
