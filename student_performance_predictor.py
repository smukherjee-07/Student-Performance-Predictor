import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

# CONFIGURATION
DATASET_PATH = "student_performance_dataset_275.csv"

# UTILITY FUNCTIONS
def section(title):
    line = "=" * 60
    print("\n" + line)
    print(title.center(60))
    print(line)

def get_input(prompt, lo, hi):
    while True:
        try:
            value = float(input(f"{prompt} ({lo}-{hi}): "))
            if lo <= value <= hi:
                return value
            else:
                print("Value out of range. Please try again.")
        except:
            print("Invalid input. Please enter a number.")

# LOAD DATASET
def load_dataset():
    if not os.path.exists(DATASET_PATH):
        print("Dataset file not found.")
        return None

    df = pd.read_csv(DATASET_PATH)

    # Fix column
    df.columns = df.columns.str.strip().str.lower()

    # Rename if needed
    if "hours_studied" in df.columns:
        df.rename(columns={"hours_studied": "study_hours"}, inplace=True)

    return df

# MODEL TRAINING
def train_model(df):
    FEATURES = ["study_hours", "sleep_hours", "attendance", "midterm_marks"]

    X = df[FEATURES]
    y = df["endterm_marks"]

    model = LinearRegression()
    model.fit(X, y)

    predictions = model.predict(X)

    r2 = r2_score(y, predictions)
    mae = mean_absolute_error(y, predictions)

    section("MACHINE LEARNING TRAINING RESULT")
    print(f"Model        : Linear Regression")
    print(f"R2 Score     : {r2:.2f}")
    print(f"MAE          : {mae:.2f}")

    return model, FEATURES

# CALCULATIONS
def attendance_marks(att):
    if att >= 96: return 5
    elif att >= 91: return 4
    elif att >= 86: return 3
    elif att >= 81: return 2
    elif att >= 75: return 1
    else: return 0

def calculate_final_score(endterm, midterm, att, viva, assignment, behaviour, quiz):
    return (
        0.3 * endterm +
        0.6 * midterm +
        attendance_marks(att) +
        viva + assignment + behaviour + quiz
    )

def assign_grade(score, avg):
    if score < 40: return "F"
    elif score >= avg + 15: return "S"
    elif score >= avg + 10: return "A"
    elif score >= avg: return "B"
    elif score >= avg - 10: return "C"
    elif score >= avg - 20: return "D"
    else: return "F"

# PREDICTION
def predict(model, df, FEATURES):
    section("ENTER STUDENT DATA")

    hours = get_input("Study Hours", 0, 24)
    sleep = get_input("Sleep Hours", 0, 24)
    attendance = get_input("Attendance (%)", 0, 100)
    midterm = get_input("Midterm Marks", 0, 50)

    viva = get_input("Viva", 0, 10)
    assignment = get_input("Assignment", 0, 10)
    behaviour = get_input("Behaviour", 0, 5)
    quiz = get_input("Quiz/Tutorial", 0, 10)

    section("INPUT SUMMARY")
    print(f"Study Hours     : {hours}")
    print(f"Sleep Hours     : {sleep}")
    print(f"Attendance      : {attendance}%")
    print(f"Midterm Marks   : {midterm}/50")
    print(f"Viva            : {viva}/10")
    print(f"Assignment      : {assignment}/10")
    print(f"Behaviour       : {behaviour}/5")
    print(f"Quiz/Tutorial   : {quiz}/10")

    if attendance < 75:
        section("STATUS")
        print("Student is debarred due to attendance below 75%.")
        return

    # Prediction
    input_df = pd.DataFrame([[hours, sleep, attendance, midterm]], columns=FEATURES)
    predicted_endterm = model.predict(input_df)[0]

    section("ML PREDICTION")
    print(f"Predicted End-term Marks : {predicted_endterm:.2f}/100")

    # Final evaluation
    final_score = calculate_final_score(
        predicted_endterm, midterm, attendance,
        viva, assignment, behaviour, quiz
    )

    class_avg = df["endterm_marks"].mean()
    grade = assign_grade(final_score, class_avg)

    section("FINAL EVALUATION")
    print(f"Final Score   : {final_score:.2f}/100")
    print(f"Class Average : {class_avg:.2f}")
    print(f"Grade         : {grade}")

# GRAPH GENERATION
def generate_graphs(model, df, FEATURES):
    X = df[FEATURES]
    y = df["endterm_marks"]
    predictions = model.predict(X)

    section("GENERATING GRAPHS")

    # Actual vs Predicted
    plt.figure()
    plt.scatter(y, predictions)
    plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
    plt.title("Actual vs Predicted")
    plt.xlabel("Actual Marks")
    plt.ylabel("Predicted Marks")
    plt.savefig("accuracy.png")
    plt.show()

    # Feature Importance
    importance = pd.Series(model.coef_, index=FEATURES)
    importance.plot(kind="barh")
    plt.title("Feature Importance")
    plt.savefig("importance.png")
    plt.show()

    print("Graphs saved as 'accuracy.png' and 'importance.png'")

# MENU SYSTEM
def main():
    df = load_dataset()
    if df is None:
        return

    model = None
    FEATURES = None

    while True:
        section("STUDENT PERFORMANCE PREDICTOR")

        print("1. Train Model")
        print("2. Predict Student Performance")
        print("3. Generate Graphs")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            model, FEATURES = train_model(df)

        elif choice == "2":
            if model is None:
                print("Please train the model first.")
            else:
                predict(model, df, FEATURES)

        elif choice == "3":
            if model is None:
                print("Please train the model first.")
            else:
                generate_graphs(model, df, FEATURES)

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

# ENTRY POINT
if __name__ == "__main__":
    main()