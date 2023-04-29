# this program can read any gif image and read any csv to create a replica of the game
import turtle

import pandas

from state import State
from scoreboard import Scoreboard

ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")

screen = turtle.Screen()
screen.title("U.S State Game ")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# this the way to get the x and y coordinate of the states in the image
#def get_mouse_click_cor(x, y):
#    print(x, y)
#
#
#turtle.onscreenclick(get_mouse_click_cor)

state = State("50_states.csv")
scoreboard = Scoreboard()

game_is_on = 0
guessed_states = []

while game_is_on < 50:
    answer_state = screen.textinput(title=f"{game_is_on}/50 states correct", prompt="what is another state name ?")
    answer = answer_state.lower()
    guessed_states.append(answer)
    if answer == "exit":
        missing_state = [states for states in state.state_list if states not in guessed_states]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if state.get_state(answer):
        scoreboard.increase_score()
        game_is_on += 1


