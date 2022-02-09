import tkinter as tk

win = tk.Tk()
win.geometry(f"510x350")
win.rowconfigure(0, minsize=400, weight=1)
win.columnconfigure(1, minsize=400, weight=1)
win.title('Банковские терминалы')



class window1(tk.Toplevel):
    def __init__(self):
        super(window1, self).__init__()
        self.title('Свойства')
        self.geometry(f"510x350")
        self.ramka2 = tk.Frame(self, background="bisque2")
        self.ramka2.place(width=210, height=350)
        self.ramka3 = tk.Frame(self, background="bisque4")
        self.ramka3.place(width=300, height=350, x=210, y=0)
        self.grid_rowconfigure(0, minsize=100)
        self.grid_columnconfigure(1, minsize=100)
        self.btn1 = tk.Button(self, text="Список терминалов", command=self.deistvie)
        self.btn1.place(width=167, height=26, x=20, y=40)



    def deistvie(self):
        self.btn1 = tk.Button(self, text="Улица Ленина, д.94")
        self.btn1.grid(row=1, column=1, padx=20, pady=10, stick='we')
        self.label1 = tk.Label(self, text='Статус работы: исправен',background="bisque4")
        self.label1.place(x=250, y=112)
        self.labe12 = tk.Label(self, text='Статус работы: исправен',background="bisque4")
        self.labe12.place(x=250, y=158)
        self.label3 = tk.Label(self, text='Статус работы: исправен',background="bisque4")
        self.label3.place(x=250, y=204)
        self.labe14 = tk.Label(self, text='Статус работы: исправен',background="bisque4")
        self.labe14.place(x=250, y=250)
        self.labe15 = tk.Label(self, text='Для получения информации о банковских\n устройствах нажмине на знак "?"',background="bisque4")
        self.labe15.place(x=250, y=37)
        self.btn2 = tk.Button(self, text="?", command = window2)
        self.btn2.place(x=430, y=112, width=26, height=26)
        self.btn3 = tk.Button(self, text="?", command=window3)
        self.btn3.place(x=430, y=158, width=26, height=26)
        self.btn4 = tk.Button(self, text="?", command=window4)
        self.btn4.place(x=430, y=204, width=26, height=26)
        self.btn5 = tk.Button(self, text="?", command=window5)
        self.btn5.place(x=430, y=250, width=26, height=26)
        self.btn6 = tk.Button(self, text="Техническая поддержка", command=TP)
        self.btn6.place(x=313, y=300)
        self.btn7 = tk.Button(self, text="Улица Луначарского, д.78")
        self.btn7.grid(row=2, column=1, padx=20, pady=10, stick='we')
        self.btn8 = tk.Button(self, text="Улица Титова, д.9")
        self.btn8.grid(row=3, column=1, padx=20, pady=10, stick='we')
        self.btn9 = tk.Button(self, text="Улица Пр.Космонавтов, д.56")
        self.btn9.grid(row=4, column=1, padx=20, pady=10, stick='we')


class window2(tk.Toplevel):
        def __init__(self):
            super(window2, self).__init__()
            self.title('Улица Ленина, д.94')
            self.geometry(f"510x350")
            self.photo = tk.PhotoImage(file=r"C:\Kursach\Lenina.png")
            self.grid_rowconfigure(0, minsize=100)
            self.grid_columnconfigure(1, minsize=100)
            self.ramka13 = tk.Frame(self, background="bisque2")
            self.ramka13.place(width=210, height=350)
            self.ramka14 = tk.Frame(self, background="bisque4")
            self.ramka14.place(width=300, height=350, x=210, y=0)
            self.labe16 = tk.Label(self, text='Серийный номер: ААБ942ВВВ3245\n Адрес: г.Новоуральск, ул. Ленина'
                                              ', д.94\n Ответственный: Петрухно А.А.\n Техническое обеспечение: '
                                              'Группа Б-1\n По вопросам обслуживания обращаться: Петрухно А.А',
                                   background="bisque4", font=('TimesNewRoman', 14), justify='left')
            self.labe16.grid(row=1, column=0, stick='e')
            self.btnTP = tk.Button(self, text='Закрыть', command=self.destroy)
            self.btnTP.place(x=280, y=275, width=167, height=26)




