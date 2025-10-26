from tkinter import *

def onclick():
    label.configure(text=str(eval(entry.get())))

#Creating main Interface
window = Tk()
photo = PhotoImage(file="certificate.png")
window.iconphoto(True,photo)
window.title("Calculator")
window.geometry("500x500")
window.config(background="black")

#Create Tittle Text "Calculator to-ay ni Comedia"
label = Label(window, 
              text="Calculator to-ay ni Comedia",
              font=("Arial", 10, "bold"),
              padx=50,
              pady=10,
              fg="black",
              bd=10,
              relief=RAISED)
label.pack()
label.place(y=20, x=115)
#Create Entry where user can type the number to calculate
entry = Entry(window,
              bd=5,
              relief=RAISED,
              font=("Arila",20),
              fg="black")
entry.pack(anchor="w")
entry.place(y=300, x=85)

#Create label where the results display
label = Label(window,
              font=("Arial", 30),
              fg="black",
              padx= 100,
              bd=10,
              relief= RAISED,
              pady= 20
              )
label.pack()
label.place(y=80, x=135)

#Create Button to click by the user in order to display the result
button = Button(window,
                text="=",
                font=("Arial", 20),
                bd=5,
                fg="black",
                command=onclick)

button.pack()
button.place(x=225,y=200)

window.mainloop()

