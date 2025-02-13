class Bank:
    # Base class methods
    def get_roi(self):
        return 10.0
    def get_balance(self):
        return 1000
    def get_account_type(self):
        return "Savings"
    def get_min_balance(self):
        return 1000
    def get_min_balance_penalty(self):
        return 100
    def get_interest(self):
        return 0.1

class SBI(Bank):
    # Overriding methods in SBI subclass
    def get_roi(self):
        return 8.0
    def get_min_balance_penalty(self):
        return 200
    def get_interest(self):
        return 0.2
    def get_account_type(self):
        return "Current"
    def get_min_balance(self):
        return 2000
    
class HDFC(Bank):
    # Overriding methods in HDFC subclass
    def get_roi(self):
        return 7.0
    def get_min_balance_penalty(self):
        return 300
    def get_interest(self):
        return 0.3
    def get_account_type(self):
        return "Savings"
    def get_min_balance(self):
        return 3000

s = Bank()
print("Rate of Interest in Bank:", s.get_roi())
print("Minimum Balance Penalty in Bank:", s.get_min_balance_penalty())
print("Interest in Bank:", s.get_interest())
print("Account Type in Bank:", s.get_account_type())
print("Minimum Balance in Bank:", s.get_min_balance())

# Creating instances of SBI and HDFC
s1 = SBI()
print("Rate of Interest in SBI:", s1.get_roi())
print("Minimum Balance Penalty in SBI:", s1.get_min_balance_penalty())
print("Interest in SBI:", s1.get_interest())
print("Account Type in SBI:", s1.get_account_type())

s2 = HDFC()
print("Rate of Interest in HDFC:", s2.get_roi())
print("Minimum Balance Penalty in HDFC:", s2.get_min_balance_penalty())
print("Interest in HDFC:", s2.get_interest())
print("Account Type in HDFC:", s2.get_account_type())
print("Minimum Balance in HDFC:", s2.get_min_balance())