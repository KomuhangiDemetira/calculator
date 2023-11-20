from tkinter import *

# Function to get the inputs from Entry and execute operations
def calculate():
    operation = operation_var.get()
    number1 = float(number1_entry.get())
    number2 = float(number2_entry.get())

    if operation == "Addition":
        result = number1 + number2
    elif operation == "Subtraction":
        result = number1 - number2
    elif operation == "Multiplication":
        result = number1 * number2
    elif operation == "Division":
        if number2 == 0:
            result = "Error! Division by zero is not allowed."
        else:
            result = number1 / number2

    result_text.set(str(result))

# Create a window
window = Tk()
window.title("Simple Calculator")

# Create widgets
operation_var = StringVar()
number1_entry = Entry(window, width=10)
number2_entry = Entry(window, width=10)
result_text = StringVar()

operation_label = Label(window, text="Operation:")
operation_dropdown = OptionMenu(window, operation_var, "Addition", "Subtraction", "Multiplication", "Division")
number1_label = Label(window, text="Number 1:")
number2_label = Label(window, text="Number 2:")
calculate_button = Button(window, text="Calculate", command=calculate)
result_label = Label(window, text="Result:")
result_display = Label(window, textvariable=result_text)

# Display widgets
operation_label.grid(row=0, column=0)
operation_dropdown.grid(row=0, column=1)
number1_label.grid(row=1, column=0)
number1_entry.grid(row=1, column=1)
number2_label.grid(row=2, column=0)
number2_entry.grid(row=2, column=1)
calculate_button.grid(row=3, column=1)
result_label.grid(row=4, column=0)
result_display.grid(row=4, column=1)

# Run the app
window.mainloop()
