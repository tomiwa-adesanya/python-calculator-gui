from tkinter import ttk
import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        #--------------------------------------------------------------
        #           ROOT WINDOW ATTRIBUTES CONFIGURATION
        #--------------------------------------------------------------
        self.title("Calculator")
        self.geometry("345x500")
        self.resizable(False, False)
        self.attributes("-alpha", 0.90) # Sets level of transparency to 0.10
        self.bind("<Control-KeyPress-w>", lambda event=None: self.destroy(), add="+") # Exits calculator when user presses Ctrl+w
        self.bind("<Control-KeyPress-W>", lambda event=None: self.destroy(), add="+") # Exits calculator when user presses Ctrl+W


        #---------------------------------------------------------------
        #               GRID LAYOUT CONFIGURATION
        #---------------------------------------------------------------
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)
        self.columnconfigure(index=2, weight=1)


        #---------------------------------------------------------------
        self.build_wigets()
        self.run()

    def build_wigets(self):
        """
        Creates and places all required GUI components within the root window
        """

        #---------------------------------------------------------------
        #               NEW THEMED WIDGET CLASSES
        #---------------------------------------------------------------
        Button = ttk.Button
        Entry = ttk.Entry
        Label = ttk.Label

        #---------------------------------------------------------------
        #                   DEFAULT CONFIGURATIONS
        #---------------------------------------------------------------
        widget_attr = {
            "font" : ("Helvetica", 14)
        }
        btn_ipad = {
            "ipadx" : 17.5, "ipady" : 19.5,
        }
        btn_pad = {
            "padx" : 1.5, "pady" : 1.5,
        }

        #---------------------------------------------------------------
        #                           ENTRY
        #---------------------------------------------------------------
        entry_var = tk.StringVar()
        entry = Entry(self, textvariable=entry_var, width=35, **widget_attr)
        entry.bind(
            "<Return>", lambda event=None: entry_var.set(self.evaluate(entry_var.get())), add="+"
        )
        entry.focus() # Sets typing cursor to entry when window is created
        entry.grid(
            column=0, row=0,
            columnspan=3,
            ipadx=15, ipady=23.5,
            padx=1.5, pady=1.5,
            sticky="nw"
        )
        

        #-----------------------------------------------------------------------------------
        #                            BUTTONS CONFIGURATION
        #-----------------------------------------------------------------------------------

        btn_percent = Button(self, text="%", command=lambda: entry_var.set(entry_var.get() + "% "))
        btn_percent.grid(
            column=0, row=1,
            sticky="nw",
            **btn_pad,
            **btn_ipad
        )

        btn_ce = Button(self, text="CE", command=lambda: entry_var.set(""))
        btn_ce.grid(
            column=1, row=1,
            **btn_ipad
        )

        btn_equals = Button(self, text="=", command=lambda : entry_var.set(self.evaluate(entry_var.get())))
        btn_equals.grid(
            column=2, row=1,
            sticky="ne",
            **btn_pad,
            **btn_ipad
        )

        btn_x = Button(self, text="X", command=lambda: entry_var.set(entry_var.get() + " x "))
        btn_x.grid(
            column=0, row=2,
            sticky="nw",
            **btn_pad,
            **btn_ipad
        )

        btn_div = Button(self, text="/", command=lambda: entry_var.set(entry_var.get() + " / "))
        btn_div.grid(
            column=1, row=2,
            **btn_ipad
        )

        btn_pow = Button(self, text="^", command=lambda: entry_var.set(entry_var.get() + " ^ "))
        btn_pow.grid(
            column=2, row=2,
            sticky="ne",
            **btn_pad,
            **btn_ipad
        )

        btn_7 = Button(self, text="7", command=lambda: entry_var.set(entry_var.get() + "7"))
        btn_7.grid(
            column=0, row=3,
            sticky="nw",
            **btn_pad,
            **btn_ipad
        )

        btn_8 = Button(self, text="8", command=lambda: entry_var.set(entry_var.get() + "8"))
        btn_8.grid(
            column=1, row=3,
            **btn_ipad
        )

        btn_9 = Button(self, text="9", command=lambda: entry_var.set(entry_var.get() + "9"))
        btn_9.grid(
            column=2, row=3,
            sticky="ne",
            **btn_pad,
            **btn_ipad
        )

        btn_4 = Button(self, text="4", command=lambda: entry_var.set(entry_var.get() + "4"))
        btn_4.grid(
            column=0, row=4,
            sticky="nw",
            **btn_pad,
            **btn_ipad
        )

        btn_5 = Button(self, text="5", command=lambda: entry_var.set(entry_var.get() + "5"))
        btn_5.grid(
            column=1, row=4,
            **btn_ipad
        )

        btn_6 = Button(self, text="6", command=lambda: entry_var.set(entry_var.get() + "6"))
        btn_6.grid(
            column=2, row=4,
            sticky="ne",
            **btn_pad,
            **btn_ipad
        )

        btn_1 = Button(self, text="1", command=lambda: entry_var.set(entry_var.get() + "1"))
        btn_1.grid(
            column=0, row=5,
            sticky="nw",
            **btn_pad,
            **btn_ipad
        )

        btn_2 = Button(self, text="2", command=lambda: entry_var.set(entry_var.get() + "2"))
        btn_2.grid(
            column=1, row=5,
            **btn_ipad
        )

        btn_3 = Button(self, text="3", command=lambda: entry_var.set(entry_var.get() + "3"))
        btn_3.grid(
            column=2, row=5, 
            sticky="ne",
            **btn_pad,
            **btn_ipad
        )
        
        btn_plus = Button(self, text="+", command=lambda: entry_var.set(entry_var.get() + " + "))
        btn_plus.grid(
            column=0, row=6,
            sticky="nw",
            **btn_pad,
            **btn_ipad
        )

        btn_0 = Button(self, text="0", command=lambda: entry_var.set(entry_var.get() + "0"))
        btn_0.grid(
            column=1, row=6,
            **btn_ipad
        )

        btn_minus = Button(self, text="-", command=lambda: entry_var.set(entry_var.get() + " - "))
        btn_minus.grid(
            column=2, row=6,
            sticky="ne",
            **btn_pad,
            **btn_ipad
        )

    def evaluate(self, eq):
        """
        Solves equation string input and returns solution
        """
        eq = eq.lower()
        eq = eq.replace("%", "/100") if ("%" in eq) else eq 
        eq = eq.replace("x", "*") if ("x" in eq) else eq

        return eval(eq)
        
    def run(self):
        """
        Runs GUI
        """
        self.mainloop()

Calculator()