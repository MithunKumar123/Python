import function
import PySimpleGUI as psg

label = psg.Text("Type in a todo")
input_box = psg.InputText(tooltip="Enter todo",
                          key='todo')
add_button = psg.Button("Add")
list_box = psg.Listbox(values=function.get_todos(), key='todos', enable_events=True, size=[45,20])
edit_button = psg.Button("Edit")
complete_button = psg.Button("Complete")
exit_button = psg.Button("Exit")
layout = [[label],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]

window = psg.Window("My Todo App",
                    layout= layout,
                    font=('Helvetica', 21))
while True:
    event, values = window.read()

    match event:
        case 'Add':
            todos = function.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            function.write_todos(todos)
        case 'Edit':
            todo_to_edit = values["todos"][0]
            new_todo = values['todo']
            todos = function.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            function.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Complete':
            todo_to_complete = values['todos'][0]
            todos = function.get_todos()
            todos.remove(todo_to_complete)
            function.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'Exit':
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case psg.WIN_CLOSED:
            break

window.close()
