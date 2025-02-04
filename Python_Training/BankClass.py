class BankTrans:
    totalBalance = 0
    # def __init__(self,balance):
    #     self.balance = balance
    def checkBalance(self):
        print(f"Total Balance: ₹{BankTrans.totalBalance}")  

    def deposit(self,depAmt):

        #self.totalBalance += depAmt
        BankTrans.totalBalance += depAmt
        print(f"Deposited Amount: {depAmt} , Updated Balance: ₹{BankTrans.totalBalance}")

    def withdrawal(self,withrAmt):
        if withrAmt > BankTrans.totalBalance:
            print(f"Insufficient Balance! Cannot withdraw ₹{withrAmt}, Available Balance: ₹{BankTrans.totalBalance}")
            return

        BankTrans.totalBalance -= withrAmt
        
        if BankTrans.totalBalance < 1000:
            print(f"Be Fined!! Not maintained minnimum balance of ₹1000 ,Total Balance: ₹{BankTrans.totalBalance}")
        else:
            print(f"Total Amount Withdrawn: ₹{withrAmt} , Check Account Balance :₹{BankTrans.totalBalance}")

#Create an instance of BankTrans class
bank = BankTrans()

# Main_Driven 

while (True):
    ch = input(""" \n Welcome To BankTez 
                Press 1. Deposit
                      2. Withdrawal
                      3. Check Balance 
                      4. Exit
                Your Choice : """)
    match ch:
        case '1':
            depoAmt = int(input("Enter the Deposit amount: ₹"))
            bank.deposit(depoAmt)
        
        case '2':
            withdrawalAmt = int(input("Enter the amt to be Withdrawn: ₹"))
            bank.withdrawal(withdrawalAmt)
        
        case '3':
            bank.checkBalance()

        case '0':
            break
        
        case _:
            print("Enter the proper choice 1/2/3")
            continue
            

    ch1 = input("Do you want to continue (Y/N)")
    if ch1 == 'y' or ch1 == 'Y':
        continue 
    elif ch1 == 'n' or ch1 == 'N':
        break
    else:
        print("Enter Proper choice (Y/N)")
        continue 


# bank.deposit(5000)
# bank.deposit(10000)
