# coding=gbk
import tkinter
import math

class calculator:
    def __init__(self):
        #Initialized Interface
        self.root = tkinter.Tk()
        self.root.title('Calculator')
        self.root['bg'] = '#cadddb'
        self.root.minsize(265, 320)
        self.root.resizable(False, False)

        # Setting the initial value on display 
        self.value1 = tkinter.StringVar()
        self.value1.set('0')

        # define an invariant to check if the number is negative
        self.ispresign = False
        # set an array for storing the number clicked
        self.numlist = []
        # define an invariant to check if equal sign is clicked
        self.isequalsign = 0
        # define an invariant to check if special sign is clicked
        self.specialsign = 0

        #Call a Layout
        self.show()
        
        self.root.mainloop()
        
    # Layout function
    def show(self):

        # Total menu
        self.allmenu = tkinter.Menu()
        # Adding submenu
        self.file = tkinter.Menu(tearoff=0)
        # Adding options to submenu board
        self.file.add_command(label='Introduction',command = self.introduce)
        self.file.add_command(label='Exit', command=self.root.quit)
        # Adding submenu to Total menu
        self.allmenu.add_cascade(menu=self.file, label='File')
        self.root.config(menu=self.allmenu)

        # display area setting
        show = tkinter.Label(textvariable=self.value1, anchor='e', bg='white', font=('Arial', 15), bd=10)
        show.place(x=10, y=5, width=245, height=35)

        # Button Number
        btn0 = tkinter.Button(text='0', command=lambda: self.pressnum('0'))
        btn0.place(x=10, y=270, width=95, height=40)

        btnpoint = tkinter.Button(text='.', command=lambda: self.pressnum('.'))
        btnpoint.place(x=110, y=270, width=45, height=40)

        btn1 = tkinter.Button(text='1', command=lambda: self.pressnum('1'))
        btn1.place(x=10, y=225, width=45, height=40)

        btn2 = tkinter.Button(text='2', command=lambda: self.pressnum('2'))
        btn2.place(x=60, y=225, width=45, height=40)

        btn3 = tkinter.Button(text='3', command=lambda: self.pressnum('3'))
        btn3.place(x=110, y=225, width=45, height=40)

        btn4 = tkinter.Button(text='4', command=lambda: self.pressnum('4'))
        btn4.place(x=10, y=180, width=45, height=40)

        btn5 = tkinter.Button(text='5', command=lambda: self.pressnum('5'))
        btn5.place(x=60, y=180, width=45, height=40)

        btn6 = tkinter.Button(text='6', command=lambda: self.pressnum('6'))
        btn6.place(x=110, y=180, width=45, height=40)

        btn7 = tkinter.Button(text='7', command=lambda: self.pressnum('7'))
        btn7.place(x=10, y=135, width=45, height=40)

        btn8 = tkinter.Button(text='8', command=lambda: self.pressnum('8'))
        btn8.place(x=60, y=135, width=45, height=40)

        btn9 = tkinter.Button(text='9', command=lambda: self.pressnum('9'))
        btn9.place(x=110, y=135, width=45, height=40)

        # simple calculation button (plus / minus / product / division)
        btnplus = tkinter.Button(text='+', command=lambda: self.presign('+'))
        btnplus.place(x=160, y=270, width=45, height=40)

        btnminus = tkinter.Button(text='-', command=lambda: self.presign('-'))
        btnminus.place(x=160, y=225, width=45, height=40)

        btnproduct = tkinter.Button(text='X', command=lambda: self.presign('*'))
        btnproduct.place(x=160, y=180, width=45, height=40)

        btndivide = tkinter.Button(text='¡Â', command=lambda: self.presign('/'))
        btndivide.place(x=160, y=135, width=45, height=40)

        # special operator (sine, cos, tan, ln, log, 1/x, x^2...)
        btnsine = tkinter.Button(text='sin', command=lambda: self.special('sin'))
        btnsine.place(x=10, y=45, width=45, height=40)
        
        btncos = tkinter.Button(text='cos', command=lambda: self.special('cos'))
        btncos.place(x=60, y=45, width=45, height=40)
        
        btntan = tkinter.Button(text='tan', command=lambda: self.special('tan'))
        btntan.place(x=110, y=45, width=45, height=40)
        
        btnln = tkinter.Button(text='ln', command=lambda: self.special('ln'))
        btnln.place(x=160, y=45, width=45, height=40)
        
        btnlog = tkinter.Button(text='log', command=lambda: self.special('log'))
        btnlog.place(x=210, y=45, width=45, height=40)

        btnreciprocal = tkinter.Button(text='1/x', command=lambda: self.special('1/x'))
        btnreciprocal.place(x=10, y=90, width=45, height=40)

        btnroot = tkinter.Button(text='sqrt', command=lambda: self.special('sqrt'))
        btnroot.place(x=60, y=90, width=45, height=40)

        btnsquare = tkinter.Button(text='©O', command=lambda: self.special('m2'))
        btnsquare.place(x=110, y=90, width=45, height=40)

        btnnegative = tkinter.Button(text='+/-', command=lambda: self.special('+/-'))
        btnnegative.place(x=160, y=90, width=45, height=40)

        btnclean = tkinter.Button(text='C', command=lambda: self.special('C'))
        btnclean.place(x=210, y=90, width=45, height=40)

        btndel = tkinter.Button(text='¡û', command=lambda: self.special('¡û'))
        btndel.place(x=210, y=180, width=45, height=40)

        btnclear = tkinter.Button(text='CE', command=lambda: self.special('CE'))
        btnclear.place(x=210, y=135, width=45, height=40)

        btnequal = tkinter.Button(text='=', command=lambda: self.presseq('='))
        btnequal.place(x=210, y=225, width=45, height=85)

    def introduce(self):
        #Build a new brief introduction window
        self.newroot = tkinter.Toplevel(relief='sunken', bd=10)
        # Set Title
        self.newroot.title('Introduction')
        # Set Minimum size
        self.newroot.minsize(350, 200)
        # Set Maximum size
        self.newroot.maxsize(600, 400)
        # Not allowed to adjust the size
        self.newroot.resizable(True, True)

        # Hide the windown and delete the window
        btn = tkinter.Button(self.newroot,bg = 'white',justify = 'left',anchor = 'nw',state = 'disabled',font= ('Arial', 10), bd=10, text='It is a simple calculator like you used before.\n\nAttention: \nSpecial Function should type number firstly.\nFor example: sin(90) --> 90 sin\n                    sqrt(2) --> 2 sqrt\n\n')
        btn.place(width = 350,height = 200)

    # function of press number 0,1,2,...9
    def pressnum(self,num):
        if self.ispresign == True:
            self.value1.set('0')
            self.ispresign = False
        if self.isequalsign == 1:
            self.value1.set('0')
            self.isequalsign = 0
        if self.specialsign == 1:
            self.value1.set('0')
            self.specialsign = 0
        oldnum = self.value1.get()
        if oldnum == 'Divisor CANNOT be Zero':
            return
        else:
            if num == '.' and num in oldnum:
                res = oldnum
            elif num == '.' and oldnum == '0':
                res = oldnum + '.'
            elif oldnum == '0':
                res = num
            else:
                res = oldnum + num
            self.value1.set(res)

    # Function of press presign
    def presign(self,sign):
        if self.ispresign == True and self.numlist != []:  # True  ever pressed
            self.numlist[-1] = sign  
        else:
            oldnum = self.value1.get()
            if oldnum == 'Divisor CANNOT be Zero':
                self.value1.set('Divisor CANNOT be Zero')
            else:
                self.numlist.append(oldnum)
                self.numlist.append(sign)
        self.ispresign = True

    # Function of pressing special button
    def special(self,sign):
        strs = self.value1.get()
        if sign == 'sin':
            if strs != 'Divisor CANNOT be Zero':
                res = math.sin(math.radians(eval(strs)))
            else:
                res = strs
        elif sign == 'cos':
            if strs != 'Divisor CANNOT be Zero':
                res = math.cos(math.radians(eval(strs)))
            else:
                res = strs
        elif sign == 'tan':
            if strs != 'Divisor CANNOT be Zero':
                res = math.tan(math.radians(eval(strs)))
            else:
                res = strs
        elif sign == 'ln':
            if strs != 'Divisor CANNOT be Zero':
                res = math.log(eval(strs))
            else:
                res = strs
        elif sign == 'log':
            if strs != 'Divisor CANNOT be Zero':
                res = math.log(eval(strs),10)
            else:
                res = strs
                
        elif sign == '1/x':
            if strs != 'Divisor CANNOT be Zero':
                if eval(strs) != 0:
                    res = eval('1/' + strs)
                else:
                    res = strs
            else:
                res = strs
        elif sign == 'sqrt':
            if strs != 'Divisor CANNOT be Zero':
                if eval(strs) > 0:
                    res = math.sqrt(eval(strs))
                else:
                    res = strs
            else:
                res = strs
        elif sign == 'm2':
            if strs != 'Divisor CANNOT be Zero':
                res = eval(strs + '*' + strs)
            else:
                res = strs
        elif sign == '+/-':
            if strs != 'Divisor CANNOT be Zero':
                if eval(strs) != 0:
                    res = eval('-' + strs)
                else:
                    res = strs
            else:
                res = strs
        elif sign == 'C':
            self.numlist.clear()
            res = 0
        elif sign == 'CE':
            res = 0
        elif sign == '¡û':
            if strs != 'Divisor CANNOT be Zero':
                if strs != '0':
                    if len(strs) != 1:
                        res = strs[0:-1]
                    else:
                        res = '0'
                    if self.isequalsign == 1:
                        res = strs
                else:
                    res = '0'
            else:
                res = strs

        self.specialsign = 1
        self.value1.set(res)

    # Function of pressing the equal button
    def presseq(self,signeq):
        oldnum = self.value1.get()
        if self.isequalsign == 1:
            self.value1.set(oldnum)
            self.isequalsign = 0
        elif self.specialsign == 1:
            self.value1.set(oldnum)
            self.specialsign = 0
        elif self.numlist == []:
            self.value1.set(oldnum)
        else:
            if oldnum == 'Divisor CANNOT be Zero':
                self.value1.set(oldnum)
            else:
                if self.numlist[-1] == '/' and eval(oldnum) == 0:
                    self.value1.set('Divisor CANNOT be Zero')
                    self.numlist.clear()
                else:
                    self.numlist.append(oldnum)
                    expression = ''.join(self.numlist)
                    result = eval(expression)
                    express = expression + "=" + str(result)
                    self.value1.set(express)
                    self.numlist.clear()
        self.isequalsign = 1

js = calculator()
