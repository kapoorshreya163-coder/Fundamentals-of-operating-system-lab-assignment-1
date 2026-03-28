# CPU Scheduling Algorithms (FCFS & SJF)

## 📌 Project Overview

This project is part of the Operating System Lab. It focuses on the implementation and analysis of two CPU scheduling algorithms:

* First Come First Serve (FCFS)
* Shortest Job First (SJF - Non Preemptive)

The project demonstrates how processes are scheduled in an operating system and evaluates performance using standard metrics.

---

## 🎯 Objectives

* Understand CPU scheduling concepts
* Implement FCFS and SJF algorithms using Python
* Calculate:

  * Completion Time (CT)
  * Turnaround Time (TAT)
  * Waiting Time (WT)
* Compare performance of scheduling algorithms

---

## 🛠️ Technologies Used

* Python 3.x
* Standard Python Libraries
* Git & GitHub

---

## 📂 Project Structure

```
├── fcfs_sjf.py        # Main Python code
├── output_screenshots # Output images
├── report.pdf         # Assignment report
└── README.md          # Project documentation
```

---

## ⚙️ How to Run the Code

1. Clone the repository:

```
git clone https://github.com/your-username/cpu-scheduling.git
```

2. Navigate to the project folder:

```
cd cpu-scheduling
```

3. Run the program:

```
python fcfs_sjf.py
```

4. Enter process details:

* Process ID
* Arrival Time
* Burst Time

---

## 📊 Algorithms Implemented

### 1. FCFS (First Come First Serve)

* Processes are executed in order of arrival
* Simple and easy to implement
* May cause long waiting time (Convoy Effect)

### 2. SJF (Shortest Job First)

* Process with shortest burst time executes first
* Gives better average waiting time
* Requires knowledge of burst time

---

## 📈 Performance Metrics

* Completion Time (CT)
* Turnaround Time (TAT = CT - AT)
* Waiting Time (WT = TAT - BT)

---

## 📉 Results & Comparison

| Algorithm | Performance         |
| --------- | ------------------- |
| FCFS      | Higher waiting time |
| SJF       | Lower waiting time  |

✅ **Conclusion:**
SJF performs better than FCFS in terms of average waiting time and turnaround time.

---

## 📌 Features

* User input for processes
* Tabular output display
* Calculation of CT, TAT, WT
* Gantt chart representation (manual/visual)

---

## 📷 Output

(Add screenshots of your output here)

---

## 👨‍💻 Author

* Name: Shreya Kapoor
* Course: BCA (AI & DS)
* Subject: Operating System Lab

---

## 📎 Submission Details

* Individual Assignment
* Includes:

  * Source Code
  * Output Screenshots
  * Report
  * GitHub Link

---

## 📚 References

* Operating System Concepts
* Python Documentation

---
