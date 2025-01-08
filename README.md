# Expense Tracker Application

## Overview
The **Expense Tracker Application** is a simple, user-friendly web application that allows users to record and manage their daily expenses. The app is built using Python and Flask for the backend, HTML/CSS for the frontend, and provides a clean, interactive interface to track expenses efficiently.

---

## Features
- Add expenses with details like **name**, **amount**, and **category**.
- View a list of all recorded expenses.
- Fully responsive design, works on both desktop and mobile.
- Stylish and modern UI with smooth animations.
- Data stored temporarily (can be extended with a database).

---

## Technologies Used
1. **Backend**: Python (Flask framework)
2. **Frontend**: HTML, CSS (with custom styling for a sleek design)
3. **Optional**: SQLite or any other database for persistent storage (not included in this version)

---

## Prerequisites
- Python 3.6+
- pip (Python package installer)
- Flask (Install using `pip install flask`)

---

## Installation Guide

### Step 1: Clone the Repository
```bash
$ git clone https://github.com/your-repo/expense-tracker.git
$ cd expense-tracker
```

### Step 2: Install Dependencies
Ensure Flask is installed:
```bash
$ pip install flask
```

### Step 3: Run the Application
Start the Flask server:
```bash
$ python app.py
```

### Step 4: Access the Application
Open your web browser and navigate to:
```
http://127.0.0.1:5000/
```

---

## Project Structure
```
expense-tracker/
|├── app.py             # Main Flask application file
|├── templates/
|   └── index.html     # HTML template for the UI
|├── static/
|   └── styles.css    # CSS file for styling
|└── README.md         # Documentation (this file)
```

---

## How to Use
1. Open the application in your browser.
2. Enter the expense details (e.g., Name, Amount, Category) in the form.
3. Click on the **Add Expense** button to record the expense.
4. View the list of all expenses below the form.

---

## Example Walkthrough
### Adding an Expense
1. Enter details:
   - **Name**: "Coffee"
   - **Amount**: "100"
   - **Category**: "Food"
2. Click **Add Expense**.

### Viewing Expenses
- Newly added expenses appear immediately in the list with details.

---

## Customization
### Styling
To modify the app's appearance, edit `static/styles.css`. Example changes:
- Update colors in the `body` or `button` styles.
- Add additional animations.

### Persistent Storage
To store data permanently:
1. Add a database like SQLite or MySQL.
2. Modify `app.py` to save expenses into the database instead of a Python list.

---

## Future Enhancements
- Add user authentication for personalized expense tracking.
- Integrate with a database for persistent storage.
- Visualize expenses with charts and graphs.
- Allow users to filter expenses by date or category.

---

## Contact
For questions or suggestions, feel free to contact:
- **Name**: Ankit Kumar
- **Email**: ankitrajput9999999@gmail.com

