import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Proj24-US_States/blank_states_img.gif"
screen.setup(height=491, width=725)
screen.addshape(image)
turtle.shape(image)

states = pd.read_csv("Proj24-US_States/50_states.csv")
state_names = states.state.to_list()
guessed_states = []

score = 0
while len(guessed_states) < 50:
    answer_state = str(screen.textinput(
        title=f"{score}/{len(state_names)} States Correct", prompt="Enter a State's name:")).strip().title()

    if answer_state == "Exit":
        missing_states = [state for state in state_names if state not in guessed_states]
        data = pd.DataFrame(missing_states)
        data.to_csv("Proj25-NATO_Alphabet/states_to_learn.csv")
        break

    if answer_state in state_names:
        guessed_states.append(answer_state)
        score += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
