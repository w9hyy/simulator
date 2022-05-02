

class Company:
    def __init__(self):
        self.money = 100
        self.employees = 1
        self.rating = 1
        self.employees_list = []
        self.order_list = []
        self.worker_str_list = []

    def do_order(self):
        print("do order")
        self.order_list[0].term-=1
        if self.order_list[0].term==0:
            self.get_paid()


    def print_workers(self):
        print("works in your company: " + str(self.employees))
        print("name | ability | salary")
        index = 0
        for worker in self.employees_list:
            print(str(index) + ' | ' + str(worker.name) + ' | ' + str(worker.ability) + ' | ' + str(worker.salary))
            index += 1

    def print_orders(self):
        # complexity, name, paid, rating, relevance, term
        print('in progress five order ')
        print("complexity | name | paid | rating | relevance | term")
        index = 0
        for order in self.order_list:
            print(str(index) + ' | ' + str(order.name) + ' | ' + str(order.complexity) + ' | ' + str(order.paid) + ' | ' + str(order.rating) + ' | ' + str(order.relevance) + ' | ' + str(order.term))
            index += 1

    def print_data(self):
        print("your reting: " + str(self.rating))
        print("in your account: " + str(self.money) + '$')
        self.print_orders()
        self.print_workers()

    def hire(self, worker):
        self.employees += 1
        self.employees_list.append(worker)

    def fire(self):
        self.print_workers()
        self.employees -= 1
        number = input('choose en employee- ')
        self.employees_list.pop(number)

    def salary_payment(self):
        self.money -= 10 * self.employees

    def get_paid(self):
        self.money += self.order_list[0].paid

    def get_order(self, order):
        self.order_list.append(order)


class Order:
    def __init__(self, complexity, name, paid, rating, relevance, term):
        self.name = name
        self.complexity = complexity
        self.paid = paid
        self.rating = rating
        self.term = term
        self.relevance = relevance


class Worker:
    def __init__(self, name, ability, salary):
        self.name = name
        self.salary = salary
        self.ability = ability

