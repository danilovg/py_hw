def func():
    book = {}
    a = 0
    while a != "q":
        print("Нажмите q для выхода")
        print()
        print("Введите свое имя: ")
        a = input()
        if a == "q":
            break
        print("Введите свой номер: ")
        b = input()
        if len(b) == 16:
            if b[0] == "+" and b[1].isdigit() and b[2] == "-" and b[6] == "-" and b[10] == "-" and b[13] == "-" and b[3:6].isdigit() and b[7:10].isdigit() and b[11:13].isdigit() and b[14:17]:
                book[a] = b
            else:
                print("Неправильный номер")
                print()
        else:
            print("Неправильный номер")
            print()
    print(book)

func()