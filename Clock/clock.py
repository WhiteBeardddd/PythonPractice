from tkinter import *
from time import *

    

def update():
    time_string = strftime("%I:%M:%S %p")  
    time_label.config(text=time_string)
    
    
    day_string = strftime("%A")  
    day_label.config(text=day_string)
    
    date_string = strftime("%B %m %y")
    date_label.config(text=date_string)
    
    
    time_label.after(1000, update)  
    
def add():
    global counter
    counter += 1
    update_count()
    
def subtract():
    global counter
    if counter > 0:
        counter -= 1
    update_count()
    
def update_count():
    counter_num.config(text=str(counter))
    

window = Tk()
window.title("THE TIME OF CHARLES")
window.config(bg="black")

counter = 0

time_label = Label(window, font=("Arial", 100), fg="#00FF00", bg="Black")
time_label.pack()

day_label = Label(window, font=("Ink Free", 100), fg="#00FF00", bg="Black")
day_label.pack()

date_label = Label(window, font=("Times New Roman", 100), fg="#00FF00", bg="Black")
date_label.pack()

add_button = Button(window, text="ADD", command=add)
add_button.pack()

minus_button = Button(window, text="SUBTRACT", command=subtract)
minus_button.pack()

counter_num = Label(window, text=str(counter), font=("Arial",150))
counter_num.pack(pady=20,padx=20)

update()  

window.mainloop()

