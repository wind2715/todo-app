FILE_PATH = "to_do_list/list.txt"


def get_todo():
    with open(FILE_PATH, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todo(todos_local):
    with open(FILE_PATH, 'w') as file:
        file.writelines(todos_local)
