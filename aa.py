from abc import ABC,abstractmethod
class person:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def getid(self):
        return self.id
    def getname(self):
        return self.name
    def setid(self,id):
        self.id=id
    def setname(self,name):
        self.name=name
class User(person):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
class expense(ABC):
    def __init__(self,amount,paid_by,part):
        self.amount=amount
        self.paid_by=paid_by
        self.part=part

    @abstractmethod
    def split(self):
        pass
class equal(expense):
    def split(self):
        split_amount=self.amount/len(self.part)
        return {user_id:split_amount for user_id in self.part}
class exact(expense):
    def split(self):
        return self.part
class percent(expense):
    def split(self):
        return {user_id:(self.amount*percent)/100 for user_id,percent in self.part.items()}

class sharing():
    def __init__(self):
        self.users={}
        self.expenses=[]
        self.bal={}

    def adduser(self,id,name):
        if id not in self.users:
            self.users[id] = User(id, name)
            self.bal[id] = {}
    def addexp(self,expense):
        self.expenses.append(expense)
        self.update_balances(expense)
    def update_balances(self,expense):
        split = expense.split()
        for user_id, amount in split.items():
            if user_id != expense.paid_by:
                if user_id not in self.bal[expense.paid_by]:
                    self.bal[expense.paid_by][user_id] = 0
                if expense.paid_by not in self.bal[user_id]:
                    self.bal[user_id][expense.paid_by] = 0
                
                self.bal[expense.paid_by][user_id] += amount
                self.bal[user_id][expense.paid_by] -= amount
    def get_balances(self):
        return {self.users[user_id].name: {self.users[other_id].name: amount for other_id, amount in balance.items()} for user_id, balance in self.bal.items()}

app = sharing()
app.adduser(1, "Alice")
app.adduser(2, "Bob")
app.adduser(3, "Charlie")

equal_expense = equal(120, 1, [1, 2, 3])
exact_expense = exact(150, 2, {1: 100, 2: 50})
percent_expense = percent(200, 3, {1: 50, 2: 30, 3: 20})

app.addexp(equal_expense)
app.addexp(exact_expense)
app.addexp(percent_expense)

print(app.get_balances())
