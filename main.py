from tkinter import * 
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
global reps

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    # reps += 1


    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    
    if reps % 8 == 0:
        countdown(short_break_sec)
    elif reps % 2 == 0:
        countdown(long_break_sec)
    else:
        countdown(work_sec)

    # countdown(5 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}" # This is Dynamic Variable Concept in Python 
        # changing a variable type from int to str

    canvas.itemconfig(timer_text , text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000 , countdown , count - 1)
        # This is the method to work with gui | after is something like await;

        #Now we want to show this time in our canvas | to do this we need to assign variable what we want to show
        # in this case we want this in canvas text( text in tomato) | lets create a variable named timer_text
        # creating a variable is not ultimate solution because we cant show this in screen with our old method (variable.config) 
        #we need to use canvas.itemconfig() | first argument is where we want to configure and second is what we want to  change


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Promodoro")
window.config(padx=100 , pady=50 , bg=YELLOW )
# when we change the background color of the window it shows a problem of images background
#need to change image background 


canvas_title = Label(text="Timer" , font=(FONT_NAME , 50) , bg=YELLOW , fg=GREEN)
canvas_title.grid(column=1 , row=0)



canvas = Canvas(width=200, height=224 , bg=YELLOW , highlightthickness= 0)
#When we change the image background another problem aries that image has a border and its white .
#but there is not such good thing to remove the border exepct highlightthickness = 0
#We set height and width according to the image we have selected | it has 200 * 224
#We nedd to set an Image to the background | for this it as built in mehod PhotoImage we need to use

tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image=tomato_img)
# cordination selected bcz we exactly want img to be centered
timer_text = canvas.create_text(110 , 130, text="00:00" , fill="white" , font=(FONT_NAME , 35 , "bold"))
canvas.grid(column=1 , row=1)


start_btn = Button(text="Start" , highlightthickness=0 , padx=10 , command=start_timer)
start_btn.grid(column=0 , row=3)
reset_btn = Button(text="Reset" , highlightthickness=0 , padx=10)
reset_btn.grid(column=2 , row=3)

check_marks = Label(text="✔" , fg=GREEN , bg = YELLOW)
check_marks.grid(column=1 , row=4)

window.mainloop()