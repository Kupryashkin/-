import tkinter as tk

def say_hello():
    global entry
    name = entry.get()
    label_hello.config(text=f"Привет, {name}!")
    label_length.config(text=f"Количество символов в имени: {len(name)}")

def print_message():
    print("Простая функция была вызвана!")

root = tk.Tk()
root.title('Белка в колесе :)')
root.geometry("700x300+600+500")
root.resizable(False, False)
root.config(bg='#495b52')

l1 = tk.Label(root, text='Йоу! Вводи свое имя',
              bg='#495b52',
              fg='#ffffff',
              font=('Soledago', 20, 'bold'),
              padx=20,
              pady=30)
l1.pack()

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

button = tk.Button(root, text="Нажимай",
                   bg='#7abb61',
                   command=say_hello)
button.pack()

label_hello = tk.Label(root, text=":)", bg='#495b52')
label_hello.pack(pady=50)
label_length = tk.Label(root, text="")
label_length.pack(pady=10)

root.mainloop()