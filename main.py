import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
name=data.state.to_list()
guessed_states=[]

while len(guessed_states) < 51:
    answer_state = turtle.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name").title()
    if answer_state=="Exit":
        missing_states = [names for names in name if names not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in name:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

#States to learn .csv

turtle.mainloop()






