def get_todos(filepath="files/todos.txt"):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="files/todos.txt"):
    """write the todos into the file"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


if __name__ == '__main__':
    print("We are in the function.py. Currently running the function.py directly")