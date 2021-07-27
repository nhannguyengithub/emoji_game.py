import os
from random import shuffle,randint
from guizero import App, Box, Picture,PushButton,Text,yesno,TextBox

#read high score
names=[]
scores=[]
try:
    with open("highscore_emoji.txt", "r") as f:
        for line in f:
            line = line.strip("\n")
            line = line.split(" ")
            names.append(line[0])
            scores.append(int(line[1]))

except FileNotFoundError:
    with open("highscore_emoji.txt", "w") as f:
        f.write("player1 0")
    names[0] = "player1"
    scores[0]=0

app = App("Emoji Match",width=400,height=550)

#creat box to house player name and score
info=Box(app,layout="grid")

#player name
player_lbl=Text(info,text="Player: ",grid=[0,0])
player_name=TextBox(info,text="Player1",grid=[1,0])

#score
score_lbl=Text(info,text="Score: ",grid=[2,0])
score_txt=Text(info,grid=[3,0])

#highscore
highscore_lbl=Text(info,text="Highscore: ",grid=[4,0])
highscore_name=Text(info,grid=[5,0])
highscore_name.value=names[0]
highscore_txt=Text(info,grid=[6,0])
highscore_txt.value=scores[0]


#result message
result=Text(app)

#extra features box
extra_features=Box(app)
timer=Text(extra_features,text="GET READY!!!",align="left")

# create a box to house the grid
pictures_box = Box(app, layout="grid")
button_box=Box(app,layout="grid")

# create an empty list to which pictures will be added
pictures = []
buttons=[]
count_down_time=30
score_txt.value=0

for x in range(0,3):
    for y in range(0,3):
        # put the pictures into the list
        picture = Picture(pictures_box, grid=[x,y])
        pictures.append(picture)

        button=PushButton(button_box,grid=[x,y])
        buttons.append(button)

def match_emoji(matched):
    if matched:
        result.value=" "
        set_round()
        score_txt.value=int(score_txt.value)+1

    else:
        result.value="INCORRECT!!!"

def counter():
    timer.value = int(timer.value) - 1
    if int(timer.value) == 0:
        # reset the timer
        timer.cancel(counter)
        add_highscore(names,scores)
        #create another game when time out
        play_more=yesno("Time out","Play another game?")
        if play_more:
            timer.value=count_down_time
            set_round()
            score_txt.value=0
            timer.repeat(1000,counter)
            highscore_name.value=names[0]
            highscore_txt.value=scores[0]
        else:
            app.destroy()

def add_highscore(names,scores):
    position = 0
    score=int(score_txt.value)
    name=player_name.value

    for compare_score in scores:
        if score < compare_score:
            position = position + 1
    scores.insert(position, score)
    names.insert(position, name)

    scores = scores[:10]
    names = names[:10]
    with open("highscore_emoji.txt", 'w') as f:
        for pos in range(len(names)):
            f.write(names[pos] + " " + str(scores[pos]) + "\n")

def set_round():
    # set the path to the emoji folder on your computer
    emojis_dir = "emojis"
    # create a list of the locations of the emoji images
    emojis = [os.path.join(emojis_dir, f) for f in os.listdir(emojis_dir) if
              os.path.isfile(os.path.join(emojis_dir, f))]
    # shuffle the emojis
    shuffle(emojis)
    # for each picture in the list
    for picture in pictures:
        # make the picture a random emoji
        picture.image = emojis.pop()

    for button in buttons:
        button.image = emojis.pop()
        button.update_command(match_emoji, [False])

    random_picture = randint(0, 8)
    randon_button = randint(0, 8)

    matched_emoji = pictures[random_picture].image
    buttons[randon_button].image = matched_emoji
    buttons[randon_button].update_command(match_emoji, [True])

set_round()

# start the timer
timer.value = count_down_time
timer.repeat(1000, counter)

app.display()
