# Hurdle exercise
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if front_is_clear():
        move()
        if right_is_clear():
            turn_right()
    else:
        turn_left()

# Maze
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
right_turns = 0  

while not at_goal():
    if right_is_clear() and right_turns < 4:
        turn_right()
        move()
        right_turns += 1
    elif front_is_clear():
        move()
        right_turns = 0
    else:
       turn_left()
       right_turns = 0