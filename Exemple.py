from rpn.converter import Converter
from rpn.evaluetor import Actions
from rpn.rpn import Rpn
from rpn.checkers import Checkers
from rpn.helpers import Operators
import tkinter as tk
from tkinter import W, E
from tkinter.ttk import Frame, Button, Entry, Style

class Exemple(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("RPN")

        Style().configure("TButton", padding=(0, 6, 0, 6),
                          font='serif 10')

        self.columnconfigure(0, pad=0)
        self.columnconfigure(1, pad=0)
        self.columnconfigure(2, pad=0)
        self.columnconfigure(3, pad=0)

        self.rowconfigure(0, pad=0)
        self.rowconfigure(1, pad=0)
        self.rowconfigure(2, pad=0)
        self.rowconfigure(3, pad=0)
        self.rowconfigure(4, pad=0)
        self.rowconfigure(5, pad=0)

        self.var = tk.StringVar()
        self.entry = Entry(self, textvariable=self.var, justif="right")
        self.data_from_entry = self.entry.get()
        self.entry.grid(row=0, columnspan=4, sticky=W + E)

        lp = Button(self, text="(", command=self.in_entry_lp)
        lp.grid(row=1,columnspan=2,sticky=W + E)

        rp = Button(self, text=")", command=self.in_entry_rp)
        rp.grid(row=1,column=2, columnspan=2, sticky=W + E)

        cls = Button(self, text="Cls")
        cls.grid(row=2, column=0)
        bck = Button(self, text="Back")
        bck.grid(row=2, column=1)
        pob = Button(self, text="^", command=self.in_entry_pow)
        pob.grid(row=2, column=2)
        clo = Button(self, text="Close", command=self.quit)
        clo.grid(row=2, column=3)
        sev = Button(self, text="7", command=self.in_entry_sev)
        sev.grid(row=3, column=0)
        eig = Button(self, text="8", command=self.in_entry_eight)
        eig.grid(row=3, column=1)
        nin = Button(self, text="9", command=self.in_entry_night)
        nin.grid(row=3, column=2)
        div = Button(self, text="/", command=self.in_entry_div)
        div.grid(row=3, column=3)

        fou = Button(self, text="4", command=self.in_entry_four)
        fou.grid(row=4, column=0)
        fiv = Button(self, text="5", command=self.in_entry_five)
        fiv.grid(row=4, column=1)
        six = Button(self, text="6", command=self.in_entry_six)
        six.grid(row=4, column=2)
        mul = Button(self, text="*", command=self.in_entry_mul)
        mul.grid(row=4, column=3)

        one = Button(self, text="1", command=self.in_entry_one)
        one.grid(row=5, column=0)
        two = Button(self, text="2", command=self.in_entry_two)
        two.grid(row=5, column=1)
        thr = Button(self, text="3", command=self.in_entry_tree)
        thr.grid(row=5, column=2)
        mns = Button(self, text="-", command=self.in_entry_minus)
        mns.grid(row=5, column=3)

        zer = Button(self, text="0", command=self.in_entry_zero)
        zer.grid(row=6, column=0)
        dot = Button(self, text=".", command=self.in_entry_dot)
        dot.grid(row=6, column=1)
        equ = Button(self, text="=", command=self.result_is)
        equ.grid(row=6, column=2)
        pls = Button(self, text="+", command=self.in_entry_plus)
        pls.grid(row=6, column=3)

        self.pack()

    def in_entry_zero(self):
        self.data_from_entry += "0"
        self.var.set(self.data_from_entry)

    def in_entry_one(self):
        self.data_from_entry += "1"
        self.var.set(self.data_from_entry)

    def in_entry_two(self):
        self.data_from_entry += "2"
        self.var.set(self.data_from_entry)

    def in_entry_tree(self):
        self.data_from_entry += "3"
        self.var.set(self.data_from_entry)

    def in_entry_four(self):
        self.data_from_entry += "4"
        self.var.set(self.data_from_entry)

    def in_entry_five(self):
        self.data_from_entry += "5"
        self.var.set(self.data_from_entry)

    def in_entry_six(self):
        self.data_from_entry += "6"
        self.var.set(self.data_from_entry)

    def in_entry_sev(self):
        self.data_from_entry += "7"
        self.var.set(self.data_from_entry)

    def in_entry_eight(self):
        self.data_from_entry += "8"
        self.var.set(self.data_from_entry)

    def in_entry_night(self):
        self.data_from_entry += '9'
        self.var.set(self.data_from_entry)

    def in_entry_plus(self):
        self.data_from_entry += '+'
        self.var.set(self.data_from_entry)

    def in_entry_minus(self):
        self.data_from_entry += '-'
        self.var.set(self.data_from_entry)

    def in_entry_div(self):
        self.data_from_entry += '/'
        self.var.set(self.data_from_entry)

    def in_entry_mul(self):
        self.data_from_entry += '*'
        self.var.set(self.data_from_entry)

    def in_entry_dot(self):
        self.data_from_entry += '.'
        self.var.set(self.data_from_entry)

    def in_entry_pow(self):
        self.data_from_entry += '^'
        self.var.set(self.data_from_entry)

    def in_entry_rp(self):
        self.data_from_entry += ')'
        self.var.set(self.data_from_entry)

    def in_entry_lp(self):
        self.data_from_entry += '('
        self.var.set(self.data_from_entry)

    def result_is(self):
        res = Rpn.rpn(self.data_from_entry, Converter.toPostfix, Actions.postixEval, Checkers.check_pr)

        if res:
            self.data_from_entry = str(res)
            self.var.set(self.data_from_entry)
            print(res)
        else:
            self.data_from_entry = "error"
            self.var.set(self.data_from_entry)
