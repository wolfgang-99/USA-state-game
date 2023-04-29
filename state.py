import pandas
from turtle import Turtle

FRONT = ("Arial", 7, "normal")


class State:
    def __init__(self, file_to_read):
        self.data = pandas.read_csv(file_to_read)
        self.state_colum = self.data["state"]
        self. state_data = self.state_colum.str.lower()
        self.state_list = self.state_data.to_list()

    def get_state(self, answer):
        if answer in self.state_list:
            state = self.data[self.state_data == answer]
            state_name = state["state"].item()

            state_x = int(state["x"])
            state_y = int(state["y"])

            state_written = Turtle()
            state_written.color("black")
            state_written.penup()
            state_written.goto(x=state_x, y=state_y)
            state_written.write(f"{state_name}", font=FRONT)
            state_written.hideturtle()
            return True
        else:
            return False
