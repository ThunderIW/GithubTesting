from dearpygui import  core, simple

def myfunction(sender,data):
    print("Sender : ", sender)
    print("Data :", data)

def exitProgramFunc(sender,data):
    print(data)
    if data=="ExitGui":
        core.stop_dearpygui()

def myfunction2(sender,data):
    userName=core.get_value("username")
    password=core.get_value("password")
    print(f"username : {userName}")
    print(f"Password : {password}")


##simple.show_style_editor()
core.set_theme("Classic")
##simple.show_documentation()




with simple.window("TEST"):
    core.add_button("Click here",callback=myfunction,callback_data="Working....1")
    core.add_button("Button",callback=myfunction,callback_data="Working....2")
    core.set_main_window_size(500,500)

with simple.window("TEST Win 2",autosize=True,x_pos=150,y_pos=200):
    core.add_input_text(name="username",hint="Enter username",on_enter=True, callback=myfunction2)
    core.add_input_text(name="password",hint="Enter password",password=True, on_enter=True, callback=myfunction2)
    core.add_button("Send",callback=myfunction2)
    core.add_button("Exit",callback_data="ExitGui",callback=exitProgramFunc)
core.start_dearpygui()