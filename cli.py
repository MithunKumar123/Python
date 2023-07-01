import function as module
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
user_prompt = 'Enter a todo:'
print(f"Today's date is: {now}")
while True:
    action = input("Enter add or show or edit or complete or exit: ").strip()

    if action.startswith('add'):
        todo = action[4:] + "\n"
        todos = module.get_todos()
        todos.append(todo)
        module.write_todos(todos)

    elif action.startswith('show'):
        todos = module.get_todos()
        new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(new_todos):
            row = f"{index + 1}){item}"
            print(row)

    elif action.startswith('edit'):
        try:
            number = int(action[5:])
            new_todo = input("Enter the new value: ") + "\n"
            todos = module.get_todos()
            todos[number - 1] = new_todo
            module.write_todos(todos)
        except ValueError:
            print("Enter a valid command to do operation")
            continue

    elif action.startswith('complete'):
        try:
            number = int(action[9:])
            todos = module.get_todos()
            todo_to_remove = todos.pop(number - 1).strip('\n')
            module.write_todos(todos)
            message = f"Todo {todo_to_remove} was completed from the list of todos"
            print(message)
        except IndexError:
            print("There is no item with this number. Please enter a valid number")
            continue

    elif action.startswith('exit'):
        break
    else:
        print("Command is invalid")

print('Bye! See you later...')
