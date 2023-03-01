import turtle
import pandas

score = 0

ALIGNMENT = "center"
FONT = ("Arial", 7, "normal")

screen = turtle.Screen()
screen.title("Name the States")

image = "blank_states_img.gif"
screen.addshape(image)
img = turtle.Turtle()
img.shape(image)
coord_pos = turtle.Turtle()
coord_pos.hideturtle()



def is_state():
    screen.tracer(0)
    coord_pos.penup()
    list_states = data[data.state == f"{answer_state}"]
    state_coord_x = float(list_states["x"])
    state_coord_y = float(list_states["y"])
    coord_pos.goto(state_coord_x, state_coord_y)
    coord_pos.color("black")
    coord_pos.write(f"{answer_state}", False, ALIGNMENT, FONT)
    screen.update()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
correct_guesses = []


while score < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct.", prompt="Whats another State's name?\nType 'exit' to Quit.").title()

    if answer_state == "Exit":
        states_to_learn = [state for state in all_states if state not in correct_guesses]
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break



    if answer_state in all_states:
        correct_guesses.append(answer_state)
        is_state()
        score += 1
    # for state in data["state"]:
        # if answer_state in correct_guesses:
        #     answer_state = screen.textinput(title=f"{score}/50 States Correct.",
        #                                     prompt="Whats another State's name?\nType 'exit' to Quit.").title()

