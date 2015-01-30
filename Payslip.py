class payslip:
    def __int__(self):
        self.name = None
        self.number = None
        self.rate = None
        self.hour = None

new_record = payslip()
new_record.name = input("Please enter the employees name: ")
new_record.number = input("Please enter the employees number: ")
new_record.rate= float(input("Please enter the employees pay rate: "))
new_record.hours = float(input("Please input the number of hours worked: "))

total_pay= new_record.rate * new_record.hours
print("""Name: {0}
Number: {1}
Pay Rate: £{2}
Hours: {3}

Total Pay: £{4:.2f}""".format(new_record.name,new_record.number,new_record.rate,new_record.hours,total_pay))

