################################################################################
# Description: Bank Account exercise
################################################################################
class Account:
    def balance(self, deposit, withdraw, get_balance):
        self.deposit = deposit
        self.withdraw = withdraw
        self.get_balance = get_balance

class Savings(Account):
    def accure_interest(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

def main():


if __name__ == '__main__':
    main()
