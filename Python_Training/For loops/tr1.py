from datetime import datetime,date, timedelta

class TrainTicket:
    def __init__(self, cus_name, book_amt, dep_date, book_date, cancel_date):
        self.cus_name = cus_name
        self.book_amt = book_amt
        self.dep_date = dep_date
        self.book_date = book_date
        self.cancel_date = cancel_date
        print(f"Initialized TrainTicket for {self.cus_name}: Booked on {self.book_time}, Departure on {self.dep_time}, Cancelled on {self.cancel_time}")
    
    def booking_module(self,):
        print("Welcome to the Booking Section of LocoTez ")
        
    def calculate_refund(self):
        print(f"Calculating refund for {self.cus_name}...")
        days_diff = (self.dep_time - self.cancel_time).days
        print(f"Days {days_diff}")

        if self.cancel_time >= self.dep_time:
            print("Cancellation not allowed from departure date.")
            return "Cancellation not allowed, No refund available from departure date!"
        
        if (self.cancel_time - self.book_time).days <= 2:
            print("Full refund applicable.")
            return f"Refund Amount: ₹ {int(self.book_amt)}"
        
        if self.book_time < self.cancel_time < self.dep_time:
            print("Processing refund based on cancellation date.")
            if days_diff < 2:
                print("No refund applicable.")
                return "Refund Amount: ₹ 0"
            elif days_diff == 2:
                print("30% refund applicable.")
                return f"Refund Amount: ₹ {int(0.3 * self.book_amt)}"
            elif 3 <= days_diff <= 5:
                print("50% refund applicable.")
                return f"Refund Amount: ₹ {int(0.5 * self.book_amt)}"
            elif days_diff in [6, 7]:
                print("90% refund applicable.")
                return f"Refund Amount: ₹ {int(0.9 * self.book_amt)}"
            else:
                print("Full refund applicable.")
                return f"Refund Amount: ₹ {int(self.book_amt)}"

        print("Invalid cancellation date.")
        return "Invalid cancellation date."
    
def datechecker(input_date):
    date_formats = ["%Y-%m-%d","%m-%d-%Y","%d-%m-%Y","%d/%m/%Y"]
        
    for date_format in date_formats:
        try:
            date_obj = datetime.strptime(input_date,date_format).date()
            break
        except ValueError:
            pass
    if date_obj:
        return date_obj
    else:
        return "Invalid Date Format. Try for the date format(DD-MM-YYYY)"


# Testing the logic
today = date.today()
print("Today Date:", today)

#ticket1 = TrainTicket(cusName, 2000, today, today - timedelta(7), today - timedelta(5))

# Example ticket
cusName = input("Enter Passenger Name: ") #Input of Cusname

while(True):
    ch = input(""" Welcome To LocoTez
               Press 
                    1. Booking 
                    2. Cancel Booking
                    3. Exit """)
    
    match ch:
        case '1':
            dep_date_string = input("Enter the departure date of Train: ")
            dep_date = datechecker(dep_date_string)
            book_date_string = input("Enter the booking date for the Journey of Train at ",dep_date_string)
            book_date = datechecker(book_date_string)
            booking_List = [dep_date,book_date]






print(ticket1.calculate_refund())
