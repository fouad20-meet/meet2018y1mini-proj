# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 23:58:42 2018

Snake Mini project Starter Code
Name:
Date:
"""
import turtle
import random
import time

turtle.tracer(1,0) 

SIZE_X=550
SIZE_Y=550
turtle.setup(800, 800)
RAINBOW = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
screen = turtle.Screen()
screen.setup(800,800)
screen.bgpic('giphy.gif')
turtle.penup()
rocks = 2
SQUARE_SIZE = 20
START_LENGTH = 2

pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
score=0
border = turtle.clone()
border.hideturtle()
border.pensize(8)
border.speed(0)
border.penup()
border.goto(300,300)
border.pendown()
border.goto(300,-300)
border.goto(-300,-300)
border.goto(-300,300)
border.goto(300,300)
border.penup()
border.goto(-150,330)
border.pendown()
border.write("SNAKE GAME!", font=("Arial", 35, "normal"))
score1 = turtle.clone()
score1.hideturtle()
score1.penup()
score1.goto(-50,-340)
score1.write("score:" + str(score), font=("Arial", 20, "normal"))
z = 0
#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for i in range(START_LENGTH) :
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1] 

#    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
#    # You're RIGHT!
    x_pos+=SQUARE_SIZE 

    my_pos=(x_pos,y_pos) #Store position variables in a tuple
    snake.goto(my_pos) #Move snake to new (x,y)
   
#    #Append the new position tuple to pos_list
    pos_list.append(my_pos) 

#    #Save the stamp ID! You'll need to erase it later. Then append
#    # it to stamp_list.
   
    
    if z == 7:
        z = 0
    snake.color(RAINBOW[z])
    stamp_id = snake.stamp()
    stamp_list.append(stamp_id)
    z += 1

###############################################################
#                    PART 2 -- READ INSTRUCTIONS!!
###############################################################
UP_ARROW = "Up" #Make sure you pay attention to upper and lower 
                #case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 244 #Update snake position after this many 
                #milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!
#
direction = UP

UP_EDGE = 300
DOWN_EDGE = -300
RIGHT_EDGE = 300
LEFT_EDGE = -300
ANGLE = 90

def up():
    global direction #snake direction is global (same everywhere)
    global DOWN
    if direction != DOWN:
        direction=UP #Change direction to up
    print("You pressed the up key!")

def down():
    global direction #snake direction is global (same everywhere)
    if direction != UP:
        direction=DOWN #Change direction to up
    print("You pressed the down key!")

def left():
    global direction #snake direction is global (same everywhere)
    if direction != RIGHT:
        direction=LEFT #Change direction to up
    print("You pressed the left key!")

def right():
    global direction #snake direction is global (same everywhere)
    if direction != LEFT:
        direction=RIGHT #Change direction to up
    print("You pressed the right key!")
#
##2. Make functions down(), left(), and right() that change direction
#####WRITE YOUR CODE HERE!!
#
turtle.onkeypress(up, UP_ARROW) # Create listener for up key
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
##3. Do the same for the other arrow keys
#####WRITE YOUR CODE HERE!!
turtle.register_shape("burger.gif") #Add trash picture
                      # Make sure you have downloaded this shape 
                      # from the Google Drive folder and saved it
                      # in the same folder as this Python script


food = turtle.clone()
food.shape("burger.gif") 

#Locations of food
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

# Write code that:
#1. moves the food turtle to each food position
#2. stamps the food turtle at that location
#3. saves the stamp by appending it to the food_stamps list using
# food_stamps.append(    )
#4. Don’t forget to hide the food turtle!
for this_food_pos in food_pos :
    ####WRITE YOUR CODE HERE!!
    food.penup()
    food.goto(this_food_pos)
    food_stamp = food.stamp()
    food_stamps.append(food_stamp)
    

def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)+1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE

        ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated
        ##                        position
    food.goto(food_x,food_y)
        ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
    food_pos.append((food_x,food_y))
        ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list
    food_stamp = food.stamp()
    food_stamps.append(food_stamp)

turtle.register_shape("rock.gif")

turtle.listen()
rock = turtle.clone()
rock.shape("rock.gif")

#Locations of food
rock_pos = []
rock_stamps = []

# Write code that:
#1. moves the food turtle to each food position
#2. stamps the food turtle at that location
#3. saves the stamp by appending it to the food_stamps list using
# food_stamps.append(    )
#4. Don’t forget to hide the food turtle!
for this_rock_pos in rock_pos :
    ####WRITE YOUR CODE HERE!!
    rock.penup()
    rock.goto(this_rock_pos)
    rock_stamp = rock.stamp()
    rock_stamps.append(rock_stamp)
    

def make_rock():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)+1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    rock_x = random.randint(min_x,max_x)*SQUARE_SIZE
    rock_y = random.randint(min_y,max_y)*SQUARE_SIZE

        ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated
        ##                        position
    rock.goto(rock_x,rock_y)
        ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
    rock_pos.append((rock_x,rock_y))
        ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list
    rock_stamp = rock.stamp()
    rock_stamps.append(rock_stamp)

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction==DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("You moved down!")
    elif direction==UP:
         snake.goto(x_pos, y_pos + SQUARE_SIZE)
         print("You moved up!")
         DOWN = UP
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        border.penup()
        border.goto(0,0)
        border.pencolor("red")
        border.write("GAME OVER", font = ("arial", 57, "normal"), align = "center")
        time.sleep(5)
        quit()
    elif new_x_pos <= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        border.penup()
        border.goto(0,0)
        border.pencolor("red")
        border.write("GAME OVER", font = ("arial", 57, "normal"), align = "center")
        time.sleep(5)
        quit()
    elif new_y_pos >= UP_EDGE:
        print("You hit the up edge! Game over!")
        border.penup()
        border.goto(0,0)
        border.pencolor("red")
        border.write("GAME OVER", font = ("arial", 57, "normal"), align = "center")
        time.sleep(5)
        quit()
    elif new_y_pos <= DOWN_EDGE:
        print("You hit the down edge! Game over!")
        border.penup()
        border.goto(0,0)
        border.pencolor("red")
        border.write("GAME OVER", font = ("arial", 57, "normal"), align = "center")
        time.sleep(5)
        quit()
    global z
    if z == 7:
        z = 0
    snake.color(RAINBOW[z])
    
    
    z += 1
#    #4. Write the conditions for UP and DOWN on your own
#    ##### YOUR CODE HERE
#
#    #Stamp new element and append new stamp in list
#    #Remember: The snake position changed - update my_pos()
#
    my_pos=snake.pos() 
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
     ######## SPECIAL PLACE - Remember it for Part 5
    global food_stamps, food_pos
    #If snake is on top of food item
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_ind]) #Remove eaten food                 
                                               #stamp
        food_pos.pop(food_ind) #Remove eaten food position
        food_stamps.pop(food_ind) #Remove eaten food stamp
        print("You have eaten the food!")
        score1.penup()
        score1.goto(-50,-340)
        global score
        score += 1
        score1.clear()
        score1.write("score:" + str(score), font=("Arial", 20, "normal"))
        global TIME_STEP 
        if TIME_STEP == 1:
            pass
        else:
            TIME_STEP = TIME_STEP - 9
    else:
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
    global rocks

    if score % 10 == 0:
        rocks = 2 + score// 10
    #pop zeroth element in pos_list to get rid of last the last 
    #piece of the tail
    
    if len(rock_stamps) <= rocks:
        make_rock()
    if snake.pos() in rock_pos:
        border.penup()
        border.goto(0,0)
        border.pencolor("red")
        border.write("GAME OVER", font = ("arial", 57, "normal"), align = "center")
        time.sleep(5)
        quit()
    if len(food_stamps) <= 5 :
        make_food()
    turtle.ontimer(move_snake,TIME_STEP)
    if snake.pos() in pos_list[:-1]:
        print("the body touched the head")
        border.penup()
        border.goto(0,0)
        border.pencolor("red")
        border.write("GAME OVER", font = ("arial", 57, "normal"), align = "center")
        time.sleep(5)
        quit()

    
move_snake()
