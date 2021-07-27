# Import the GUI widgets that you'll be using, and create the 'app' for your program.
from guizero import App, TextBox, PushButton, Text, info
app = App()

# Function definitions for your events go here.
def btn_go_clicked():
    info("Greetings","Hello, " + txt_name.value + " - I hope you're having a nice day")

# Your GUI widgets go here
lbl_name = Text(app, text="Hello. What's your name?")
txt_name = TextBox(app)
btn_go = PushButton(app, command=btn_go_clicked, text="Done")

# Show the GUI on the screen
app.display()
