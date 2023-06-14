from functions import get_todo, write_todo
import time
# tạo file zip
    # import shutil
    # shutil.make_archive("to_do", "zip", "to_do_list")
#duyệt các file có cùng kiểu
    # import glob
    # files = glob.glob("to_do_list/*.txt")
    # for file in files:
    #     print(file)
#tìm kiếm cho người dùng
    # import webbrowser
    # search = input("Enter a request: ").replace(" ","+") # trong url tìm kiếm dấu cách = dấu cộng
    # webbrowser.open("https://www.google.com/search?q=" + search)
now = time.strftime("%d %b, %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Enter type add, show, edit, complete or exit: ")
    if 'add' in user_action:
        todos = get_todo()
        todo = input("Enter a todo: ")
        todos.append(todo + "\n")
        write_todo(todos)
    elif 'show' in user_action:
        todos = get_todo()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}.{item}")
    elif 'edit' in user_action:
        todos = get_todo()
        number = int(input("Number of todo you want to edit: "))
        number -= 1
        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + "\n"
        write_todo(todos)
    elif 'complete' in user_action:
        todos = get_todo()
        number = int(input("Todo you completed: "))
        todos.pop(number - 1)
        write_todo(todos)
    elif 'exit' in user_action:
        break
    else:
        print("Command is not valid")
print("Bye!")
