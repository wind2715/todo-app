import PySimpleGUI as sg
import functions

label_add = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button("Add")

label_box = sg.Text("List to-do")
list_box = sg.Listbox(values=functions.get_todo(), key='todos', enable_events=True, size=(45, 10))

label_edit = sg.Text("Choose a to-do in list to edit")
input_edit = sg.InputText(tooltip='Edit todo', key='edit_todo')
edit_button = sg.Button("Edit")

window = sg.Window('My To-Do-App', layout=[[label_add], [input_box, add_button], [label_box], [list_box], [label_edit], [input_edit, edit_button]], font=('roboto', 15))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todo()
            todos.append(values['todo'] + "\n")
            functions.write_todo(todos)
            window['todos'].update(values=todos)

        case "todos":
            window['edit_todo'].update(value=values['todos'][0])

        case "Edit":
            current_todo = values['todos'][0]
            new_todo = values['edit_todo']
            todos = functions.get_todo()
            index = todos.index(current_todo)
            todos[index] = new_todo
            functions.write_todo(todos)
            window['todos'].update(values=todos)

        case None:
            break
            
window.close()
