def turn_right():
    turn_left()
    turn_left()
    turn_left()

# get in a position where there is a wall to the right
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
