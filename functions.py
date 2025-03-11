FILEPATH="files/todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and returns a list of
    to-do list
    """
    with open(filepath, "r") as file:
        todos_local=file.readlines()
    return todos_local

def write_todos(todos_arg, filename=FILEPATH):
    """ Write a to-do items list in the given file."""
    with open(filename, "w") as file:
        file.writelines(todos_arg)
