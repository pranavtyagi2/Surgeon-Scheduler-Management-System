# 🏥 AI-Based Surgeon Scheduler Management System

## 📌 Overview

Managing surgery schedules in hospitals is a complex and time-sensitive task. Manual scheduling often leads to delays, conflicts, and inefficient use of operation theatres.

This project presents an intelligent solution that automates the scheduling process using Machine Learning and optimized algorithms. It ensures that surgeries are planned efficiently, priorities are respected, and emergency cases are handled dynamically.

---

## 🚀 Key Features

* 🔹 **Automated Scheduling**
  Eliminates manual errors by generating schedules programmatically.

* 🔹 **Priority-Based Allocation**
  Critical surgeries are handled first using a Priority Queue.

* 🔹 **Machine Learning Integration**
  Predicts surgery duration based on type, patient condition, and surgeon experience.

* 🔹 **Conflict-Free Scheduling**
  Ensures no overlapping of surgeries.

* 🔹 **Emergency Override System 🚨**
  Dynamically adjusts the schedule when emergency cases arrive.

* 🔹 **REST API Support**
  Backend APIs allow integration with any frontend or external system.

---

## 🧠 Tech Stack

* Python
* Flask (Backend API)
* Scikit-learn (Machine Learning)
* Pandas & NumPy

---

## 📂 Project Structure

```
Surgeon-Scheduler-System/
│
├── api.py                # Flask API
├── scheduler.py          # Core scheduling logic
├── surgery_model.pkl     # Trained ML model
├── surgery_data.csv      # Dataset
├── train_model.ipynb     # Model training notebook
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ How to Run

1. Clone the repository
2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```
3. Run the backend server:

   ```
   python api.py
   ```
4. Open in browser:

   ```
   http://127.0.0.1:5000
   ```

---

## 🔌 API Endpoints

### ➤ Schedule Surgeries

**POST** `/schedule`

#### Sample Input:

```json
{
  "surgeries": [
    {"id":1,"type":"Cardio","experience":10,"condition":"critical","priority":1},
    {"id":2,"type":"Ortho","experience":5,"condition":"normal","priority":3}
  ]
}
```

#### Output:

Returns optimized, conflict-free schedule with start and end times.

---

### ➤ Emergency Handling

**POST** `/emergency`

Allows insertion of emergency surgeries and dynamically updates the schedule.

---

## 🎯 Problem Solved

* Reduces scheduling errors
* Minimizes delays in surgeries
* Improves resource utilization
* Handles real-time emergency scenarios

---

## 💡 Future Improvements

* Web-based dashboard for hospital staff
* Multi-operation theatre support
* Real-time database integration
* AI-based surgeon recommendation

---

## 👨‍💻 Author

Developed as part of a hackathon project focused on solving real-world healthcare scheduling challenges.

---

## ⭐ Final Note

This project demonstrates how combining Machine Learning with algorithmic optimization can significantly improve efficiency in critical domains like healthcare.

---
