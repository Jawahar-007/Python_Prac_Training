from datetime import date,timedelta

class Train_ticket:

    def __init__(self,cusname,book_amt,depTime,book_time,cancel_time):
            self.book_amt = book_amt
            self.book_time = book_time
            self.cusname = cusname 
            self.depTime = depTime
            self.cancel_time = cancel_time
            self.return_amount = 0
    
    def fine_calc(self):
        days_diff = (self.depTime - self.cancel_time).days
        
        if(self.book_time > self.cancel_time >= self.depTime):
            self.return_amount = 0
            print ("Cancellation not Allowed , No Refund Available from Train Journey Depature Date !!")
        
        elif (self.book_time - self.cancel_time).days <= 2:
             return f"Refund Amount: ₹ {int(self.book_amt)}"

        else:
            
            if(self.book_time < self.cancel_time < self.depTime):
                
                if days_diff < 2:
                    return f"Refund Amount : ₹ 0" #no Refund for less than 2 days
                elif (days_diff == 2):
                    return f"Refund Amount : ₹ {int(0.3 * self.return_amount)}" # Refund 

                elif ((days_diff >= 3) and (days_diff <= 5)):
                    return f"return_amount = ₹ {int(0.5 * self.book_amt)}"
                
                elif days_diff in [6,7]:
                   return f"Refund Amount : ₹ {int(0.9 * self.return_amount)}"

                elif( days_diff >=7):
                    return f"Refund Amount : ₹ {int(self.return_amount)}"
        
        
                
today = date.today()
print("Today : ",today)
print("7 days before:",today - timedelta(days= 7))
print("6 days before:",today - timedelta(days= 6))
# pass the input arg Train_ticket  (cusname , book_amt , dept_date , book_date , cancel_date)
ticket1 = Train_ticket('Rogan',2000,today,today - timedelta(7),today - timedelta(7))
# ticket2 = Train_ticket('Baasha',3000,)
print(ticket1.fine_calc())  