import turtle
import pandas

screen = turtle.Screen()
screen.title("INDIAN STATE GAME")
image = "India.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 33:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/33 States Correct",
                                    prompt="What's another state's name?").title()

    #if answer_state is one of the state in all the states of the 31 states.
    if answer_state == "Exit":
        missing_state =[state for state in all_states if state not in guessed_state]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("State_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

#state to learn csv
screen.exitonclick()
