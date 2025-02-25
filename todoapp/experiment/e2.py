user_prompt = "enter todo:"
todos = []

while True:
    todo = input(user_prompt)
    print(todo.title())
    todos.append(todo)