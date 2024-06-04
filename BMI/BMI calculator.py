import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pandas as pd
import matplotlib.pyplot as plt

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = weight / (height / 100) ** 2
        
        if bmi < 18.5:
            bmi_category = "Underweight"
        elif 18.5 <= bmi < 25:
            bmi_category = "Healthy weight"
        elif 25 <= bmi < 30:
            bmi_category = "Overweight"
        else:
            bmi_category = "Obese"

        bmi_label.config(text=f"Your calculated BMI is: {bmi:.2f}")
        bmi_category_label.config(text=f"Category: {bmi_category}")

        with open("bmi_results.txt", "a") as file:
            file.write(f"Weight: {weight} kg\n")
            file.write(f"Height: {height} cm\n")
            file.write(f"BMI: {bmi:.2f}\n")
            file.write(f"Category: {bmi_category}\n\n")

        try:
            df_existing = pd.read_excel('bmi_results.xlsx')
        except FileNotFoundError:
            df_existing = pd.DataFrame()

        df_new = pd.DataFrame({'weight': [weight], 'height': [height], 'bmi': [bmi], 'category': [bmi_category]})
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        df_combined.to_excel('bmi_results.xlsx', index=False)

    except ValueError:
        messagebox.showerror("Incorrect Value")
    except Exception as e:
        messagebox.showerror("Unexpected Error", f"An unexpected error occurred: {str(e)}")

def generate_line_chart():
    try:
        df = pd.read_excel('bmi_results.xlsx')
        plt.figure(figsize=(5, 5))

        plt.plot(df.index, df['weight'], marker='o', label='Weight (kg)')
        plt.plot(df.index, df['height'], marker='o', label='Height (cm)')

        plt.title('BMI Results Over Time')
        plt.ylabel('weight/height')
        plt.legend()
        plt.grid(True)
        plt.show()

    except FileNotFoundError:
        messagebox.showerror("The Excel file bmi_results.xlsx does not exist.")
    except Exception as e:
        messagebox.showerror("Unexpected Error", f"An unexpected error occurred: {str(e)}")

root = tk.Tk()
root.geometry("475x475+50+50")
root.title("BMI Calculator")

image = Image.open("C:\\Users\\Aden\\OneDrive\\Desktop\\Personal coding\\Internship - info\\BMI\\adult-body-mass-index-guide-alt-1440x810.jpg")
bg_image = ImageTk.PhotoImage(image)
limg = tk.Label(root, image=bg_image)
limg.place(x=0, y=0, relwidth=1, relheight=1)

weight_label = tk.Label(root, text="Weight in kg:", font=("Arial", 20))
weight_label.pack()
weight_entry = tk.Entry(root, font=("Arial", 20))
weight_entry.pack()
height_label = tk.Label(root, text="Height in cm:", font=("Arial", 20))
height_label.pack()
height_entry = tk.Entry(root, font=("Arial", 20))
height_entry.pack()
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi, font=("Arial", 10))
calculate_button.pack()
empty_label = tk.Label(root, text="", font=("Arial", 15))
empty_label.pack()
chart_button = tk.Button(root, text="Generate Line Chart",
command=generate_line_chart, font=("Arial", 10))
chart_button.pack()
empty_label = tk.Label(root, text="", font=("Arial", 15))
empty_label.pack()
bmi_label = tk.Label(root, text="", font=("Arial", 15))
bmi_label.pack()
bmi_category_label = tk.Label(root, text="", font=("Arial", 15))
bmi_category_label.pack()

root.mainloop()
