from guizero import App,TextBox,Text,Box,PushButton,Combo,Slider,MenuBar,ButtonGroup

def open_file():
    with open(file_name.value,"r") as f:
        editor.value=f.read()

def save_file():
    with open(file_name.value,'w') as f:
        f.write(editor.value)
        save_btn.disable()

def enable_save_btn():
    save_btn.enable()

def editor_font():
    editor.font=font.value

def editor_size():
    editor.text_size=size.value
#    editor.resize(1,1)
#    editor.resize("fill","fill")

def exit_app():
    if save_btn.enabled==True:
        warning()
        app.destroy()
    else:
        app.destroy()

def warning():
    save_warning=app.yesno("File hasn't been saved", "Do you want to save file?")
    if  save_warning ==True:
        save_file()
        app.destroy()
    else:
        app.destroy()

def theme():
    if theme_mode.value=="Light mode":
        editor.text_color = "black"
        editor.bg = "white"
    elif theme_mode.value=="Dark mode":
        editor.text_color = "white"
        editor.bg = "black"

app=App(title="Text editor",width=600,height=600)

menubar=MenuBar(app,
                toplevel=["File","Edit"],
                options=[
                    [["Open",open_file],["Save",save_file],["Exit",exit_app]],
                    [["Undo",exit_app]]
                ])

file_controls=Box(app,align="top",width="fill")
file_name=TextBox(file_controls,text="text_file.txt",width=60,align="left")
open_btn=PushButton(file_controls,text="Open",command=open_file,align="left")
save_btn=PushButton(file_controls,text="Save",command=save_file,align="right")

preference_controls=Box(app,width="fill")
font_txt=Text(preference_controls,text="Font",align="left")
font=Combo(preference_controls,options=["Time news roman","Courier","Arial"],command=editor_font,align="left")

size_txt=Text(preference_controls,text="size",align="left")
size=Slider(preference_controls,start=8,end=42,command=editor_size,align="left")

editor=TextBox(app,multiline=True,width="fill",height="fill",command=enable_save_btn)

theme_mode= ButtonGroup(preference_controls, options=["Light mode", "Dark mode"],
                        selected="Light mode",
                        command=theme)


save_btn.enabled=False


app.when_closed=warning



app.display()

