import tkinter as tk

def container_calculator(case_type, quantity, location):
    # Your implementation to calculate the required number of containers
    # for a given case type, quantity, and location
    containers = 0
    return containers

def calculate_containers():
    case_type = case_type_var.get()
    try:
        quantity = int(quantity_entry.get())
    except ValueError:
        result_label.config(text="Quantity must be an intege...Meow!.")
        return

    location = location_var.get()

    containers = container_calculator(case_type, quantity, location)
    result_label.config(text=containers)

root = tk.Tk()
root.title("Container Calculator")

case_types = {
    "R3ACT": 1,
    "R3CRT": 2,
    "R3CTT": 2,
    "R3HRT": 2,
    "R4JZT": 2,
    "R7F1T": 2,
    "R7F2T": 2,
    "R7F3T": 2,
    "R7F4T": 2,
    "R7F5T": 2,
    "R7F6T": 2,
    "R8F1T": 2,
    "R8F3T": 2,
    "R8F4T": 2,
    "R8F5T": 2,
    "R8F6T": 2,
    "R8HAT": 2,
    # ... add the rest of your case types here
}

locations = [
    "Location 1",
    "Location 2",
    # ... add the rest of your locations here
]

case_type_var = tk.StringVar()
location_var = tk.StringVar()

case_type_label = tk.Label(root, text="Case Type:")
case_type_label.grid(row=0, column=0, padx=10, pady=10)

case_type_entry = tk.OptionMenu(root, case_type_var, *case_types.keys())
case_type_entry.grid(row=0, column=1, padx=10, pady=10)

quantity_label = tk.Label(root, text="Quantity:")
quantity_label.grid(row=1, column=0, padx=10, pady=10)

quantity_entry = tk.Entry(root)
quantity_entry.grid(row=1, column=1, padx=10, pady=10)

location_label = tk.Label(root, text="Location:")
location_label.grid(row=2, column=0, padx=10, pady=10)

location_entry = tk.OptionMenu(root, location_var, *locations)
location_entry.grid(row=2, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate", command=calculate_containers)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()