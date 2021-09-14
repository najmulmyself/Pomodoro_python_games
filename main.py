
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import * 

window = Tk()
window.title("Promodoro")
window.config(padx=100 , pady=50 , bg=YELLOW )
# when we change the background color of the window it shows a problem of images background
#need to change image background 

canvas = Canvas(width=200, height=224 , bg=YELLOW , highlightthickness= 0)
#When we change the image background another problem aries that image has a border and its white .
#but there is not such good thing to remove the border exepct highlightthickness = 0
#We set height and width according to the image we have selected | it has 200 * 224
#We nedd to set an Image to the background | for this it as built in mehod PhotoImage we need to use

tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image=tomato_img)
# cordination selected bcz we exactly want img to be centered
canvas.create_text(110 , 130, text="00:00" , fill="white" , font=(FONT_NAME , 35 , "bold"))
canvas.pack()



window.mainloop()