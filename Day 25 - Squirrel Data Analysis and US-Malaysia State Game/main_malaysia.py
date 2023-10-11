import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.title("Malaysia States Game")
image = "malaysia_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("malaysia_states.csv")
all_states = data.state.to_list()
guessed_states = []

# To check coordinate on screen
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

while len(guessed_states) < 13:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/13 States Correct!", prompt="What's another state's "
                                                                                              "name?").title()
    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_states:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("malay_states_to_learn.csv")
        break
    # If answer_state are in 50 states.csv
    if answer_state in all_states:
        guessed_states.append(answer_state)
        # If they got it right:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # Create a turtle to write the name of the state at state's x and y coordinate
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

