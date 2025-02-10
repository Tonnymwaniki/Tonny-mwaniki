class employee:
    def __init__(self,name,position,salary):
        self.name = name
        self.position = position
        self.salary = salary

    def detail(self):
        print(self.name,"is the",self.position)

employee1 = employee("john","manager","40000")
print(employee1.name,employee1.position,employee1.salary)
employee2 = employee("jane","managing director","4000")
print(employee2.name,employee2.position,employee2.salary)
employee3 = employee("john","clerk","500000")
employee4 = employee("john","ceo","80000")