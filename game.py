import time

import myclass
import random

company = myclass.Company()
company.print_data()

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




# order_list()
# print_order_list()
# choose_order()
# counter = 0
#
#
# while True:
#     print("day number", counter)
#     counter+=1
#
#     if company.money < 0:
#         print('you are bankrupt')
#         break
#     else:
#         print('____________________________________________')
#         company.print_data()
#         print('want to hire a ew employee? ')
#         answer = str(input())
#         yes = 'yes'
#         if answer == yes:
#             workers()
#             choose_worker()
#         company.do_order()
#         time.sleep(3)

