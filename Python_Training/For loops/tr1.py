from datetime import date, timedelta

class TrainTicket:
    def __init__(self, cus_name, book_amt, dep_time, book_time, cancel_time):
        self.cus_name = cus_name
        self.book_amt = book_amt
        self.dep_time = dep_time
        self.book_time = book_time
        self.cancel_time = cancel_time
        print(f"Initialized TrainTicket for {self.cus_name}: Booked on {self.book_time}, Departure on {self.dep_time}, Cancelled on {self.cancel_time}")
    
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

# Testing the logic
today = date.today()
print("Today :", today)

# Example ticket
ticket1 = TrainTicket('Rogan', 2000, today, today - timedelta(7), today - timedelta(5))
print(ticket1.calculate_refund())
