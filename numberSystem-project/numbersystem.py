from tkinter  import *

def convert_number(number):
    try:
        decimal = int(number)
        binary = bin(decimal)[2:]
        octal = oct(decimal)[2:]
        hexadecimal = hex(decimal)[2:].upper()
        label.config(text=f"Binary: {binary}\nOctal: {octal}\nHexadecimal: {hexadecimal}")
    except ValueError:
        label.config(text="Invalid input")

window = Tk()
window.title("Number System Converter")
window.geometry("700x500")
window.configure(background="White")



label = Label(window, text="Number System Converter", fg="Green", font=("Arial", 20, "bold"))
label.pack(pady=20)

entry = Entry(window, bd=5, font=("Arial", 12,"bold"), fg="green", width=20, )
entry.pack(padx=20, anchor="w")
entry.place(y=100, x=250)

button = Button(window, text="Convert", bg="white", fg="black", font=("Arial", 12, "bold"), command=lambda: convert_number(entry.get()))
button.pack()
button.place(y=150, x=300)

label = Label(window, text="Result", fg="black", font=("Arial", 12, "bold"), relief="solid")
label.pack(pady=20)
label.place(y=200, x=250)


mainloop()