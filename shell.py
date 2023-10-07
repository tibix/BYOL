import basic

running = True

while running:
    text = input("basic > ")
    if text in ["quit", "exit", "stop", "end"]:
        running = False

    result, error = basic.run("<stdin>", text)

    if error:
        print(error.as_string())
    else:
        print(result)
