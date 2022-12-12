from tkinter import *


def calculate():
    miles = float(miles_input.get())
    result = round(miles * 1.60934, 2)
    output_label.config(text=result)


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 10, "bold"))
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", font=("Arial", 10, "bold"))
equal_label.grid(column=0, row=1)

output_label = Label(text="0", font=("Arial", 10, "bold"))
output_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 10, "bold"))
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=3)

mainloop()
