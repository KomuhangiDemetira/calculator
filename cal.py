from tkinter import *

# Function to get the inputs from Entry and execute operations
def calculate():
    operation = operation_var.get()
    try:
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
    except ValueError:
        result_text.set("Error! Please enter valid numbers.")

# Create a window
window = Tk()
window.title("Simple Calculator")

# Set styles
bg_color = "#f0f0f0"
font_style = ("Helvetica", 12)

window.configure(bg=bg_color)

# Create a frame to contain all widgets
content_frame = Frame(window, bg=bg_color, bd=2, relief="solid")

# Create widgets
operation_var = StringVar()
number1_entry = Entry(content_frame, width=10, font=font_style, bd=2, relief="solid")
number2_entry = Entry(content_frame, width=10, font=font_style, bd=2, relief="solid")
result_text = StringVar()

operation_label = Label(content_frame, text="Operation:", bg=bg_color, font=font_style)
operation_dropdown = OptionMenu(content_frame, operation_var, "Addition", "Subtraction", "Multiplication", "Division")
number1_label = Label(content_frame, text="Number 1:", bg=bg_color, font=font_style)
number2_label = Label(content_frame, text="Number 2:", bg=bg_color, font=font_style)
calculate_button = Button(content_frame, text="Calculate", command=calculate, bg="black", fg="white", font=font_style)
result_label = Label(content_frame, text="Result:", bg=bg_color, font=font_style)
result_display = Label(content_frame, textvariable=result_text, bg=bg_color, font=font_style)

# Display widgets
operation_label.grid(row=0, column=0, pady=5)
operation_dropdown.grid(row=0, column=1, pady=5)
number1_label.grid(row=1, column=0, pady=5)
number1_entry.grid(row=1, column=1, pady=5)
number2_label.grid(row=2, column=0, pady=5)
number2_entry.grid(row=2, column=1, pady=5)
calculate_button.grid(row=3, column=1, pady=5)
result_label.grid(row=4, column=0, pady=5)
result_display.grid(row=4, column=1, pady=5)

# Pack the content_frame to center align it within the window
content_frame.pack(expand=True, fill='both', padx=20, pady=20)

# Run the app
window.mainloop()
