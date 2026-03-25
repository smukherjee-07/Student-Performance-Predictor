#  Project Report: Student Performance Predictor (SPP)

# 1. Introduction & Problem Statement

In most academic systems, students usually receive feedback only after exams are completed. By that point, it is often too late to improve. This project aims to address that issue.

The **Student Performance Predictor (SPP)** is designed as a proactive tool that gives an early estimate of how a student might perform in their final exams. It uses factors such as study hours, sleep patterns, attendance, and midterm marks to predict end-term performance and calculate an overall grade.

The goal of this system is to help students and educators identify potential academic risks early, allowing corrective actions before the semester ends.


# 2. Methodology & Approach

This project follows a **hybrid approach**, combining Machine Learning with rule-based academic logic.

## 2.1 Machine Learning Component

The prediction system uses a **supervised learning model**, specifically **Linear Regression**.

This model was chosen because:
- It is simple and easy to understand  
- It clearly shows how each input affects the output  
- It works well for linear relationships in academic data  

For example, the model helps estimate how changes in study hours or midterm performance impact the final outcome.

## 2.2 Rule-Based Evaluation

Machine Learning alone cannot fully capture academic policies, so a rule-based layer is added.

This layer handles:

- **Attendance Constraint:**  
  If attendance is below 75%, the student is marked as **debarred**, regardless of predicted performance.

- **Weighted Scoring:**  
  The final score combines predicted marks, midterm marks, and internal assessments.

This makes the system closer to real-world academic evaluation.


# 3. System Design & Implementation

## 3.1 Mathematical Framework

The final score is calculated out of 100:

Final Score = (0.3 × Predicted Endterm) + (0.6 × Midterm) + Internals + Attendance

Where:
- Predicted Endterm: Output of the ML model (0–100)  
- Midterm Marks: User input (0–50)  
- Internals: Viva, Assignment, Behaviour, Quiz (max 35)  
- Attendance Bonus: 1–5 marks based on attendance  

This formula ensures a balanced and realistic evaluation.

## 3.2 Data Processing

The system uses the **pandas** library for handling data.

It automatically:
- Removes extra spaces from column names  
- Converts column names to lowercase  
- Renames columns (e.g., `hours_studied` → `study_hours`)  

This ensures compatibility and reduces errors during execution.


# 4. Results & Analysis

The model performance is evaluated using:

- **R² Score:**  
  Around **0.90 – 0.95**, indicating strong predictive capability  

- **Mean Absolute Error (MAE):**  
  Less than **5 marks**, showing reliable predictions  

## 4.1 Feature Importance

From the model analysis:

- **Study Hours** and **Midterm Marks** have the highest impact  
- Attendance also contributes significantly  

This aligns with real-world expectations of academic performance.


# 5. Challenges & Key Learnings

- **Data Leakage:**  
  Including internal marks in training made predictions unrealistic.  
  This was fixed by excluding them from the ML model.

- **System Design:**  
  Creating a menu-based CLI helped organize the workflow and avoid repeated training.

- **Relative Grading:**  
  Implementing grading based on class average improved fairness but required handling dynamic values.


# 6. Conclusion

The Student Performance Predictor shows that Machine Learning is most effective when combined with real-world logic.

By integrating prediction with academic rules, the system becomes:
- Practical  
- Easy to interpret  
- Useful for early performance analysis  

This project demonstrates how data-driven tools can support better academic decision-making.


# Appendix: Technical Specifications

- **Language:** Python 3.8+  
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib  
- **Dataset:** student_performance_dataset_275.csv  
- **Visualizations:** accuracy.png, importance.png  
