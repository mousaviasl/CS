class Calendar:
    def __init__(self):
        self.name_of_month: 'February'
        self.days_in_month: 0
        
    def month_info(self, incomingMonth, incomingDays):
        self.name_of_month = incomingMonth
        self.days_in_month = incomingDays
        print('Month: ' + self.name_of_month)
        print('Days in month: ' + self.days_in_month)
        
        
myCalendar = Calendar()
month = input("What is the name of the month?")
days = input("How many days are in the month?")
myCalendar.month_info(month, days)
