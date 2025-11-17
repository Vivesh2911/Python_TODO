# Objective
# Create a simple command-line To-Do List application where a user can:
# Add new tasks
# View all tasks
# Mark tasks as completed
# Delete tasks
# Save and load tasks from a file

TASKS_FILE = "tasks.txt"

#------Helper Function-----#

def load_tasks():
  try:
    with open(TASKS_FILE , "r") as f:
      tasks = [line.strip() for line in f.readlines()]
    return tasks
  except FileNotFoundError:
    return []
# print(load_task())

def save_tasks(tasks):
  with open(TASKS_FILE , "w") as f:
    for task in tasks:
      f.write(task+"\n")
      
def show_tasks(tasks):
  if not tasks:
    print("\n No Tasks Available")
  else:
    print("\n Your Tasks")
    for i, task in enumerate(tasks , start =1):
      print(f"{i} . {task}")
    
# ---------- Main Menu ----------
def main():
    tasks = load_tasks()

    while True:
        print("\n========== TO-DO LIST ==========")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        print("================================")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            show_tasks(tasks)

        elif choice == '2':
            task = input("Enter new task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
                print(f"✅ Task '{task}' added successfully!")
            else:
                print("⚠️ Task cannot be empty!")

        elif choice == '3':
            show_tasks(tasks)
            try:
                num = int(input("Enter task number to mark as done: "))
                if 1 <= num <= len(tasks):
                    tasks[num - 1] += " ✅ (Done)"
                    save_tasks(tasks)
                    print("🎉 Task marked as done!")
                else:
                    print("⚠️ Invalid task number!")
            except ValueError:
                print("⚠️ Please enter a valid number.")

        elif choice == '4':
            show_tasks(tasks)
            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    save_tasks(tasks)
                    print(f"🗑️ Task '{removed}' deleted successfully!")
                else:
                    print("⚠️ Invalid task number!")
            except ValueError:
                print("⚠️ Please enter a valid number.")

        elif choice == '5':
            print("👋 Exiting... Your tasks are saved!")
            save_tasks(tasks)
            break

        else:
            print("⚠️ Invalid choice! Please select 1–5.")

# ---------- Run the program ----------
if __name__ == "__main__":
    main()