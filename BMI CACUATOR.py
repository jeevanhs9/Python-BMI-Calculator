import tkinter as tk
import matplotlib.pyplot as plt

# ---------------- BMI CALCULATION ----------------
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height_cm = float(height_entry.get())
        gender = gender_var.get()

        # validation
        if weight <= 0 or height_cm <= 0:
            raise ValueError

        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)

        bmi_value.config(text=f"{bmi:.1f}")

        if bmi < 18.5:
            category = "Underweight"
            color = "#4fc3f7"
        elif bmi < 25:
            category = "Normal"
            color = "#66bb6a"
        elif bmi < 30:
            category = "Overweight"
            color = "#ffa726"
        else:
            category = "Obese"
            color = "#ef5350"

        bmi_status.config(text=f"{category} ({gender})", fg=color)

        # SAVE HISTORY
        with open("bmi_history.txt", "a") as file:
            file.write(f"{gender},{weight},{height_cm},{bmi:.1f},{category}\n")

    except:
        bmi_value.config(text="Error")
        bmi_status.config(text="Invalid Input", fg="red")

# ---------------- SHOW HISTORY ----------------
def show_history():
    try:
        with open("bmi_history.txt", "r") as file:
            data = file.read()
    except:
        data = "No history found"

    history_window = tk.Toplevel(root)
    history_window.title("BMI History")
    history_window.geometry("320x350")

    tk.Label(history_window, text="BMI History", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Message(history_window, text=data, width=300).pack()

# ---------------- SHOW GRAPH ----------------
def show_graph():
    try:
        bmis = []
        with open("bmi_history.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                bmis.append(float(data[3]))

        if len(bmis) == 0:
            raise ValueError

        plt.plot(bmis, marker="o")
        plt.title("BMI Trend Graph")
        plt.xlabel("Records")
        plt.ylabel("BMI")
        plt.grid(True)
        plt.show()

    except:
        print("No data available for graph")

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Advanced BMI Calculator - IBM Project")
root.geometry("360x520")
root.configure(bg="#1e1e2f")
root.resizable(False, False)

# Title
tk.Label(
    root,
    text="BMI Calculator",
    font=("Arial", 20, "bold"),
    fg="#7CFC00",
    bg="#1e1e2f"
).pack(pady=15)

# BMI Display
bmi_value = tk.Label(
    root,
    text="0.0",
    font=("Arial", 36, "bold"),
    fg="white",
    bg="#1e1e2f"
)
bmi_value.pack()

bmi_status = tk.Label(
    root,
    text="Status",
    font=("Arial", 14),
    fg="white",
    bg="#1e1e2f"
)
bmi_status.pack(pady=5)

# Gender
gender_var = tk.StringVar(value="Male")
gender_frame = tk.Frame(root, bg="#1e1e2f")
gender_frame.pack(pady=10)

tk.Label(gender_frame, text="Gender:", fg="white", bg="#1e1e2f").pack(side="left", padx=5)

tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male",
               bg="#1e1e2f", fg="white", selectcolor="#2a2a40").pack(side="left", padx=5)

tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female",
               bg="#1e1e2f", fg="white", selectcolor="#2a2a40").pack(side="left", padx=15)

# Input frame
frame = tk.Frame(root, bg="#2a2a40")
frame.pack(pady=15, padx=20, fill="x")

tk.Label(frame, text="Height (cm)", fg="white", bg="#2a2a40").pack(pady=5)
height_entry = tk.Entry(frame, font=("Arial", 12), justify="center")
height_entry.pack()

tk.Label(frame, text="Weight (kg)", fg="white", bg="#2a2a40").pack(pady=5)
weight_entry = tk.Entry(frame, font=("Arial", 12), justify="center")
weight_entry.pack()

# Calculate button
tk.Button(
    root,
    text="Calculate Your BMI",
    font=("Arial", 14, "bold"),
    bg="#ff2d55",
    fg="white",
    command=calculate_bmi
).pack(pady=15, ipadx=10, ipady=5)

# History button
tk.Button(
    root,
    text="View History",
    font=("Arial", 12, "bold"),
    bg="#00adb5",
    fg="white",
    command=show_history
).pack(pady=5)

# Graph button
tk.Button(
    root,
    text="Show BMI Graph",
    font=("Arial", 12, "bold"),
    bg="#ffaa00",
    fg="white",
    command=show_graph
).pack(pady=5)

root.mainloop()
