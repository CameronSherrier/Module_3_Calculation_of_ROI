class RoIcalculator():

    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.cashflow = 0
        self.totalinvestment = 0
        self.annualCashFlow = 0
    
    def calcIncome(self):
        response_Income = input("Please enter amount received from renting [$$]: ")

        self.income += int(response_Income)
        response_MiscIncome = input("If any misc. income [ex: Laundry, storage, etc] please enter here: ")
        self.income += int(response_MiscIncome)
        print(f'Your total Monthly Rental Income is: {self.income}')

    def calcExpenses(self):
        response_Tax = input("Enter Monthly Tax: ")
        self.expenses += int(response_Tax)
        response_Insurance = input("Enter Monthly Insurance Cost: ")
        self.expenses += int(response_Insurance)
        response_Utilities =  input("Enter the total amount for Utilities: ")
        self.expenses += int(response_Utilities)
        response_HOA = input("Enter HOA and Lawn/Snow service total: ")
        self.expenses += int(response_HOA)
        response_Repair = input("Enter Repair, Vacancy and CapEx total: ")
        self.expenses += int(response_Repair)
        response_Management = input("Total expenses for a Property Manager: ")
        self.expenses += int(response_Management)
        response_Mortgage = input("What is your Mortgage?: ")
        self.expenses += int(response_Mortgage)
        print(f'We have grand expense total of {self.expenses}. Oh boy, lets see how we do next!')
    
    def calcCashFlow(self):
        difference = self.income - self.expenses
        self.cashflow += difference
    
    def calcTotalInvesment(self):
        response_DownPayment = input("Total of Down Payment and Closing Costs: ")
        self.totalinvestment += int(response_DownPayment)
        response_Rehab = input("Total Rehab and Misc. Costs: ")
        self.totalinvestment += int(response_Rehab)

    def calcAnnualCashFlow(self):
        acf = self.cashflow * 12
        self.annualCashFlow += acf

    def calcROI(self):
        roi = self.annualCashFlow / self.totalinvestment
        percent = roi * 100
        print(f'Your Return of investment [ROI] is: {percent}%')


sherrier_RoIcalculator = RoIcalculator()

def run():
    flag = True
    while flag:

        print("Welcome to Sherrier's ROI Calculator! Here we will be calculating the costs of expense vs. the income being generated from it. This will return a percentage of how much you will make back from the propertly over the year. The choice is yours to make if you deem the percentage worthy enough to make the investment!")
        
        print("I'm going to ask you a series of questions crucial to the calculation. After which I will inform you of the ROI %. Please answer to the best of your knowledge.")
        sherrier_RoIcalculator.calcIncome()
        print(f'Now that you are generating {sherrier_RoIcalculator.income}/m, lets find out your expenses!')
        sherrier_RoIcalculator.calcExpenses()
        sherrier_RoIcalculator.calcCashFlow()
        print(f'This gives you a Total Cash Flow of: {sherrier_RoIcalculator.cashflow}/m')
        print("Lets take a peek at your total investment.")
        sherrier_RoIcalculator.calcTotalInvesment()
        sherrier_RoIcalculator.calcAnnualCashFlow()
        print(f'Now we take your Annual Cash Flow {sherrier_RoIcalculator.annualCashFlow} and divide by Total Investment {sherrier_RoIcalculator.totalinvestment}')
        sherrier_RoIcalculator.calcROI()
        flag = False

run()