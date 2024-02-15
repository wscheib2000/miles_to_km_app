import tkinter as tk

window = tk.Tk()
window.config(padx=20, pady=20)

is_equal = tk.Label(text="is equal to")
is_equal.grid(row=1, column=0)

miles_input = tk.Entry(width=10)
miles_input.insert(tk.END, string="0")
miles_input.grid(row=0, column=1)

miles = tk.Label(text="Miles")
miles.grid(row=0, column=2)

km_output = tk.Label(text="0")
km_output.grid(row=1, column=1)

km = tk.Label(text="Km")
km.grid(row=1, column=2)

def calculate():
    km_output.config(text=f'{round(float(miles_input.get())*1.609, 1)}')

calculate_button = tk.Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1)

window.mainloop()