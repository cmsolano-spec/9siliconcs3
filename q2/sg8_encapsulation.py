class BankAccount:
    def __init__(self, account_name, balance):
        self.__account_name = account_name
        self.__balance = 0
        self.set_balance(balance)

    #setter and getter methods for account name
    def set_account_name(self, account_name):
        self.__account_name = account_name

    def get_account_name(self):
        return self.__account_name

    #setter and getter methods for balance
    def set_balance(self, balance):
        if balance > 0:
            self.__balance = balance
        
            
    def get_balance(self):
        return self.__balance

a1 = BankAccount(12345, 1000) #Object
print("Account 1:")
print(f"Account name: {a1.get_account_name()}") #print the Bank account's name
print(f"Balance: {a1.get_balance()} \n" ) #balance

Input = -100 #Input of the user
a1.set_balance(Input) #sets the new balance

print(f"Update balance to {Input}") #Shows updates
if a1.set_balance(Input) is not None: #If not NOne(which is negative), continue print
    print(f"Balance: {a1.get_balance()}")
else:
    print("The balance must not be a negative number") #tells user invalid input

print(f"Account name: {a1.get_account_name()}") #print the Bank account's name
print(f"Balance: {a1.get_balance()}") #balance
