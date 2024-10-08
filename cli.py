from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            print(f"{index + 1}-{item}")

    elif user_action.startswith("edit"):
        try:
            num = int(user_action[5:])

            todos = get_todos()

            todos[num - 1] = input("Enter the new todo:") + '\n'

            write_todos(todos)

        except ValueError:
            print("Your edit command is wrong!")
            continue

    elif user_action.startswith("complete"):
        try:
            num = int(user_action[9:])

            todos = get_todos()

            todo_to_remove = todos[num - 1].strip('\n')
            todos.pop(num - 1)

            write_todos(todos)

            message = f"Todo {todo_to_remove} has been removed from the list"
            print(message)
        except IndexError:
            print("There is no todo associated with this number")
            continue


    elif "exit" in user_action:
        break

    else:
        print("Command is not valid")

print("Bye!")
