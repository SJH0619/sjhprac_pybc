class Transaction:
    def __init__(self, sender, reciver, amount):
        self.sender = sender
        self.reciver = reciver
        self.amount = amount

    def __str__(self):
        return self.sender + " to " + self.reciver + " " + str(self.amount)
