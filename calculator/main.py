from tkinter import *

def btn_click(item):
    global expression
    try:
        w_field['state'] = "normal"
        expression += item
        w_field.insert(END,item)

        if item == '=':
            result = str(eval(expression[:-1]))
            w_field.insert(END, result)
            expression = ""

            w_field['state'] = "readonly"

    except ZeroDivisionError:
        w_field.delete(0, END)
        w_field.insert(0, 'Ошибка (деление на ноль)')
    except SyntaxError:
        w_field.delete(0, END)
        w_field.insert((0, 'Ошибка'))


def bt_clear():
    global expression
    expression = ""
    w_field['state'] = 'normal'
    w_field.delete(0, END)
    w_field['state'] = 'readonly'


window = Tk()
window.title('calculator')
window.geometry('268x288')
window.resizable(0, 0) # разрешение изменять окно в Tkinter

frame_input = Frame(window)
frame_input.grid(row=0, column=0, columnspan=4, sticky='nsew') # Frame - создание виджетов, grid - отображает Frame

w_field = Entry(frame_input, font='Arial 15 bold', width=24, bg='lavender', state= "readonly") # - добавление текстового поля
w_field.pack(fill=BOTH) # -  отображение текстового поля

buttons = (('7', '8', '9', '/'),
           ('4', '5', '6', '*'),
           ('1', '2', '3', '-'),
           ('0', '.', '+', '=')
            )
expression = ''
button = Button(window, text = 'C',bg='PowderBlue', fg='purple4',  command=lambda: bt_clear())
button.grid(row=1, column=3, sticky='nsew')

for row in range(4):
    for col in range(4):
        Button(window, width=2, height=3, bg='aquamarine' , fg='CadetBlue4', text=buttons[row][col], relief= 'ridge',
               command=lambda row=row, col=col: btn_click(buttons[row][col])).grid(row=row + 2, column=col, sticky="nsew", padx=1, pady=1)



window.mainloop()