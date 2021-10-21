
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as mb
from tkinter import filedialog

root=0

class Student(object):

    student_code = None
    FIO = None
    adres = None
    telefon = None
    sex = False
    data_birthday = None
    student_class = None

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def insert(self, table):
        table.insert('', 'end', text=self.student_code,
            values=(
                self.FIO,
                self.adres,
                self.telefon,
                'мужской' if self.sex else 'женский',
                self.data_birthday,
                self.student_class
             )
         )

    def search_class(self, table, st_class):
        if self.student_class==st_class:
            self.insert(table)

    def save(self):
        s1 = '_'.join(self.student_code.split())
        s2 = '_'.join(self.FIO.split())
        s3 = '_'.join(self.adres.split())
        s4 = '_'.join(self.telefon.split())
        s5 = '_'.join(self.data_birthday.split())
        s6 = '_'.join(self.student_class.split())
        return '{0} {1} {2} {3} {4} {5} {6}\n'.format(s1, s2, s3,  s4,
                                            'мужской' if self.sex else 'женский', s5, s6)
class MainFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.students = []
        self.file_name = ""
        
        self.initUI()
        self.bindEvents()

    def initUI(self):
        self.parent.title("Ученики")
        self.pack(fill=BOTH, expand=True)

        self.frame_add_1 = Frame(self)
        self.frame_add_1.pack(fill=X)

        student_code_label = Label(self.frame_add_1, text="Код")
        student_code_label.pack()

        self.student_code_entry = Entry(self.frame_add_1)
        self.student_code_entry.pack()

        FIO_label = Label(self.frame_add_1, text="ФИО")
        FIO_label.pack()

        self.FIO_entry = Entry(self.frame_add_1)
        self.FIO_entry.pack()

        adres_label = Label(self.frame_add_1, text="Адрес")
        adres_label.pack()

        self.adres_entry = Entry(self.frame_add_1)
        self.adres_entry.pack()

        telefon_label = Label(self.frame_add_1, text="Телефон")
        telefon_label.pack()

        self.telefon_entry = Entry(self.frame_add_1)
        self.telefon_entry.pack()
        
        
        data_birthday_label = Label(self.frame_add_1, text="Дата рождения")
        data_birthday_label.pack()

        self.data_birthday_entry = Entry(self.frame_add_1)
        self.data_birthday_entry.pack()

        student_class_label = Label(self.frame_add_1, text="Класс")
        student_class_label.pack()

        self.student_class_entry = Entry(self.frame_add_1)
        self.student_class_entry.pack()
        
        self.frame_add_2 = Frame(self)
        self.frame_add_2.pack(fill=X)

        self.var = IntVar()
        self.var.set(0)
        self.male = Radiobutton(self.frame_add_2, text="Мужской",
                          variable=self.var, value=1)
        self.female = Radiobutton(self.frame_add_2, text="Женский",
                            variable=self.var, value=0)
        self.male.pack()
        self.female.pack()

        self.btn_add = Button(self.frame_add_2, text="Добавить", width=15)
        self.btn_add.pack()

        self.frame_remove = Frame(self)
        self.frame_remove.pack(fill=X)

        lbl_remove = Label(self.frame_remove, text="Код", width=8)
        lbl_remove.pack(padx=5, pady=5)

        self.entry_remove = Entry(self.frame_remove, width=15)
        self.entry_remove.pack(padx=5)

        self.btn_remove = Button(self.frame_remove, text="Удалить", width=15)
        self.btn_remove.pack(padx=5, pady=5)

        self.frame_table = Frame(self)
        self.frame_table.pack(fill=X)

        self.table = Treeview(self.frame_table)

        self.table["columns"] = ("1", "2", "3", "4", "5", "6")

        self.table.column("#0", width=80, minwidth=50)
        self.table.column("1", width=80, minwidth=50)
        self.table.column("2", width=80, minwidth=50)
        self.table.column("3", width=80, minwidth=50)
        self.table.column("4", width=80, minwidth=50)
        self.table.column("5", width=80, minwidth=50)
        self.table.column("6", width=80, minwidth=50)
        
        self.table.heading("#0", text="Код", anchor=W)
        self.table.heading("1", text="ФИО", anchor=W)
        self.table.heading("2", text="Адрес", anchor=W)
        self.table.heading("3", text="Телефон", anchor=W)
        self.table.heading("4", text="Пол", anchor=W)
        self.table.heading("5", text="Дата рождения", anchor=W)
        self.table.heading("6", text="Класс", anchor=W)

        self.table.pack(side=TOP, fill=X)


        self.frame_table_search = Frame(self)
        self.frame_table_search.pack(fill=X)

        lbl_serch = Label(self.frame_table_search, text="Класс", width=8)
        lbl_serch.pack(side=TOP, padx=5, pady=5)

        self.entry_search = Entry(self.frame_table_search, width=15)
        self.entry_search.pack(side=TOP, padx=5)

        self.btn_search = Button(self.frame_table_search, text="Поиск", width=15)
        self.btn_search.pack(side=TOP, padx=5, pady=5)
        
        self.table_search = Treeview(self.frame_table_search)

        self.table_search["columns"] = ("1", "2", "3", "4", "5", "6")

        self.table_search.column("#0", width=80, minwidth=50)
        self.table_search.column("1", width=80, minwidth=50)
        self.table_search.column("2", width=80, minwidth=50)
        self.table_search.column("3", width=80, minwidth=50)
        self.table_search.column("4", width=80, minwidth=50)
        self.table_search.column("5", width=80, minwidth=50)
        self.table_search.column("6", width=80, minwidth=50)
        
        self.table_search.heading("#0", text="Код", anchor=W)
        self.table_search.heading("1", text="ФИО", anchor=W)
        self.table_search.heading("2", text="Адрес", anchor=W)
        self.table_search.heading("3", text="Телефон", anchor=W)
        self.table_search.heading("4", text="Пол", anchor=W)
        self.table_search.heading("5", text="Дата рождения", anchor=W)
        self.table_search.heading("6", text="Класс", anchor=W)

        self.table_search.pack(side=BOTTOM, fill=X)
        
        self.main_frame = Frame(self)
        self.main_frame.pack(fill=X)

        self.v = StringVar()
        self.v.trace('w', self.on_combo_change)

        self.combo = Combobox(self.main_frame, state='readonly', width=50, textvar=self.v)
        self.combo['values'] = ("Добавить ученика", "Удалить ученика (по коду)", "Вывести всех учеников", "Вывести учеников указанного класса")
        self.combo.current(0)
        self.combo.pack(side=BOTTOM, padx=5, pady=5)


        self.mainmenu = Menu(self.parent)

        self.parent.config(menu=self.mainmenu)

        self.filemenu = Menu(self.mainmenu, tearoff=0)
        self.filemenu.add_command(label="Создать", command=self.create)
        self.filemenu.add_command(label="Открыть", command=self.download_file)
        self.filemenu.add_command(label="Сохранить", state=DISABLED, command=self.save_file)
        self.filemenu.add_command(label="Сохранить как", command=self.save_as_file)
        self.filemenu.add_command(label="Выход", command=self.ask_exit)

        self.mainmenu.add_cascade(label="Файл", menu=self.filemenu)
        self.mainmenu.add_command(label='Справка', command=self.description)
        
    def hide(self):
        self.frame_add_1.pack_forget()
        self.frame_add_2.pack_forget()
        self.frame_remove.pack_forget()
        self.frame_table.pack_forget()
        self.frame_table_search.pack_forget()
        
    def on_combo_change(self, index, value, op):
        self.hide()
        current_state = self.combo.get()
        if current_state == "Добавить ученика":
            self.frame_add_1.pack(fill=X)
            self.frame_add_2.pack(fill=X)

        elif current_state == "Удалить ученика (по коду)":
            self.frame_remove.pack(fill=X)

        elif current_state == "Вывести всех учеников":
            self.frame_table.pack(fill=X)
            self.get_students()
        else:
            self.frame_table_search.pack(fill=X)   

    def bindEvents(self):
        self.btn_add.bind('<Button-1>', self.add_new_student)
        self.btn_remove.bind('<Button-1>', self.delete_student)
        self.btn_search.bind('<Button-1>', self.get_students_class)

    def add_new_student(self, event):
        code = self.student_code_entry.get()
        name = self.FIO_entry.get()
        adres = self.adres_entry.get()
        sex = int(self.var.get())
        telefon = self.telefon_entry.get()
        birthday = self.data_birthday_entry.get()
        _class = self.student_class_entry.get()

        if len(code) == 0 or len(name) == 0 or len(adres) == 0 or len(telefon) == 0 or len(birthday) == 0 or len(_class) == 0: 
            mb.showerror("Ошибка", "Все поля должны быть заполнены!")
            return


        self.students.append(Student(
            student_code=code,
            FIO=name,
            adres=adres,
            sex=sex,
            telefon=telefon,
            data_birthday=birthday,
            student_class=_class)
        )
        self.clear_text()
        mb.showinfo("Успешно", "Информация добавлена!")
        if self.file_name:
            self.filemenu.entryconfig(2, state=NORMAL)

    def get_students(self):
        self.table.delete(*self.table.get_children())

        for item in self.students:
            item.insert(self.table)

    def get_students_class(self, event):
        serch_class = self.entry_search.get()
        self.table_search.delete(*self.table_search.get_children())

        if len(serch_class) == 0:
            mb.showerror("Ошибка", "Заполните поле!")
            return
        
        for item in self.students:
            item.search_class(self.table_search,serch_class)
        
    def clear_text(self):
        self.student_code_entry.delete(0, 'end')
        self.FIO_entry.delete(0, 'end')
        self.adres_entry.delete(0, 'end')
        self.var.set(0)
        self.telefon_entry.delete(0, 'end')
        self.data_birthday_entry.delete(0, 'end')
        self.student_class_entry.delete(0, 'end')
        
    def delete_student(self, event):
        code = self.entry_remove.get()

        if len(code) == 0:
            mb.showerror("Ошибка", "Заполните поле!")
            return

        self.students = [item for item in self.students if item.student_code != code]
        self.clear_text()
        mb.showinfo("Успешно", "Удалено!")
        self.filemenu.entryconfig(2, state=NORMAL)
        
    def create(self):
        self.ask_save()
        self.file_name = ""
        self.clear_text()
        self.students.clear()
        self.table.delete(*self.table.get_children())
        self.combo.current(0)
        self.filemenu.entryconfig(2, state=DISABLED)
        
    def download_file(self):
        self.ask_save()

        self.table.delete(*self.table.get_children())
        self.students.clear()

        self.file_name = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

        with open(self.file_name, "r", encoding='utf-8') as f:
            f.seek(0)
            for line in f:
                info = line.split()
                self.students.append(Student(
                    student_code=info[0].replace("_", " "),
                    FIO=info[1].replace("_", " "),
                    adres=info[2].replace("_", " "),
                    telefon=info[3].replace("_", " "),
                    sex=True if info[4] == 'мужской' else False,
                    data_birthday=info[5].replace("_", " "),
                    student_class=info[6].replace("_", " "))
                )

        self.combo.current(2)

    def save_file(self):
        with open(self.file_name, "w", encoding='utf-8') as f:
            f.seek(0)
            for item in self.students:
                f.write(item.save())

        mb.showinfo("Успешно", "Информация сохранена!")
        self.filemenu.entryconfig(2, state=DISABLED)

    def save_as_file(self):
        self.file_name = filedialog.asksaveasfilename(defaultextension=".txt")
        if self.file_name:
            self.save_file()

    def ask_save(self):
        answer = mb.askyesno("Сохранить", "Сохранить изменения?")
        if answer == True:
            if len(self.file_name) > 0:
                self.save_file()
            else:
                self.save_as_file()

    def ask_exit(self):
        global root
        self.ask_save()
        answer = mb.askyesno("Выход", "Вы дейстельно хотите выйти?")
        if answer == True:
            self.quit()
            root.destroy()
            
    def description(self):
         mb.showinfo(
            "О программе", 
            "Бессонов Максим, 92ПГ")
        
def main():
    global root
    root = Tk()
    root.geometry("1000x400")
    app = MainFrame(root)
    root.mainloop()


if __name__ == '__main__':
    main()
