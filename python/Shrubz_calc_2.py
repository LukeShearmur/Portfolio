from tkinter import *


expression =""

def press(num):
    global expression

    expression = expression + str(num)

    equation.set(expression)

def equals():

    try:

        global expression

        total = str(eval(expression))

        equation.set(total)

        expression = ""
    
    except:
        equation.set(" error ")
        expression = ""

def clear():
    global expression
    expression=""
    equation.set("")

if __name__ == "__main__":
    t=Tk()
    t.configure(background = "light grey")
    t.title("Welcome to Shrubz Calc 2.0",)
    t.geometry("320x224")

    equation = StringVar()
    expression_field = Entry(t, textvariable = equation)
    expression_field.grid(columnspan = 4, ipadx = 70)

    button1 = Button(t, text = ' 1 ', fg='black', bg= 'light green', command=lambda: press(1), height = 2, width = 10)

    button1.grid(row=2, column=0)

    button2 = Button(t, text = ' 2 ', fg='black', bg= 'light green', command=lambda: press(2), height = 2, width = 10)

    button2.grid(row=2, column=1)

    button3 = Button(t, text = ' 3 ', fg='black', bg= 'light green', command=lambda: press(3), height = 2, width = 10)

    button3.grid(row=2, column=2)

    button4 = Button(t, text = ' 4 ', fg='black', bg= 'light green', command=lambda: press(4), height = 2, width = 10)

    button4.grid(row=3, column=0)

    button5 = Button(t, text = ' 5 ', fg='black', bg= 'light green', command=lambda: press(5), height = 2, width = 10)

    button5.grid(row=3, column=1)

    button6 = Button(t, text = ' 6 ', fg='black', bg= 'light green', command=lambda: press(6), height = 2, width = 10)

    button6.grid(row=3, column=2)

    button7 = Button(t, text = ' 7 ', fg='black', bg= 'light green', command=lambda: press(7), height = 2, width = 10)

    button7.grid(row=4, column=0)

    button8 = Button(t, text = ' 8 ', fg='black', bg= 'light green', command=lambda: press(8), height = 2, width = 10)

    button8.grid(row=4, column=1)

    button9 = Button(t, text = ' 9 ', fg='black', bg= 'light green', command=lambda: press(9), height = 2, width = 10)

    button9.grid(row=4, column=2)

    button0 = Button(t, text = ' 0 ', fg='black', bg= 'light green', command=lambda: press(0), height = 2, width = 10)

    button0.grid(row=5, column=0)

    plus = Button(t, text = ' + ', fg = 'black', bg= 'light blue', command=lambda: press("+"), height = 2, width= 10)

    plus.grid(row=2, column=3)

    minus = Button(t, text = ' - ', fg='black', bg='light blue', command=lambda: press("-"), height = 2, width = 10)

    minus.grid(row=3, column=3)

    divide = Button(t, text = ' / ', fg='black', bg='light blue', command=lambda: press("/"), height = 2, width = 10)

    divide.grid(row=4, column=3)

    multiply = Button(t, text = ' * ', fg='black', bg='light blue', command=lambda: press("*"), height = 2, width = 10)

    multiply.grid(row=5, column=3)

    decimal = Button(t, text = ' . ', fg='black', bg='light blue', command=lambda: press("."), height = 2, width = 10)

    decimal.grid(row=6, column=0)

    clear = Button(t, text = 'Clear', fg='black', bg='light blue', command=clear, height = 2, width = 10)

    clear.grid(row=5, column=2)

    equal = Button(t, text = ' = ', fg='black', bg= 'light blue', command=equals, height = 2, width = 10)

    equal.grid(row=5, column=1)


    t.mainloop()
