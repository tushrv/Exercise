class TipCalculator:
    def __init__(self, bill, tip_percent, num_people):
        self.bill = bill
        self.tip_percent = tip_percent / 100
        self.num_people = num_people

    def calculate_tip(self):
        return self.bill * self.tip_percent

    def calculate_total_bill(self):
        return self.bill + self.calculate_tip()

    def calculate_per_person_cost(self):
        return round(self.calculate_total_bill() / self.num_people, 2)

if __name__ == "__main__":
    print("Welcome to the tip calculator!")
    bill = float(input("What was the total bill? $"))
    tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
    people = int(input("How many people to split the bill?"))

    calculator = TipCalculator(bill, tip, people)
    cost_per_person = calculator.calculate_per_person_cost()

    print(f"Each person should pay: ${cost_per_person}")

