notebook = {}
def add_note():
    litlup = input("Введи название заметки: ")
    text = input("Введи текст: ")
    notebook[litlup] = text
    print("Ты добавил заметку")

def read_note():
    if len(notebook) == 0:
        print("Заметок нету :)")
    else:
        print("Доступные заметки: ")
        for litlup in notebook:
            print(litlup)
            litlup = input("Введи название заметки, которую хош прочесть: ")
            if litlup in notebook:
                print(notebook[litlup])
            else:
                print("Такой нет брат")

def menu():
    while True:
        litlup = ("Выбери действие: \n1. Добавить заметку\n2. Прочесть заметку\n3. Выйти\n")
        if litlup =="1":
            add_note()
        elif litlup == '2':
            read_note()
        elif litlup == "3":
            break
        else:
            print("Попробуйте снова")

menu()
