import tkinter as tk
from tkinter import messagebox
import random
import time

class OBDMockApp:
    def __init__(self, master):
        self.master = master
        master.title("RI-Auto Diagnostic Reader")
        
        self.speed_label = tk.Label(master, text="Vehicle Speed: -- km/h", font=("Helvetica", 16))
        self.speed_label.pack(pady=20)

        self.rpm_label = tk.Label(master, text="Engine RPM: --", font=("Poppins", 16))
        self.rpm_label.pack(pady=20)

        self.update_button = tk.Button(master, text="Get OBD Data", command=self.get_obd_data, font=("Helvetica", 14))
        self.update_button.pack(pady=10)

    def get_obd_data(self):
        # Mock data generation
        speed = random.randint(0, 200)  # Simulated speed in km/h
        rpm = random.randint(0, 8000)    # Simulated RPM

        # Update labels with mock data
        self.speed_label.config(text=f"Vehicle Speed: {speed} km/h")
        self.rpm_label.config(text=f"Engine RPM: {rpm}")

if __name__ == "__main__":
    root = tk.Tk()
    app = OBDMockApp(root)
    root.geometry("400x300")
    root.mainloop()