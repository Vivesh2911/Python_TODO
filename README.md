# 📝 To-Do List CLI App

*A simple, lightweight Python command-line To-Do manager with file storage.*

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue" />
  <img src="https://img.shields.io/badge/Status-Active-success" />
  <img src="https://img.shields.io/badge/Type-CLI App-orange" />
</p>

---

## 📌 Overview

This is a beginner-friendly **Command Line To-Do List Application** built with Python.
It allows users to:

* ➕ Add new tasks
* 📄 View all tasks
* ✔️ Mark tasks as completed
* 🗑️ Delete tasks
* 💾 Save & load tasks from a file

A simple and perfect project to practice Python fundamentals such as loops, functions, lists, and file handling.

---

## 🚀 Features

| Feature      | Description                             |
| ------------ | --------------------------------------- |
| Add Task     | Add a new task to your list             |
| View Tasks   | Display all tasks with numbering        |
| Mark as Done | Append a “✅ (Done)” tag to any task     |
| Delete Task  | Remove any task by selecting its number |
| Auto Save    | All updates are saved to `tasks.txt`    |
| Auto Load    | Tasks load automatically on startup     |

---

## 📂 Project Structure

```
📁 ToDo-CLI
 ├── todo.py         # Main program
 └── tasks.txt       # Auto-created file that stores tasks
```

---

## 🛠️ Installation & Usage

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/your-username/todo-cli.git
cd todo-cli
```

### **2️⃣ Run the Application**

```bash
python todo.py
```

---

## 🧠 Code Explanation

### **Main Functions**

* `load_tasks()` — Reads tasks from file
* `save_tasks(tasks)` — Saves tasks to file every update
* `show_tasks(tasks)` — Displays list with index
* Menu options run in a loop until user selects exit

### **Task File**

All tasks are saved in:

```
tasks.txt
```

Automatically created if missing.

---

## 📸 Sample Output

```
========== TO-DO LIST ==========
1. View Tasks
2. Add Task
3. Mark Task as Done
4. Delete Task
5. Exit
================================
Enter your choice (1-5):
```

---

## 🌱 Future Enhancements

* [ ] Add deadlines
* [ ] Add priority levels
* [ ] Add search feature
* [ ] Add colored terminal UI
* [ ] Convert to a GUI using Tkinter

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

