class BankAccount:
    def __init__(self, name, phone, balance= 0.00):
        self.name= name
        self.phone= phone
        self.balance= balance

    def deposit(self, amount):
        if amount >=0:
            self.balance += amount
            print(f"Successful deposit {amount:.2f} to {self.name } account ")


        else:
            print("Invalid deposit amount: ")           
    

    def withdraw (self, amount):
        if 0 < amount <= self.balance:  
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} from {self.name}'s account.")
      
        else:
            print("Invalid withdrawal amount or insufficient amount ")

    def get_amount(self):
       return f"{self.name}'s current balance: ${self.balance:.2f}"





ram = BankAccount("RAM THAPA", "9865665665" )
ram.deposit(5000)
ram.withdraw(1000)
print(ram.get_amount())




hari = BankAccount("Hari KC", "985451265")
hari.deposit(10000)
hari.withdraw(2000)
print(hari.get_amount())

shyam = BankAccount("Shyam Nepal", "984652121")
shyam.deposit(20000)
shyam.withdraw(1500)
print(shyam.get_amount())



# #create three different bank account objects
# account1 = BankAccount(" Ram", "9845265621", " 500.0")

# account2 = BankAccount = ("Gopal", "9862313442", "400.0" )



