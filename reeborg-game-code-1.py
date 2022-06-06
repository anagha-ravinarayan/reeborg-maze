def turn_right():
    turn_left()
    turn_left()
    turn_left()

def do_one_round():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()

for num in range(0,5):
    do_one_round()
    turn_left()

do_one_round()
