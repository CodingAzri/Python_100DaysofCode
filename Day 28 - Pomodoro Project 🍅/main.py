from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FF4B91"
RED = "#D80032"
GREEN = "#004225"
BEIGE = "#F8F0E5"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    # Reset 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # title.label "Timer"
    title_label.config(text="Timer")
    # Reset check_marks
    check_marks.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro 🍅")
window.config(padx=50, pady=50, bg=BEIGE)

title_label = Label(text="Timer", fg=GREEN, bg=BEIGE, font=(FONT_NAME, 50, "normal"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=290, height=280, bg=BEIGE, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(145, 140, image=tomato_img)
timer_text = canvas.create_text(145, 155, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=BEIGE)
check_marks.grid(column=1, row=3)

window.mainloop()
