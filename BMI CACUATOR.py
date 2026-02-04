import tkinter as tk

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height_cm = float(height_entry.get())
        gender = gender_var.get()

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

    except:
        bmi_value.config(text="Error")
        bmi_status.config(text="Invalid Input", fg="red")


# Window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("360x460")
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

# Gender Selection
gender_var = tk.StringVar(value="Male")

gender_frame = tk.Frame(root, bg="#1e1e2f")
gender_frame.pack(pady=10)

tk.Label(
    gender_frame,
    text="Gender:",
    fg="white",
    bg="#1e1e2f"
).pack(side="left", padx=5)

tk.Radiobutton(
    gender_frame,
    text="Male",
    variable=gender_var,
    value="Male",
    bg="#1e1e2f",
    fg="white",
    selectcolor="#2a2a40"
).pack(side="left", padx=5)

tk.Radiobutton(
    gender_frame,
    text="Female",
    variable=gender_var,
    value="Female",
    bg="#1e1e2f",
    fg="white",
    selectcolor="#2a2a40"
).pack(side="left", padx=15)

# Input Frame
frame = tk.Frame(root, bg="#2a2a40")
frame.pack(pady=15, padx=20, fill="x")

# Height
tk.Label(frame, text="Height (cm)", fg="white", bg="#2a2a40").pack(pady=5)
height_entry = tk.Entry(frame, font=("Arial", 12), justify="center")
height_entry.pack()

# Weight
tk.Label(frame, text="Weight (kg)", fg="white", bg="#2a2a40").pack(pady=5)
weight_entry = tk.Entry(frame, font=("Arial", 12), justify="center")
weight_entry.pack()

# Button
tk.Button(
    root,
    text="Calculate Your BMI",
    font=("Arial", 14, "bold"),
    bg="#ff2d55",
    fg="white",
    command=calculate_bmi
).pack(pady=25, ipadx=10, ipady=5)

root.mainloop()
