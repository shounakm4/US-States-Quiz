import pandas
import turtle
image = 'blank_states_img.gif'
screen = turtle.Screen()
screen.title("US States Game,type \'give up\' if you wish to stop")
screen.addshape(image)
turtle.shape(image)


def name_appear(correct_state, x, y):
    state = turtle.Turtle()
    state.hideturtle()
    state.penup()
    state.speed('fastest')
    state.goto(x, y)
    state.write(f'{correct_state}', False, 'center', ('SansSerif', 10, 'normal'))
data = pandas.read_csv('50_states.csv')
states_list = data['state'].to_list()
title = 'Guess the state'
guesses = 0
game_on = True
while game_on:
    answer = screen.textinput(title,'Name the states:').lower()
    for state in states_list:
        if answer == state.lower():
            xcor = data[data.state == answer.title()].x.item()
            ycor = data[data.state == answer.title()].y.item()
            name_appear(state,xcor,ycor)
            guesses += 1
            title = f'Guessed {guesses}/50'
        else:
            pass
    if guesses == 50:
        game_on = False
        print("You are too smart!Thanks for playing!")
    if answer == 'give up':
        for state in states_list:
                xcor = data[data.state == state.title()].x.item()
                ycor = data[data.state == state.title()].y.item()
                name_appear(state, xcor, ycor)
        game_on = False
        print("Try harder next time")


screen.exitonclick()








































