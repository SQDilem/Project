#импорт неообходимых библиатек 
import tkinter as tk
from tkinter import ttk 
import sqlite3 
import tkinter 

#главное окно
class Main(tk.Frame): 
    def __init__(self, root): 
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_information()
    
    #Виджеты
    def init_main(self): 
        tollbar = tk.Frame(bg='#d7d7d7', bd = 2) 
        tollbar.pack(side=tk.TOP, fill = tk.X)
        
        #Кнопка добавления сотрудника
        self.img_add = tk.PhotoImage(file = './icons/add.png')
        btn_add = tk.Button(tollbar, text = 'Добавить сотрудника', bg = '#d7d8e0', bd = 0, 
                            image = self.img_add, command = self.open_dialog)
        btn_add.pack (side = tk.LEFT) 
        
        #Кнопка изменения инфорамации о сотруднике
        self.img_upd = tk.PhotoImage(file = './icons/change.png')
        btn_upd = tk.Button(tollbar, bg = '#d7d8e0', bd = 0, image = self.img_upd, command = self.open_update_worker)
        btn_upd.pack (side = tk.LEFT) 
        
        #Кнопка удаления сотрудника 
        self.img_del = tk.PhotoImage(file = './icons/delete.png')
        btn_del = tk.Button(tollbar, bg = '#d7d8e0', bd = 0, image = self.img_del, command = self.delete_information)
        btn_del.pack (side = tk.LEFT) 
        
        #Кнопка обновления информации 
        self.img_refresh = tk.PhotoImage(file = './icons/refresh.png')
        bth_ref = tk.Button(tollbar, bg = '#d7d8e0', bd = 0, image = self.img_refresh, 
                            command = self.view_information)
        bth_ref.pack (side = tk.LEFT)
        
        #Кнопка поиска сотрудника
        self.img_search = tk.PhotoImage(file = './icons/search.png')
        bth_search = tk.Button (tollbar, bg = '#d7d8e0', bd = 0, image = self.img_search, command = self.open_search)
        bth_search.pack(side = tk.LEFT)
        
        #Таблица сотрудников
        self.tree = ttk.Treeview(self,  
                                 columns = ('id', 'name', 'phone', 'email', 'salary'),
                                 height = 17,
                                 show = 'headings') 
        self.tree.column('id', width = 45, anchor = tk.CENTER)
        self.tree.column('name', width = 250, anchor = tk.CENTER)
        self.tree.column('phone', width = 100, anchor = tk.CENTER)
        self.tree.column('email', width = 150, anchor = tk.CENTER)
        self.tree.column('salary', width = 100, anchor = tk.CENTER)
        
        self.tree.heading('id', text = 'id')
        self.tree.heading('name', text = 'ФИО')
        self.tree.heading('phone', text = 'Телефон')
        self.tree.heading('email', text = 'Email')
        self.tree.heading('salary', text = 'Зарплата')
        
        self.tree.pack(side = tk.LEFT)
        
        #Скроллбар 
        scroll = tk.Scrollbar(self, command = self.tree.yview)
        scroll.pack(side = tk.LEFT, fill = tk.Y)
        self.tree.configure(yscrollcommand = scroll.set)
        
    # Добавление данных 
    def infomation(self, name, phone, email, salary):
        self.db.insert_data(name, phone, email,salary )                                 =
        self.view_information() 
    
    # отображение в treeview
    def view_information(self): 
        self.db.cur.execute('SELECT * FROM users')
        [self.tree.delete[i] for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values = i) for i in self.db.cur.fetchall()] 
    
    # метод поиска сотрудников
    def search_information(self, name):
        self.db.cur.execute('SELECT * FROM users WHERE name  LIKE ?', 
                            ('%' + name + '%',))
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values = i) for i in self.db.cur.fetchall()]
        
    # метод изменения данных о сотрудниках
    def update_information(self, name, phone, email, salary):
        self.db.cur.execute(                                                       
            """UPDATE Employees SET name=?, phone=?, email=?, salary=? WHERE id=?""",
            (name, phone, email,salary, self.tree.set(self.tree.selection()[0], "#1")),
        )
        self.db.conn.commit()
        self.view_information()
        
    # метод удаления данных о сотрудниках
    def delete_information(self): 
        for row in self.tree.selection(): 
            self.db.cur.execute('DELETE FROM users WHERE id = ?', 
                                (self.tree.set(row, '#1'),))
            self.db.conn.commit()
            self.view_information()
    
    # вызов дочернего окна
    def open_dialog(self):                                                           
        Child()      
    
    # дочернее для редактированния данных
    def open_update_worker(self): 
        Update()
    
    # дочернее для поиска данных     
    def open_search(self):
        Search()
    
