from guizero import App, Text, Box, PushButton, TextBox

app = App()

# Divide the flag into two sections, a top layer containing the cross and a red block
# and a bottom, red layer.

top = Box(app, align="top", width="fill")
bottom = Box(app, width="fill", height="fill")

# Create a box to contain the cross, aligned left in the top layer.
cross = Box(top, align="left")
cross.bg = "blue"
cross_btn=PushButton(cross,text="test")

# Two boxes are needed to construct the cross.
flag = Box(cross)
# Set the background to white.
flag.bg = "white"
# Make the upper parts of the cross out of four equal sized, red blocks.
first = Text(flag,text="1", bg="red", align="top", height=1, width=3)
second = Text(flag,text="2", bg="red", align="left", height=1, width=3)
third = Text(flag,text="3", bg="red", align="left", height=1, width=3)
fourth = Text(flag,text="4", bg="red", align="left", height=1, width=3)
# Create the second box directly below the first, so that the final piece
# of the cross will be added to the bottom of the cross. Try running the
# program without this box to see where it would automatically be placed.

app.display()
