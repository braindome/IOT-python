tasks = []

def show_menu():
  print("\n1. Add task")
  print("2. View tasks")
  print("3. Remove task")
  print("4. Exit")

while True:
  show_menu()
  choice = input("Choose an option: ")
  if choice == "1":
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")
  elif choice == "2":
    print("\nYour tasks:")
    for i, task in enumerate(tasks, 1):
      print(f"{i}. {task}")
  elif choice == "3":
    num = int(input("Enter task number to remove: "))
    if 1 <= num <= len(tasks):
      removed = tasks.pop(num - 1)
      print(f"Removed: {removed}")
    else:
      print("Invalid number.")
  elif choice == "4":
    print("Goodbye!")
    break
  else:
    print("Invalid choice.")