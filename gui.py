import PySimpleGUI as sg
import functions

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button("Add")

window = sg.Window('My To-Do-App', layout=[[label, input_box, add_button]], font=('roboto', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todo()
            todos.append(values['todo'] + "\n")
            functions.write_todo(todos)
        case None:
            break
window.close()
            