class window3(tk.Toplevel):
    def __init__(self):
        super(window3, self).__init__()
        self.title("Улица Луначарского, д.78")
        self.geometry(f"510x350")
        self.grid_rowconfigure(0, minsize=100)
        self.grid_columnconfigure(1, minsize=100)
        self.ramka11 = tk.Frame(self, background="bisque2")
        self.ramka11.place(width=210, height=350)
        self.ramka12 = tk.Frame(self, background="bisque4")
        self.ramka12.place(width=300, height=350, x = 210, y = 0)
        self.labe16 = tk.Label(self, text='Серийный номер: ААА234КЛММ93\n Адрес: г.Екатеринбург, ул. Луначарского'
                                          ', д.78\n Ответственный: Петрухно А.А.\n Техническое обеспечение: '
                                          'Группа Б-2\n По вопросам обслуживания обращаться: Петрухно А.А',
                               background="bisque4", font=('TimesNewRoman', 14), justify='left')
        self.labe16.grid(row=1, column=0, stick = 'e')
        self.btnTP = tk.Button(self, text='Закрыть', command=self.destroy)
        self.btnTP.place(x=280, y=275, width=167, height=26)



class window4(tk.Toplevel):
    def __init__(self):
        super(window4, self).__init__()
        self.title('Улица Титова д.9')
        self.geometry(f"510x350")
        self.photo = tk.PhotoImage(file=r"C:\Kursach\Lenina.png")
        self.grid_rowconfigure(0, minsize=100)
        self.grid_columnconfigure(1, minsize=100)
        self.ramka7 = tk.Frame(self, background="bisque2")
        self.ramka7.place(width=210, height=350)
        self.ramka8 = tk.Frame(self, background="bisque4")
        self.ramka8.place(width=300, height=350, x=210, y=0)
        self.labe16 = tk.Label(self, text='Серийный номер: ААА5478Б3ВА\n Адрес: г.Екатеринбург, ул. Титова'
                                          ', д.9\n Ответственный: Петрухно А.А.\n Техническое обеспечение: '
                                          'Группа Б-3\n По вопросам обслуживания обращаться: Петрухно А.А',
                               background="bisque4", font=('TimesNewRoman', 14), justify='left')
        self.labe16.grid(row=1, column=0, stick='e')
        self.btnTP = tk.Button(self, text='Закрыть', command=self.destroy)
        self.btnTP.place(x=280, y=275, width=167, height=26)



class window5(tk.Toplevel):
    def __init__(self):
        super(window5, self).__init__()
        self.title("Улица Пр.Космонавтов, д.56")
        self.geometry(f"510x350")
        self.grid_rowconfigure(0, minsize=100)
        self.grid_columnconfigure(1, minsize=100)
        self.ramka9 = tk.Frame(self, background="bisque2")
        self.ramka9.place(width=210, height=350)
        self.ramka10 = tk.Frame(self, background="bisque4")
        self.ramka10.place(width=300, height=350, x=210, y=0)
        self.labe16 = tk.Label(self, text='Серийный номер: АААП942БУ32\n Адрес: г.Екатеринбург, ул. Пр.Космонавтов'
                                          ', д.56\n Ответственный: Петрухно А.А.\n Техническое обеспечение: '
                                          'Группа Б-4\n По вопросам обслуживания обращаться: Петрухно А.А',
                               background="bisque4", font=('TimesNewRoman', 14), justify='left')
        self.labe16.grid(row=1, column=0, stick='e')
        self.btnTP = tk.Button(self, text='Закрыть', command=self.destroy)
        self.btnTP.place(x=280, y=275, width=167, height=26)



class TP(tk.Toplevel):
    def __init__(self):
        super(TP, self).__init__()
        self.title("Техническая поддержка")
        self.geometry(f"510x350")
        self.grid_rowconfigure(0, minsize=200)
        self.grid_columnconfigure(1, minsize=200)
        self.ramka5 = tk.Frame(self, background="bisque2")
        self.ramka5.place(width=210, height=350)
        self.ramka6 = tk.Frame(self, background="bisque4")
        self.ramka6.place(width=300, height=350, x = 210, y = 0)
        self.btnTP = tk.Button(self, text='Отправить', command=self.destroy)
        self.btnTP.place(x=375, y=275)
        self.labelTP = tk.Label(self, text='Кратко опишите проблему:', background="bisque2")
        self.labelTP.grid(row=0, column=0, padx=10, pady=10, sticky='n')
        self.textTP = tk.Text(self, font=("TimesNewRoman", 14, "italic"))
        self.textTP.place(x=50, y=50, width=400, height=200)





ramka = tk.Frame(win, background="bisque2")

ramka4 = tk.Frame(win, background="bisque4")
ramka4.place(width=300, height=350, x = 210, y = 0)



btn1 = tk.Button(ramka, text='Главная')
btn1.place(width=167, height=26, x=20, y=20)
btn2 = tk.Button(ramka, text='Свойства', command=window1)
btn2.place(width=167, height=26, x=20, y=70)



ramka.place(width=210, height=350)

win.grid_columnconfigure(0, minsize=100)
win.mainloop()
