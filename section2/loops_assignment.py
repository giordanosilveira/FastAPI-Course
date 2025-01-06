my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for i in range(0, 3):
    for element in my_list:
        if element == "Monday":
            continue
        print(element)