class Child(tk.Toplevel):
    def __init__(self): 
        super().__init__(root)
        self.init_worker()
        self.view = app
    
    #инциализация виджетов 
    def init_worker(self): 
        self.title('Добавление сотрудника')
        self.geometry('400x200')
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()
        
        label_name = tk.Label(self, text = 'ФИО')
        label_name.place(x = 50, y = 50)
        label_phone = tk.Label(self, text = 'Телефон')
        label_phone.place(x = 50, y = 50)
        label_email = tk.Label(self, text = 'Email')
        label_email.place(x = 50, y = 50)
        label_salary = tk.Label(self, text = 'Зарплата')
        label_salary.place(x = 50, y = 50)
        
        self.entry_name = tk.Entry(self) 
        self.entry_name.place(x = 200, y = 50)
        self.entry_phone = tk.Entry(self) 
        self.entry_phone.place(x = 200, y = 50)
        self.entry_email = tk.Entry(self) 
        self.entry_email.place(x = 200, y = 50)
        self.entry_salary = tk.Entry(self) 
        self.entry_salary.place(x = 200, y = 50)
        
        btn_cancel = tk.Button(self, text = 'Закрыть', command = self.destroy)
        btn_cancel.place (x = 200, y = 150)
        
        self.bth_add = tk.Button(self, text = 'Добавить')
        self.bth_add.bind ('<Button-1>', lambda event: self.view.infomation(self.entry_name.get(),
                                                                         self.entry_email.get(), 
                                                                         self.entry_phone.get(), 
                                                                         self.entry_salary.get()))
        self.bth_add.place(x = 265, y = 150)
          
class Update(Child):      
    def __init__(self):                                            
        super().__init__()                                         
        self.init_edit()                                           
        self.view = app                                              
        self.db = db                                                
        self.default_data()                                      

    #Метод редактирования данных в бд
    def init_edit(self):
        self.title("Редактирование данных сотрудника")              
        btn_edit = ttk.Button(self, text="Редактировать")           
        btn_edit.place(x=205, y=170)                                 
        btn_edit.bind(
            "<Button-1>",
            lambda event: self.view.update_information(
                self.entry_name.get(), self.entry_email.get(), self.entry_phone.get(), self.entry_salary.get()
            ),
        )
        
        btn_edit.bind(
            "<Button-1>",
            lambda event: self.destroy(), add="+"
        )

        self.bth_add.destroy()                                          

    def default_data(self):
        self.db.cur.execute(                                           
            "SELECT * FROM Employees WHERE id=?",
            self.view.tree.set(self.view.tree.selection()[0], "#1"),        
        )
        row = self.db.cur.fetchone()                        
        self.entry_name.insert(0, row[1])                       
        self.entry_email.insert(0, row[2])                    
        self.entry_phone.insert(0, row[3])                       
        self.entry_salary.insert(0,row[4])



class Search(tk.Toplevel):
    def __init__(self):                               
        super().__init__()                                     
        self.init_search()                                     
        self.view = app                                     

    def init_search(self):
        self.title("Поиск сотрудника")                     
        self.geometry("300x100")                               
        self.resizable(False, False)                           

        label_search = tk.Label(self, text="Имя:")            
        label_search.place(x=50, y=20)                        

        self.entry_search = ttk.Entry(self)                     
        self.entry_search.place(x=100, y=20, width=150)         


        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)


        search_btn = ttk.Button(self, text="Найти")
        search_btn.place(x=105, y=50)

        search_btn.bind(
            "<Button-1>",
            lambda event: self.view.search_records(self.entry_search.get()),
        )
        search_btn.bind("<Button-1>", lambda event: self.destroy(), add="+")


# класс Db 
class Db: 
    def __init__(self): 
        self.conn = sqlite3.connect('contacts.db')
        self.cur = self.conn.cursor() 
        self.cur.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY, 
                        name TEXT,
                        phone TEXT,
                        email TEXT,  
                        salary INTEGER)
                         ''')
    
    #Добавление данных в db 
    def insert_data(self, name, phone, email, salary): 
        self.cur.execute('''
                         INSERT INTO users (name, phone, email, salary)
                         VALUES (?,?,?,?)''', (name , phone, email, salary))
             
#Запуск
if __name__ == "__main__":
    root = tk.Tk()                                  
    db = Db()                                       
    app = Main(root)                                
    app.pack()                                      
    root.title("Список сотрудников компании")       
    root.geometry("765x450")                        
    root.resizable(False, False)                    
    root.mainloop()      













