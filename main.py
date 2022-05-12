import time
import Tkinter as tk
import tkFont
import tkMessageBox

import myclass
import random
# import Tkinter.ttk as ttk
import ttk

company = myclass.Company()
company.print_data()

DAYS=0
workers_list = []
list = []


def create_order(company):
    names = ['mobile game', 'program', 'game', 'site', 'smart home']
    name = names[random.randint(0, 4)]
    term = random.randint(5, 20)
    rating = company.rating + float(random.randint(-10, 10)) / 10
    paid = 10 * term + term * rating + random.randint(5, 20)
    complexity = company.employees * 3
    relevance = random.randint(7, 23)
    order = myclass.Order(complexity, name, paid, rating, relevance, term)
    return order


def order_list():
    global list
    list = []
    for i in range(10):
        list.append(create_order(company))


def print_order_list():
    print("term | paid | rating")
    for order in list:
        print(str(order.term) + ' | ' + str(order.paid) + ' | ' + str(order.rating))


def create_worker(company):
    names = ['misha', 'katya', 'sasha', 'dasha', 'anton']
    name = names[random.randint(0, 4)]
    ability = float(random.randint(5, 20)) / 10
    salary = 10 * ability + random.randint(-5, 5)
    worker = myclass.Worker(name, ability, salary)
    return worker


def workers():
    global workers_list
    workers_list= []
    for i in range(10):
        workers_list.append(create_worker(company))

    print("name | ability | salary")
    for worker in workers_list:
        print(str(worker.name) + ' | ' + str(worker.ability) + ' | ' + str(worker.salary))


def choose_worker():
    number = input("choose en employee ")
    company.hire(workers_list[number])


def choose_order():
    number = input('choose en order ')
    company.get_order(list[number])

company.hire(create_worker(company))
workers()
order_list()

window = tk.Tk()
window.geometry('1000x1000')
window.title('my game')


name=tk.Label(window ,text='your company', fg='white', bg='#872a2a', pady=5, padx=5)
name.place(x=0, y=0)

days_label=tk.Label(window ,text='day number: ', fg='white', bg='#872a2a', pady=5, padx=5)
days_label.place(x=322, y=0)

rating=tk.Label(window, text="your reting: " + str(company.rating), fg='white', bg='#872a2a', pady=5, padx=5)
rating.place(x=100, y=0)
money=tk.Label(text='your money: ' + str(company.money), fg='white', bg='#872a2a', pady=5, padx=5)
money.place(y=0, x=200)

# worker=tk.Label(window, text=)


# ------------------------------------
# tabel with free workers
columns=('number', 'name', 'money', 'ability')
table=ttk.Treeview(window, show='headings', columns=columns)

table.heading('name', text='Name')
table.heading('money', text='Money')
table.heading('ability', text="Ability")
table.heading('number', text="Num")

table.column('name',width=100, anchor='center')
table.column('money',width=50, anchor='center')
table.column('ability',width=50, anchor='center')
table.column('number',width=30, anchor='center')

table.place(x=10,y=270)

index = 1
for worker in workers_list:
    table.insert('', index=index, values=(str(index), str(worker.name), str(worker.salary), str(worker.ability)))
    index += 1
# end of code tabel with free workers ----------------


# ------------------------------------
# tabel with company workers
columns_company=('number', 'name', 'money', 'ability')
table_company=ttk.Treeview(window, show='headings', columns=columns)

table_company.heading('name', text='Name')
table_company.heading('money', text='Money')
table_company.heading('ability', text="Ability")
table_company.heading('number', text="Num")

table_company.column('name',width=100, anchor='center')
table_company.column('money',width=50, anchor='center')
table_company.column('ability',width=50, anchor='center')
table_company.column('number',width=30, anchor='center')

table_company.place(x=10,y=50)

index = 1
for worker in company.employees_list:
    table_company.insert('', index=index, values=(str(index), str(worker.name), str(worker.salary), str(worker.ability)))
    index += 1
# end of code tabel with free workers ----------------

# ------------------------------------
# tabel with company orders
columns_order=('number', 'complexity', 'name', 'paid', 'rating', 'relevance', 'term')
table_order=ttk.Treeview(window, show='headings', columns=columns_order)

table_order.heading('name', text='Name')
table_order.heading('paid', text='Paid')
table_order.heading('complexity', text="Complexity")
table_order.heading('number', text="Num")
table_order.heading('rating', text='Rating')
table_order.heading('relevance', text='Relevance')
table_order.heading('term', text='Term')

