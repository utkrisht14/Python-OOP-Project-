
from flat import Bill, Flatmate

from reports import PDFReport


amount = float(input("Hey user. Enter the bill amount: "))
period = input("What is the bill period? E.g. December 2020: ")
print("This is an: ",amount)

name1 = input("What is your name: ")
days_in_house1 = int(input(f"How many days {name1} stay in the house during the period."))

name2 = input("What is flatmate name: ")
days_in_house2 = int(input(f"How many days {name2} stay in the house during the period."))

the_bill = Bill(amount, period=period)
flatmate1 = Flatmate(name=name1, days_in_house=days_in_house1)
flatmate2 = Flatmate(name=name2, days_in_house=days_in_house2)

print(f"{flatmate1.name} Pays: {flatmate1.pays(bill=the_bill, flatmate2=flatmate2)}")
print(f"{flatmate2.name} Pays: {flatmate2.pays(bill=the_bill, flatmate2=flatmate1)}")

pdf_report = PDFReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)