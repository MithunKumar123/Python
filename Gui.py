import function
import PySimpleGUI as psg

label = psg.Text("Type in a todo")
input_box = psg.InputText(tooltip="Enter todo",
                          key='todo')
add_button = psg.Button("Add")
window = psg.Window("My Todo App",
                    layout=[[label], [input_box, add_button]],
                    font=('Helvetica', 21))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = function.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            function.write_todos(todos)
        case psg.WIN_CLOSED:
            break

window.close()
