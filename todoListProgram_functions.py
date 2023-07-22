FILENAME = "todos.txt"


def get_todos(filename=FILENAME):
    """Read a text file and
    return a list of todo items in the list
    """
    with open(filename, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filename=FILENAME):
    """Write a list of todo items to a text file"""
    with open(filename, 'w') as file:
        file.writelines(todos_arg)

