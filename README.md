# 🎓 Student Performance Predictor (SPP)

## 📌 Overview

The **Student Performance Predictor (SPP)** is a console-based Python application designed to estimate and evaluate a student’s academic performance using a combination of **Machine Learning** and rule-based logic.

Unlike basic prediction systems, this project not only forecasts end-term marks but also simulates a realistic academic evaluation framework. It incorporates attendance policies, internal assessments, and relative grading to produce a complete performance report.

## 🏗 System Design

The application follows a modular and logically separated architecture to ensure clarity and maintainability.

### Execution Flow

User Input → Validation → ML Prediction → Score Calculation → Grading → Risk/Status Evaluation → Output Report

### Design Approach

* **Separation of Concerns:** Machine Learning is used strictly for prediction, while evaluation is handled independently using academic rules.
* **Modularity:** Each component (input handling, prediction, calculation, grading) is implemented as a separate function.
* **Interpretability:** The system uses **Linear Regression** to maintain transparency in how features affect outcomes.

## 📊 Dataset & Model

### 🗂 Dataset

The dataset used in this project is synthetically generated to reflect realistic academic behavior.
* **Total Records:** 275
* **Features:** Study hours, Sleep hours, Attendance, and Midterm marks.
* **Internal Components:** Viva, Assignment, Behaviour, and Quiz/Tutorial.

### 🧠 Machine Learning Model

The system uses **Linear Regression** for predicting end-term marks.
* **Why Linear Regression?** It is simple, interpretable, and suitable for linear academic trends.
* **Model Performance:** * **R² Score:** ~0.90 – 0.95 (High predictive power)
    * **MAE:** ≤ 5 marks (Low average error)

## 🧩 Core Functional Components

### 🤖 Prediction Engine

The trained model processes user inputs to estimate **End-term marks (0–100)**. Internal marks (viva, assignments, etc.) are intentionally excluded from training to prevent data leakage and ensure the model remains valid and fair.

### 🧮 Evaluation System

After prediction, the system calculates the final academic score out of **100 marks** using the following weighted formula:

$$Final\ Score = (0.3 \times \text{Pred. Endterm}) + (0.6 \times \text{Midterm}) + \text{Internals} + \text{Attendance Bonus}$$

### 📅 Attendance Rule & Marks

Attendance plays a critical role in both eligibility and scoring:
* **Eligibility:** If attendance < 75% → Student is **Debarred** (Fail).
* **Bonus Marks:** * 96–100%: 5 Marks
    * 91–95%: 4 Marks
    * 86–90%: 3 Marks
    * 81–85%: 2 Marks
    * 75–80%: 1 Mark

### 🏆 Grading System (Relative)

Grades are assigned relative to the class performance average:
| Condition | Grade |
| :--- | :--- |
| ≥ Average + 15 | S |
| ≥ Average + 10 | A |
| ≥ Average | B |
| ≥ Average - 10 | C |
| ≥ Average - 20 | D |
| < 40 | F |

## 📈 Analytical Features

The system includes built-in visualization tools to understand model behavior. The following graphs are automatically generated and saved:
1. **accuracy.png:** A scatter plot showing Actual vs. Predicted marks to visualize model accuracy.
2. **importance.png:** A bar chart displaying the impact of each feature (like study hours) on the prediction.

## 🚀 How to Run

### 🧾 Requirements

* Python 3.8 or higher
* Required libraries: `pandas`, `numpy`, `matplotlib`, `scikit-learn`

### 🖥 Execution Steps

1. **Prepare Files:** Ensure `student_performance_predictor.py` and `student_performance_dataset_275.csv` are in the same folder.
2. **Install Dependencies:** Run `pip install pandas numpy matplotlib scikit-learn` in your terminal.
3. **Launch Program:** Run the command `python student_performance_predictor.py`.
4. **Initial Setup:** Choose **Option 1** from the menu to train the model before attempting any predictions.

### 📌 Usage Guide

* **Option 1 (Train Model):** Initializes the ML system using the local CSV file.
* **Option 2 (Predict):** Follow the prompts to enter student data. The system will calculate the predicted exam score and the final grade.
* **Option 3 (Generate Graphs):** Saves visual performance reports to the project directory as PNG files.
* **Option 4 (Exit):** Safely terminates the application.

## 📂 Project Structure

```text
project/
│
├── README.md
├── accuracy.png
├── importance.png
├── student_performance_dataset_275.csv
└── student_performance_predictor.py
