# 📒 Contact Book CLI (Python)

A simple command-line based Contact Book application built using Python.
This project allows users to manage contacts with features like adding, viewing, searching, editing, and deleting contacts. Data is stored persistently using a JSON file.

---

## 🚀 Features

* ➕ Add new contacts with validation
* 📋 View all saved contacts
* 🔍 Search contacts by name
* ✏️ Edit existing contact details
* ❌ Delete contacts
* 💾 Persistent storage using JSON file

---

## 🛠️ Technologies Used

* Python 3
* JSON (for data storage)

---

## 📂 Project Structure

```
ContactBook/
│
├── main.py          # Main program (your CLI logic)
├── data.py          # Handles loading & saving contacts
├── contacts.json    # Stores contact data
└── README.md        # Project documentation
```

---

## ⚙️ How It Works

* Contacts are stored as a list of dictionaries:

```python
{
    "Name": "ayesha",
    "Phone": "9876543210"
}
```

* Data is automatically saved and loaded using JSON.

---

## ▶️ How to Run

1. Make sure Python is installed
2. Clone the repository
3. Run the program:

```
python main.py
```

---

## 📌 Menu Options

```
1. Add Contact
2. View Contact
3. Search Contact
4. Delete Contact
5. Edit Contact
6. Exit
```

---

## ✅ Validation Rules

* Names must contain only alphabets
* Phone numbers must:

  * Be exactly 10 digits
  * Contain only numbers
  * Not have all identical digits (e.g. 0000000000 is invalid)

---

## ⚠️ Limitations

* No duplicate name handling during edit (can be improved)
* Search uses partial matching (may return multiple results)
* CLI-based only (no GUI)

---

## 🔮 Future Improvements

* Add email field
* Add duplicate handling improvements
* Build GUI using Tkinter or Web App
* Add sorting & filtering

---

## 👩‍💻 Author

Ayesha – AIML Student

---

## 📜 License

This project is open-source and free to use.