table_order.column('name',width=100, anchor='center')
table_order.column('paid',width=50, anchor='center')
table_order.column('complexity',width=80, anchor='center')
table_order.column('number',width=30, anchor='center')
table_order.column('rating',width=50, anchor='center')
table_order.column('relevance',width=80, anchor='center')
table_order.column('term',width=30, anchor='center')
table_order.place(x=250,y=50)

index = 1
for order in company.order_list:
    table_order.insert('', index=index, values=(str(index), str(order.complexity), str(order.name), str(order.paid), str(order.rating), str(order.relevance), str(order.term)))
    index += 1
# end of code tabel with  ----------------

# ------------------------------------
# tabel with company free orders
columns_free_order=('number', 'complexity', 'name', 'paid', 'rating', 'relevance', 'term')
table_free_order=ttk.Treeview(window, show='headings', columns=columns_free_order)

table_free_order.heading('name', text='Name')
table_free_order.heading('paid', text='Paid')
table_free_order.heading('complexity', text="Complexity")
table_free_order.heading('number', text="Num")
table_free_order.heading('rating', text='Rating')
table_free_order.heading('relevance', text='Relevance')
table_free_order.heading('term', text='Term')

table_free_order.column('name',width=100, anchor='center')
table_free_order.column('paid',width=50, anchor='center')
table_free_order.column('complexity',width=80, anchor='center')
table_free_order.column('number',width=30, anchor='center')
table_free_order.column('rating',width=50, anchor='center')
table_free_order.column('relevance',width=80, anchor='center')
table_free_order.column('term',width=30, anchor='center')

table_free_order.place(x=250,y=270)

index = 1
for order in list:
    table_free_order.insert('', index=index, values=(str(index), str(order.complexity), str(order.name), str(order.paid), str(order.rating), str(order.relevance),
                                                    str(order.term)))
    index += 1
# end of code tabel with free orders----------------

button_worker=tk.Button(window, text='hire worker', bg='blue', width=10)
button_worker.place(x=70, y=500)


entry_worker=tk.Entry(window, width=5)
entry_worker.place(x=10, y=500)


def handler_button():
    print(entry_worker.get())
    index=int(entry_worker.get()) -1
    company.hire(workers_list[index])

    for row in table_company.get_children():
        table_company.delete(row)
    index = 1
    for worker in company.employees_list:
        table_company.insert('', index=index, values=(str(index), str(worker.name), str(worker.salary), str(worker.ability)))
        index += 1

    workers()

    for row in table.get_children():
        table.delete(row)
    index = 1
    for worker in workers_list:
        table.insert('', index=index, values=(str(index), str(worker.name), str(worker.salary), str(worker.ability)))
        index += 1




button_order=tk.Button(window, text='accept order', bg='green', width=10)
button_order.place(x=310, y=500)


entry_order=tk.Entry(window, width=5)
entry_order.place(x=250, y=500)


def handler_button2():
    print(entry_order.get())
    index=int(entry_order.get()) -1

    company.get_order(list[index])

    for row in table_order.get_children():
        table_order.delete(row)
    index = 1
    for order in company.order_list:
        table_order.insert('', index=index, values=(str(index), str(order.complexity), str(order.name), str(order.paid), str(order.rating), str(order.relevance), str(order.term)))
        index += 1

    order_list()

    for row in table_free_order.get_children():
        table_free_order.delete(row)
    index = 1
    for order in list:
        table_free_order.insert('', index=index, values=(str(index), str(order.complexity), str(order.name), str(order.paid), str(order.rating), str(order.relevance), str(order.term)))
        index += 1



button_worker['command']=handler_button
button_order['command']=handler_button2

def one_day_handler():
    global DAYS
    company.do_order()
    for row in table_order.get_children():
        table_order.delete(row)
    index = 1
    for order in company.order_list:
        table_order.insert('', index=index, values=(str(index), str(order.complexity), str(order.name), str(order.paid), str(order.rating), str(order.relevance), str(order.term)))
        index += 1

    for row in table_free_order.get_children():
        table_free_order.delete(row)
    index = 1
    for order in list:
        table_free_order.insert('', index=index, values=(str(index), str(order.complexity), str(order.name), str(order.paid), str(order.rating), str(order.relevance), str(order.term)))
        index += 1

    if company.money<=0:
        tkMessageBox.showerror("end","you bankrupt")


    money['text']='your money: ' + str(company.money)
    days_label['text']='day number: ' + str(DAYS+1)
    if DAYS %30==0:
        company.salary_payment()

    DAYS+=1
button_game=tk.Button(window, width=20, height=2, text='next day', font=tkFont.Font(size=36), command=one_day_handler)
button_game.place(x=10, y=600)
# entry_game



window.mainloop()

