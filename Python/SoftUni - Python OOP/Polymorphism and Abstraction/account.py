
class Account:
    def __init__(self, owner: str, amount=0):
        self.owner = owner
        self.amount = amount
        self.starting_amount = amount
        self._transactions = []

    def handle_transaction(self, transaction_amount):
        if self.amount + transaction_amount < 0:
            raise ValueError("sorry cannot go in debt!")
        self.amount += transaction_amount
        self._transactions.append(transaction_amount)
        return f"New balance: {self.amount}"

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        self.handle_transaction(amount)

    @property
    def balance(self):
        return sum(self._transactions) + self.starting_amount

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.starting_amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, item):
        return self._transactions[item]

    def __reversed__(self):
        return reversed(self._transactions)

    def __lt__(self, other):
        return self.amount < other.amount

    def __le__(self, other):
        return self.amount <= other.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __ne__(self, other):
        return self.amount != other.amount

    def __gt__(self, other):
        return self.amount > other.amount

    def __ge__(self, other):
        return self.amount >= other.amount

    def __add__(self, other):
        owner = f"{self.owner}&{other.owner}"
        amount = self.starting_amount + other.starting_amount
        new_account = Account(owner, amount)
        new_account._transactions = self._transactions + other._transactions
        return new_account


acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)
