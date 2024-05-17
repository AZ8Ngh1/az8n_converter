import tkinter as tk

def convert():
    r1 = float(rate1.get())
    r2 = float(rate2.get())
    v = float(val.get())
    result_label.config(text = str((v/r1)*r2))

def flip():
    c1, c2 = curr1.get(), curr2.get()
    curr1.delete(0, tk.END)
    curr2.delete(0, tk.END)
    curr1.insert(0, c2)
    curr2.insert(0, c1)
    r1, r2 = rate1.get(), rate2.get()

root = tk.Tk()
root.title("az8n | конвертер")
root.configure(background='lightblue')

font = ('Helvetica', 16)

tk.Label(root, text='Валюта 1', bg='lightblue', fg='white', font=font).pack()
curr1 = tk.Entry(root)
curr1.insert(0, 'USD')
curr1.pack()

tk.Label(root, text='Цена валюты 1', bg='lightblue', fg='white', font=font).pack()
rate1 = tk.Entry(root)
rate1.insert(0, '1')
rate1.pack()

tk.Label(root, text='Валюта 2', bg='lightblue', fg='white', font=font).pack()
curr2 = tk.Entry(root)
curr2.insert(0, 'EUR')
curr2.pack()

tk.Label(root, text='Цена валюты 2', bg='lightblue', fg='white', font=font).pack()
rate2 = tk.Entry(root)
rate2.insert(0, '0.85')
rate2.pack()

tk.Label(root, text='Количество для конвертации', bg='lightblue', fg='white', font=font).pack()
val = tk.Entry(root)
val.insert(0, '1')
val.pack()

convert_button = tk.Button(root, text='_Перевести_', command=convert, bg='lightblue', fg='white', font=font)
convert_button.pack()

flip_button = tk.Button(root, text='Перевернуть', command=flip, bg='lightblue', fg='white', font=font)
flip_button.pack()


result_label = tk.Label(root, text='Результат конвертации', bg='lightblue', fg='white', font=font)
result_label.pack()

root.mainloop()
