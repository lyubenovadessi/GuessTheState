import turtle
from turtle import Screen
import pandas

def get_state_lon_lat(x, y):
    """Take the lat/lon position of the state by clicking on each state on the map"""
    print(x, y)
# turtle.onscreenclick(get_state_lon_lat)
# turtle.mainloop()

ALIGNMENT = 'center'
FONT = ('Courier', 40, 'normal')
SET_TIME = 300

screen = Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_file = pandas.read_csv('50_states.csv')
all_states = states_file.state.to_list()

remaining_time = SET_TIME
time_up = False


def format_time(seconds_left):
    minutes = seconds_left // 60
    seconds = seconds_left % 60
    return f"{minutes}:{seconds:02d}"


def countdown():
    """Display the remaining time; once the timer reaches 0 the final score is displayed"""
    global remaining_time, time_up
    if remaining_time > 0:
        remaining_time -= 1
        screen.title(f"⏱️ Time left: {format_time(remaining_time)}")
        screen.ontimer(countdown, 1000)
    else:
        screen.title("⏰ Time’s up!")
        time_up = True
        screen.clear()
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(0, 0)
        turtle.write(f"YOUR SCORE IS 🏁{len(guessed_states)}/50", align=ALIGNMENT, font=FONT)


guessed_states = []
countdown()

while len(guessed_states) < 50 and not time_up:
    answer_state = screen.textinput(
        title=f"🏁{len(guessed_states)}/50",
        prompt="🗺️Guess the States📌 (or type Exit)"
    ).title()

    #in case time's up during the user is typing
    if time_up:
        break
    #in case user closes the prompt
    if answer_state is None:
        break

    if answer_state == "Exit":
        missed_states = [state for state in all_states if state not in guessed_states]
        missed_states_file = pandas.DataFrame(missed_states)
        missed_states_file.to_csv("missed_states_file.csv")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states_file[states_file.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())

if not time_up and len(guessed_states) == 50:
    screen.clear()
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(0, 0)
    turtle.write("💥💥💥💥CONGRATS💥💥💥💥", align=ALIGNMENT, font=FONT)
    screen.exitonclick()
